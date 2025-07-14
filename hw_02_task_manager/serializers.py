# HW_06
#

from rest_framework import serializers
from .models import Task


# ///////   home_work_06.md    /////////

# _____ 1.2.1 Создание сериализатора для модели `Task`

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline']


# _____ 5. ДОПОЛНИТЕЛЬНО  -->  5.2.2. Подключение Swagger и ReDoc  -->  Примечания
# from rest_framework import serializers
#
# class TaskStatisticsSerializer(serializers.Serializer):
#     total_tasks = serializers.IntegerField()
#     completed_tasks = serializers.IntegerField()
