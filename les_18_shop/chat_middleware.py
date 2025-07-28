from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.urls import resolve
from django.http import JsonResponse

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Пропускаем проверку для определённых URL
        if request.path_info in ['/shop/login/', '/shop/registration/', '/shop/logout/']:
            return

        access_token = request.COOKIES.get('access_token')
        if access_token:
            try:
                # Проверим, валиден ли access_token
                AccessToken(access_token)
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
            except TokenError:
                pass  # токен истёк, попробуем обновить в process_response

    def process_response(self, request, response):

        # Если вдруг view_func(request) снова вернёт 401, добавь в начале process_response проверку:
        if getattr(request, 'refreshing_token', False):
            return response  # уже пытались обновить, не повторяем

        if (
            response.status_code == 401 and
            b"Token is invalid or expired" in response.content and
            request.COOKIES.get('refresh_token')
        ):
            try:
                refresh = RefreshToken(request.COOKIES['refresh_token'])
                new_access_token = str(refresh.access_token)
                new_refresh_token = str(refresh)

                # Устанавливаем новые токены
                response.set_cookie('access_token', new_access_token, httponly=True, samesite='Lax')
                response.set_cookie('refresh_token', new_refresh_token, httponly=True, samesite='Lax')

                # Повторно выполняем исходный запрос
                view_func, args, kwargs = resolve(request.path_info)
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {new_access_token}'
                request._refreshing_token = True  # флаг, чтобы не зациклиться

                new_response = view_func(request, *args, **kwargs)

                # Повторно устанавливаем куки в новом ответе
                new_response.set_cookie('access_token', new_access_token, httponly=True, samesite='Lax')
                new_response.set_cookie('refresh_token', new_refresh_token, httponly=True, samesite='Lax')

                return new_response

            except TokenError:
                # refresh тоже невалиден — удаляем куки
                response.delete_cookie('access_token')
                response.delete_cookie('refresh_token')

        return response


