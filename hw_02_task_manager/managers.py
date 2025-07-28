# //////////////   home_work_10   Задание 2. Реализация мягкого удаления категорий     ////////////////////

from django.db import models


# class CategoryManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_deleted=False)


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        """
        Переопределяем базовый QuerySet, чтобы по умолчанию
        исключать записи, помеченные как удаленные.
        """
        return super().get_queryset().filter(is_deleted=False)

