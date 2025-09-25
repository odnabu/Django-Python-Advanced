# Link on GitHub: https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/apps.py
from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'

    # ____  SIGNALS ____
    # Этот метод вызывается, когда Django полностью загрузит приложение:
    def ready(self):
        # Импортируем наш модуль с сигналами:
        import library.signals
