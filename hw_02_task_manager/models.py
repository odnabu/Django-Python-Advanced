from enum import unique
from tkinter.constants import CASCADE

from django.db import models
from django.core.validators import MinLengthValidator   # Список валидаторов: https://django.fun/docs/django/5.0/ref/validators/
# *****  home_work_10  *****************************
from django.utils import timezone
from hw_02_task_manager.managers import SoftDeleteManager
# *****  home_work_13  *****************************
from django.contrib.auth.models import User
# или через get_user_model(), тогда добавить так:
# from django.contrib.auth import get_user_model
# User = get_user_model()



# ___ Модель Category __________________________________________________________________________________________

class Category(models.Model):
    name = models.CharField(max_length=50,
                            # verbose_name='Название категории',
                            help_text='Категория выполнения')

    # class Meta:
    #     verbose_name = 'Категория'
    #     verbose_name_plural = 'Категории'

    # ///////   home_work_03.md    /////////
    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name'),
        ]

    # ///////   home_work_10.md    /////////
    # Задание 2. Реализация мягкого удаления категорий.
    is_deleted = models.BooleanField(default=False)               # Поле для мягкого удаления.
    deleted_at = models.DateTimeField(null=True, blank=True)      # Дата удаления.

    objects = SoftDeleteManager()            # Менеджер по умолчанию (отфильтрованные) - для исключения удаленных записей
    all_objects = models.Manager()           # Стандартный менеджер (все записи)

    def delete(self, *args, **kwargs):
        """Переопределяем стандартный метод удаления."""
        self.is_deleted = True               # Устанавливаем флаг
        self.deleted_at = timezone.now()
        self.save()                          # Сохраняем изменения

    def restore(self):
        """Метод для восстановления записи."""
        self.is_deleted = False
        self.save()


    def __str__(self):
        return self.name          # Показывать полное название в выпадающих списках




# ___ Модель Task __________________________________________________________________________________________

class Task(models.Model):
    title = models.CharField(max_length=50,
                             validators=[MinLengthValidator(2)],    # В названии должно быть НЕ меньше 2 символов.
                             null=False,    # для БАЗЫ ДАННЫХ.
                             blank=False,   # для ФОРМ.
                             # verbose_name='Название задачи',
                             help_text='Введите название задачи, иначе будет присвоено название по умолчанию Task+Number',
                             unique_for_date='publish_date',
                             error_messages={'unique_for_date': 'Это название уже используется для сегодняшней даты. '
                                                                'Введите другое название.'} )
    # ДОПОЛНИТЕЛЬНО к полю title смотри в конце функцию save.
    publish_date = models.DateField(auto_now=True,)
    description = models.TextField(blank=True,
                                   # verbose_name='Описание задачи',
                                   )

    # categories: Категории задачи. Многие ко многим.
    categories = models.ManyToManyField(Category, related_name='tasks',
                                        # verbose_name='Категория',
                                        help_text='Категории, к которым относится задача')

    status_choices = [      # See  Pr01-Adpractice_PrfS1-04_06.pdf, p. 6.
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    status = models.CharField(choices=status_choices, verbose_name='Статус задачи')
    deadline = models.DateTimeField(help_text='Введите дату и время дедлайна.')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    # -------------------------------------------------------------------------------
    # ///////   home_work_13.md    /////////
    # _____ home_work_13   1:  Извлечение текущего пользователя из запроса:
    # Так как внутри моего проекта возник конфликт между МОДЕЛЯМИ приложений (project и hw_02_task_manager),
    # после доработки кода по примеру видео урока 35 и подсказки Чата, для вызова встроенной модели User
    # для таблицы с информацией о пользователях, нужно добавить связь (отношение Relation) между
    # моделью Task и моделью User с другим related_name, например, related_name=owned_tasks.
    # Тогда доработанная строка кода для Владельца (создателя) задачи:
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Owner", null=True, related_name='owned_tasks')
    # -------------------------------------------------------------------------------


    # def save(self, *args, **kwargs):
    #     """
    #     Функция для создания дефолтного названия задачи с ее номером == id,
    #     если пользователь не ввел название сам.
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     # Тк id в момент создания ещё не существует сначала нужно сохранить методом .save(),
    #     # чтобы получить ID. Это потому, что задача еще не сохранена в базе, а id присваивается
    #     # только при сохранении. Поэтому:
    #     if not self.id and not self.title:
    #         super().save(*args, **kwargs)       # Временное сохранение, чтобы id появился.
    #         self.title = f'Task {self.id}'      # Создание названия по умолчанию Task + номер записи в БД.
    #         kwargs['force_insert'] = False      # Создание названия по умолчанию происходит только если это нужно!
    #     super().save(*args, **kwargs)

    # ///////   home_work_03.md    /////////
    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_task_title'),
        ]

    def __str__(self):
        return self.title         # Показывать полное название в выпадающих списках


# ___ Модель SubTask __________________________________________________________________________________________

class SubTask(models.Model):
    title = models.CharField(max_length=50,
                             blank=True,
                             # verbose_name='Название подзадачи',
                             help_text='Отдельная часть основной задачи')
    description = models.TextField(blank=True,
                                   # verbose_name='Описание подзадачи',
                                   )

    # task: Основная задача. Один ко многим.
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks', help_text='Основная задача')

    status_choices = [  # See  Pr01-Adpractice_PrfS1-04_06.pdf, p. 6.
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    status = models.CharField(choices=status_choices, verbose_name='Статус подзадачи')
    deadline = models.DateTimeField(help_text='Введите дату и время дедлайна для этой подзадачи.')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания подзадачи')

    # -------------------------------------------------------------------------------
    # ///////   home_work_13.md    /////////
    # _____ home_work_13   1:  Извлечение текущего пользователя из запроса:
    # Так как внутри моего проекта возник конфликт между МОДЕЛЯМИ приложений (project и hw_02_task_manager),
    # после доработки кода по примеру видео урока 35 и подсказки Чата, для вызова встроенной модели User
    # для таблицы с информацией о пользователях, нужно добавить связь (отношение Relation) между
    # моделью Task и моделью User с другим related_name, например, related_name=owned_tasks.
    # Тогда доработанная строка кода для Владельца (создателя) ПОДзадачи будет с related_name=owned_SUBtasks:
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Owner", null=True, related_name='owned_subtasks')
    # -------------------------------------------------------------------------------


    # ///////   home_work_03.md    /////////
    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_subtask_title'),
        ]

    def __str__(self):
        return self.title         # Показывать полное название в выпадающих списках

