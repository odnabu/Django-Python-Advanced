# Link on GitHub: https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/managers.py
# См. про МЯГКОЕ УДАЛЕНИЕ.
from django.db import models


class SoftDeleteManager(models.Model):
    """
    Sof Deletion for the data.
    """

    def get_queryset(self):
        """
        Переопределение базового QuerySet, чтобы по умолчанию
        исключать записи, помеченные как удаленные.
        """
        return super().get_queryset().filter(is_deleted=False)
