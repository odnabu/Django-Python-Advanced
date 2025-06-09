from enum import unique
from tkinter.constants import CASCADE

from django.db import models
from django.core.validators import MinLengthValidator   # Список валидаторов: https://django.fun/docs/django/5.0/ref/validators/



# ___ Модель Category __________________________________________________________________________________________

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории', help_text='Категория выполнения')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



# ___ Модель Task __________________________________________________________________________________________

class Task(models.Model):
    title = models.CharField(max_length=50,
                             validators=[MinLengthValidator(2)],    # В названии должно быть НЕ меньше 2 символов.
                             null=False,    # для БАЗЫ ДАННЫХ.
                             blank=False,   # для ФОРМ.
                             verbose_name='Название задачи',
                             help_text='Введите название задачи, иначе будет присвоено название по умолчанию Task+Number',
                             unique_for_date='publish_date',
                             error_messages={'unique_for_date': 'Это название уже используется для сегодняшней даты. '
                                                                'Введите другое название.'} )
    # ДОПОЛНИТЕЛЬНО к полю title смотри в конце функцию save.
    publish_date = models.DateField(auto_now=True,)
    description = models.TextField(blank=True, verbose_name='Описание задачи')

    # categories: Категории задачи. Многие ко многим.
    categories = models.ManyToManyField(Category, related_name='tasks', verbose_name='Категория',
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

    def __str__(self):
        return self.title


# ___ Модель SubTask __________________________________________________________________________________________

class SubTask(models.Model):
    title = models.CharField(max_length=50,
                             blank=True, verbose_name='Название подзадачи',
                             help_text='Отдельная часть основной задачи')
    description = models.TextField(blank=True, verbose_name='Описание подзадачи')

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

    def __str__(self):
        return self.title


