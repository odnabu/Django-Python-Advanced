# HW_06

from rest_framework import serializers
from hw_02_task_manager.models import Task, SubTask, Category
from rest_framework.exceptions import ValidationError
from datetime import date
# ____  Для home_work_08  ____
import datetime
# ____  Для home_work_14  ____
from django.contrib.auth.models import User




# ДОПОЛНИТЕЛЬНО к "home_work_07.md": чтобы в детальном представлении задачи отображались и связанные
# с ней подзадачи. Для этого используются вложенные сериализаторы в Django REST Framework.
# Сериализатор для коротких подзадач:
class SubTaskTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['title']  # только название подзадачи


# ///////   home_work_06.md    /////////

# _____ 1.2.1 Создание сериализатора для модели `Task`

class TaskSerializer(serializers.ModelSerializer):

    # ДОПОЛНИТЕЛЬНО к "home_work_07.md":
    subtasks = SubTaskTitleSerializer(many=True, read_only=True)

    # ____  Для к "home_work_08.md"  ____
    deadline_weekday = serializers.SerializerMethodField()

    class Meta:
        model = Task
        # ____  Для "home_work_07.md"  ____
        # fields = ['id', 'title', 'deadline', 'subtasks']
        # fields = '__all__'

        # ____  Для к "home_work_08.md"  ____
        fields = ['id', 'title', 'owner', 'deadline', 'deadline_weekday', 'status', 'subtasks']

        # ____  Для к "home_work_13.md", задание 1  ____
        read_only_fields = ['owner']  # Делаем поле 'owner' только для чтения

    # Для к "home_work_08.md":
    def get_deadline_weekday(self, obj):
        # Преобразование даты в день недели:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if obj.deadline:
            return days[obj.deadline.weekday()]  # .weekday() → 0=Monday ... 6=Sunday
        return None

    # _____ home_work_07   4. Валидация данных в сериализаторах:
    def validate_deadline(self, value):
        if value < date.today():
            raise ValidationError("Deadline can't be in the past.")
        return value


# _____ 5. ДОПОЛНИТЕЛЬНО  -->  5.2.2. Подключение Swagger и ReDoc  -->  Примечания
# from rest_framework import serializers
#
# class TaskStatisticsSerializer(serializers.Serializer):
#     total_tasks = serializers.IntegerField()
#     completed_tasks = serializers.IntegerField()




# //////////////   home_work_10   Задание 1. CRUD для категорий с использованием ModelViewSet     ////////////////////

# _____ hw_10:  1. Создайте `CategoryViewSet`, используя `ModelViewSet` для CRUD операций.
class CategorySerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    # Для подсчета кол-ва задач для категории:
    task_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'tasks', 'task_count', 'is_deleted', 'deleted_at']
        # fields = '__all__'

    # Подсчет количества задач по категориям:
    def get_task_count(self, request):
        return Task.objects.filter(categories=request).count()
# -------------------------------------------------------------------------------------------------------------



# ///////   home_work_07.md    /////////

# _____ 1.2. SubTaskCreateSerializer

class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        # fields = '__all__'           # ['id', 'title', 'description', 'status', 'deadline']
        # fields = ['id', 'title', 'description', 'status', 'deadline', 'task']
        fields = ['id', 'title', 'owner', 'description', 'status', 'deadline', 'task']
        read_only_fields = ['created_at']


# _____ 2.1. `CategoryCreateSerializer` с методом `create`

class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data['name']
        # Если вводится имя категории, которое уже существует в БД:
        if Category.objects.filter(name=name).exists():
            raise ValidationError(f"Category with name {name} already exists")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data['name']
        # Если вводится имя категории, которое уже существует в БД:
        if Category.objects.exclude(pk=instance.pk, name=name).filter(name=name).exists():
            raise ValidationError(f"Category with name {name} already exists")
        return super().update(validated_data)


# _____ 3. Использование вложенных сериализаторов

class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = '__all__'
        # fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at', 'task']
        # fields = ['id', 'title', 'status', 'deadline', 'task']

        # ____  Для к "home_work_13.md", задание 1  ____
        read_only_fields = ['owner']  # Делаем поле 'owner' только для чтения



    # Сериализатор, который использует только названия подзадач:
class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)     # , source='subtasks'

    # ____  Для "home_work_08.md"  ____
    weekday = serializers.SerializerMethodField()

    # ____  Для "home_work_10.md"  ____
    categories = CategoryCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Task

        # ДОПОЛНИТЕЛЬНО к "home_work_07.md":
        # fields = ['id', 'title', 'description', 'status', 'deadline', 'subtasks']
        # fields = '__all__'

        # Для к "home_work_08.md":
        fields = ['id', 'title', 'owner', 'description', 'status', 'deadline', 'weekday', 'created_at', 'categories', 'subtasks']
        # fields = '__all__'

    # _____ home_work_08:
    def get_weekday(self, obj):
        # Преобразование даты в день недели:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if obj.deadline:
            return days[obj.deadline.weekday()]  # .weekday() → 0=Monday ... 6=Sunday
        return None

    # _____ home_work_07   4. Валидация данных в сериализаторах:
    # def validate_deadline(self, value):
    #     if value < date.today():
    #         raise ValidationError("Deadline can't be in the past.")
    #     return value


# _____ 4. Валидация данных в сериализаторах

class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

        def validate_deadline(self, value):
            if value < date.today():
                raise ValidationError("Deadline can't be in the past.")
            return value




# ///////   home_work_14.md    /////////

# _____ 1. Регистрация пользователя
# Смотри пример les_18_shop/serializers.py  -->  24.07.2025 - Les 38, Lec 33: Регистрация пользователя с JWT.

class UserRegisterSerializer(serializers.ModelSerializer):
    # Делаем поле пароля только для записи (его нельзя будет прочитать из API)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # Используем create_user, чтобы пароль был правильно захеширован.
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

