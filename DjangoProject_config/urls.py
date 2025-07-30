# DjangoProject_config/urls.py

"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 24.07.2025 - Pr 9: Задание 2.1. Настройка TokenAuthentication   +++   hw_11:
from rest_framework.authtoken.views import obtain_auth_token
# Lesson 33 "Lec 30: JWT-аутентификация", 23.07.2025 - Basic Authentication:  +++   hw_11:
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),   #  __  NB! __ Может быть только в CONFIG!!!    # http://127.0.0.1:8000/admin/
    path('les_01_begins/', include('les_14_begins.urls')),  # Подключение маршрутов приложения les_01_begins.
                    # При этом в браузере нужно ввести: http://127.0.0.1:8000/les_01_begins/<адрес из VIEWS>.
    # path('', include('hw_01_first_app.urls')),          # Подключение маршрутов ТОЛЬКО из приложения hw_01_first_app.
                    # Если несколько приложений, то пустые кавычки '' здесь НЕЛЬЗЯ использовать!.
    path('hw_01_first_app/', include('hw_01_first_app.urls')),  # Так нужно делать, если у меня в
                    # проекте Пайчарм НЕ одно приложение, как сейчас: les_01_begins, hw_01_first_app.
                    # При этом в браузере нужно ввести: http://127.0.0.1:8000/hw_01_first_app/<адрес из VIEWS>
                    # (у меня для 1-ой функции ендпоинт hw-01/ и по нему выводится приветственное сообщение в браузере).
    path('hw-02/', include('hw_02_task_manager.urls')),     # HW_02 --> HW_06
    path('project/', include('project.urls')),              # 19-06-2026
]



# _____ HW_06 --->
# _____ 5. ДОПОЛНИТЕЛЬНО  -->  5.2.2. Подключение Swagger и ReDoc
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns += [
    # Схема и документация:
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


# 27.07.2025 - Pr 8: Задание 1: Представления и маршруты для модели Category
urlpatterns += [
    path('shop/', include('les_18_shop.urls')),
]


# -------------------------------------------------------------------------------------------
# # Lesson 33 "Lec 30: JWT-аутентификация", 23.07.2025 - Basic Authentication  +++   hw_11:
# # \\\\\\\\\\\\    СМОТРИ КОД НИЖЕ   //////////////
# urlpatterns += [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]
#
# # После перехода по адресу http://127.0.0.1:8000/api/token/ получим ТОКЕНЫ. НАПРИМЕР, такие:
# # {
# #     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MzM1NTAxNCwiaWF0IjoxNzUzMjY4NjE0LCJqdGkiOiIxYTg0ZTAxZTk3Y2Q0ZDBhOTM3Mzg4YzQ1ZjU5NjY5YSIsInVzZXJfaWQiOiIxIn0.lzw1c2ORDr-mp3V3LEASWjvERmKpRBNBrEfHKSfFVDs",
# #     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzMjY4OTE0LCJpYXQiOjE3NTMyNjg2MTQsImp0aSI6ImQ2ZTIwZWQ2OGE2MjQ2ZjE4ZDBkNmU4NWRiMzY1NGVjIiwidXNlcl9pZCI6IjEifQ.j4bMYT7dWA-UQiRa2oCMXo5rJSiTKFwDj3lpm7i_d7k"
# # }
# # НАСТРОЙКИ времени смотри в DjangoProject_config/settings.py:
# #   refresh - действует 1 день.
# #   access - действует 5 минут.
# -------------------------------------------------------------------------------------------


# 24.07.2025 - Pr 9: Задание 2.1. Настройка TokenAuthentication
# Настройте аутентификацию с использованием токенов.
urlpatterns += [
    # Маршрут для получения токена:
    path('get-token/', obtain_auth_token, name='get_token'),

    # Маршрут для получения access и refresh токенов
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Маршрут для обновления access токена с помощью refresh токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
