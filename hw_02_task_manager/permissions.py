# //////////////      home_work_13    Задание 2: Реализация пермишенов для API       //////////////////////////////
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Кастомное разрешение, которое позволяет редактировать объект
    только его владельцу. Остальным доступно только чтение.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение (GET, HEAD, OPTIONS) даем всем.
        # SAFE_METHODS - это кортеж ('GET', 'HEAD', 'OPTIONS').
        if request.method in SAFE_METHODS:
            return True

        # Разрешения на запись (POST, PUT, PATCH, DELETE) даем только владельцу объекта.
        return obj.owner == request.user

# Из урока # 24.07.2025 - Python Adv 36: Практикум 10.
# class CanGetGenresStatisticPermission(BasePermission):
#     def has_permission(self, request, view):
#         # Проверяем, есть ли у пользователя право 'library.can_get_statistic'
#         # 'library' - это имя вашего Django-приложения
#         return request.user.has_perm('library.can_get_statistic')

