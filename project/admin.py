# Здесь РЕГИСТРИРУЕМ определенные в models.py модели:
from django.contrib import admin

# ДОБАВЛЯЕМ сюда МОДЕЛИ:
from project.models import Tag, Project, Developer, Task


# Сoздание красивого класса Администратора для модели Tag:
class TagAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('name',)
    # Задание полей по которым будет производиться поиск
    search_fields = ('name',)


# Сoздание красивого класса Администратора для модели Project:
class ProjectAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('name', 'created_at')
    # search_fields = ('name',)
    # Задание полей по которым будет производиться поиск
    readonly_fields = ('created_at',)
    search_fields = ('name',)


# Сoздание красивого класса Администратора для модели Developer:
class DeveloperAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('name', 'grade')
    # Задание полей по которым будет производиться поиск
    search_fields = ('name', 'grade')


# Сoздание красивого класса Администратора для модели ___:
class TaskAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('name', 'project__name', 'status', 'priority', 'created_at', 'due_date', 'assignee__username')    # project__name - для обращения к связанной модели __ .
    # Задание полей по которым будет производиться поиск
    search_fields = ('name',)
    list_filter = ('status', 'priority', 'project__name', 'created_at', 'due_date', 'assignee__username')




admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Task, TaskAdmin)

