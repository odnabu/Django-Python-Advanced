# 1.08.2025 - Консультация 5 по финанльному проекту.

from django.test import TestCase
from rest_framework.test import APITestCase

import pytest
from hw_02_task_manager.models import Task

# ПЕРЕДЕЛАТЬ ПОД Tasks

# Для запуска ввести в терминале команду из одного слова:  pythest

# Пометка, которая говорит pytest, что этот тест может работать с базой данных
@pytest.mark.django_db
def test_task_model():
    """
    Тест для проверки создания объекта Task и работы кастомного метода is_classic().
    """
    # 1. Arrange (Подготовка): Создаем объект в памяти
    # эта функция работает как транзакция, т.е. в БД данные не вностяся.
    task = Task.objects.create(
        title="Testing of Apps in Django",
        # categories="Learning",
        # status="New"
        deadline = "2025-08-02T00:00:00Z"
    )

    # 2. Act (Действие) & Assert (Проверка)
    # Проверяем, что объект создался и его поля соответствуют ожидаемым
    assert task.title == "Testing of Apps in Django"
    assert str(task) == "Testing of Apps in Django" # Проверяем работу метода __str__

    # # Проверяем наш кастомный метод --- У МЕНЯ В модели ТАСК НЕТ кастомного метода.
    # # assert task.is_classic() is True
    #
    # # Создадим другую книгу для проверки обратного случая
    # book_modern = Task.objects.create(
    #     title="Testing of Apps in Django - Reverse",
    #     categories="Learning",
    #     status="New"
    # )
    # # В этом примере она тоже будет классикой, поменяем на более новый год
    # book_modern.publication_year = 2007
    # assert book_modern.is_classic() is False
