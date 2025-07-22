# HW_06

from rest_framework import serializers
from hw_02_task_manager.models import Task, SubTask, Category
from rest_framework.exceptions import ValidationError
from datetime import date
# ____  Для home_work_08  ____
import datetime



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
    weekday = serializers.SerializerMethodField()

    class Meta:
        model = Task

        # Для к "home_work_07.md":
        # fields = ['id', 'title', 'deadline', 'subtasks']
        # fields = '__all__'

        # Для к "home_work_08.md":
        fields = ['id', 'title', 'deadline', 'weekday', 'subtasks']

    # Для к "home_work_08.md":
    def get_weekday(self, obj):
        # Преобразование даты в день недели:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if obj.deadline:
            return days[obj.deadline.weekday()]  # .weekday() → 0=Monday ... 6=Sunday
        return None


# _____ 5. ДОПОЛНИТЕЛЬНО  -->  5.2.2. Подключение Swagger и ReDoc  -->  Примечания
# from rest_framework import serializers
#
# class TaskStatisticsSerializer(serializers.Serializer):
#     total_tasks = serializers.IntegerField()
#     completed_tasks = serializers.IntegerField()


# ///////   home_work_07.md    /////////

# _____ 1.2. SubTaskCreateSerializer

class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'           # ['id', 'title', 'description', 'status', 'deadline']
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
        return super().update()


# _____ 3. Использование вложенных сериализаторов

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        # fields = '__all__'
        # fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at', 'task']
        fields = ['id', 'title', 'status', 'deadline']


    # Сериализатор, который использует только названия подзадач:
class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)     # , source='subtasks'

    # ____  Для к "home_work_08.md"  ____
    weekday = serializers.SerializerMethodField()

    class Meta:
        model = Task

        # ДОПОЛНИТЕЛЬНО к "home_work_07.md":
        # fields = ['id', 'title', 'description', 'status', 'deadline', 'subtasks']
        # fields = '__all__'

        # Для к "home_work_08.md":
        fields = ['id', 'title', 'description', 'status', 'deadline', 'weekday', 'created_at', 'subtasks']

    # Для к "home_work_08.md":
    def get_weekday(self, obj):
        # Преобразование даты в день недели:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if obj.deadline:
            return days[obj.deadline.weekday()]  # .weekday() → 0=Monday ... 6=Sunday
        return None


# _____ 4. Валидация данных в сериализаторах

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

        def validate_deadline(self, value):
            if value < date.today():
                raise ValidationError("Deadline can't be in the past.")
            return value


