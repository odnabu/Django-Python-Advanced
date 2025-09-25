# 24.07.2025 - Pr 10: Задание 2. Создание кастомных классов разрешений

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    A user permission that allows only the owner (user) to edit the object.
    Others are allowed to read only.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение (GET, HEAD, OPTIONS) даем всем.
        # SAFE_METHODS — это кортеж, содержащий ('GET', 'HEAD', 'OPTIONS').
        if request.method in SAFE_METHODS:
            return True

        # Разрешение на запись (POST, PUT, PATCH, DELETE) даем только владельцу объекта.
        return obj.user == request.user



# 24.07.2025 - Pr 10: Задание 3. Добавление эндпоинта для статистики. Часть 1
class CanViewOrderStatistics(BasePermission):
    """
    Allows access only to users who have the 'can_view_order_statistics' right.
    """
    def has_permission(self, request, view):
        # request.user.has_perm() проверяет, есть ли у пользователя
        # указанное разрешение.
        # Имя разрешения формируется как 'имя_приложения.имя_права'.
        return request.user.has_perm('les_18_shop.can_view_order_statistics')

