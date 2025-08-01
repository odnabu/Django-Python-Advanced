from django.apps import AppConfig


class Hw02TaskManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hw_02_task_manager'

    # Этот метод вызывается, когда Django полностью загрузит приложение
    def ready(self):
        import hw_02_task_manager.signals  # Импортируем наш модуль с сигналами
