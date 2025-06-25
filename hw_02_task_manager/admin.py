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


# ////////////  home_work_05 -- Inlines   /////////////////////////////////////

""" __  NB!  __ """ # Чтобы настроить ИНЛАЙНЫ в Админке, нужно сначала переместить код
# для SubTaskAdmin и для SubTaskInline выше TaskAdmin!!!

# Сoздание красивого класса Администратора для модели SubTask:
class SubTaskAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('title', 'task', 'description', 'status', 'deadline', 'created_at')
    # Задание полей по которым будет производиться поиск
    search_fields = ('title', 'description', 'status', 'deadline', 'created_at')

    # Функция, которая будет выполнять action в Админ-панели по массовому изменению
    # статуса Подзадачи на Done:
    def set_status_to_done(self, request, queryset):
        queryset.update(status='Done')

    set_status_to_done.short_description = "Set status to Done"     # Название функции в Админке.
    # Собственно, активация пользовательского действия в Админке:
    actions = [set_status_to_done]


# ____ 1. Подключение связанной модели SubTask с основной моделью Task для ИНЛАЙНА в Админке:
class SubTaskInline(admin.TabularInline):
    model = SubTask     # Вывод поля SubTask во вкладке Task.
    extra = 1           # Кол-во пустых форм для создания подзадач.



# Сoздание красивого класса Администратора для модели Task:
class TaskAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке объектов модели
    list_display = ('short_title', 'status', 'publish_date', 'description')     # здесь 'title' заменен на short_title.
    # Задание полей по которым будет производиться поиск
    search_fields = ('title', 'publish_date', 'description')
    # Добавление ИНЛАЙНОВ в Админку по дз 11 (05)
    inlines = [SubTaskInline]

    # ____ 2. Укороченный вариант Названия задач в Админ панели:
    # short_title — способ сократить текст в отображении списка.
    def short_title(self, obj):
        if len(obj.title) > 10:
            return f"{obj.title[:10]}..."
        return obj.title

    short_title.short_description  = "Title"


# """ __  NB!  __ """ # Можно прописать настройки для Админки и через декоратор. Например, так:
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'publish_date', 'description')
#     search_fields = ['title', 'publish_date', 'description']
#     list_filter = ['status']
#     fields = ['title', 'status']
#     list_per_page = 2


# ------------------------------------------------------------------------------
admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)
