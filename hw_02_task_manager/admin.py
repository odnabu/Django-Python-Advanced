from django.contrib import admin
# ДОБАВЛЯЕМ сюда МОДЕЛИ:
from hw_02_task_manager.models import Category, Task, SubTask


# ///////   home_work_03.md    /////////

# Сoздание красивого класса Администратора для модели Category:
class CategoryAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('name',)
    # Задание полей по которым будет производиться поиск
    search_fields = ('name',)


# Сoздание красивого класса Администратора для модели Task:
class TaskAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('title', 'status', 'publish_date', 'description')
    # Задание полей по которым будет производиться поиск
    search_fields = ('title', 'publish_date', 'description')


# Сoздание красивого класса Администратора для модели SubTask:
class SubTaskAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('title', 'task', 'description', 'status', 'deadline', 'created_at')
    # Задание полей по которым будет производиться поиск
    search_fields = ('title', 'description', 'status', 'deadline', 'created_at')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)

