from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def welcome_to_the_app(request):                                      # __ NB! __   hello_django.
    return HttpResponse("<h1>Welcome to the Task Manager!</h1>")


    # ///////   home_work_04.md    /////////

from datetime import timedelta, date
from hw_02_task_manager.models import Task, SubTask

def test(request):

    # ____ 1. Создание записи:  Task:
    #   - title: "Prepare presentation".
    #   - description: "Prepare materials and slides for the presentation".
    #   - status: "New".
    #   - deadline: Today's date + 3 days.

    # new_task = Task.objects.create(title='Prepare presentation',
    #                                description='Presentation about Python und AI',
    #                                status='New',
    #                                deadline=date.today() + timedelta(days=3),
    #                                )
    # new_task.save()  # СОХРАНИТЬ новое задание


    # ____ 2. Создание записи:  SubTasks  для "Prepare presentation":
    #   - title: "Gather information".
    #   - description: "Find necessary information for the presentation".
    #   - status: "New".
    #   - deadline: Today's date + 2 days.
    # # Получаю дату дедлайна для задачи "Prepare presentation":
    # task_deadline = Task.objects.get(title="Prepare presentation")
    # # print(task_deadline.deadline)
    # # Получаем задачу по названию. Причем, если в базе усть несколько задач с одинаковым названием,
    # # то лучше использовать .filter(title=...).first() вместо .get(...),
    # # чтобы избежать DoesNotExist или MultipleObjectsReturned:
    # task = Task.objects.filter(title="Prepare presentation", deadline=task_deadline.deadline).first()
    # SubTask.objects.create(title="Gather information", description="Find necessary information for the presentation", status='New', deadline=date.today() + timedelta(days=2), task=task,)
    # # new_subtask.save()  # можно не писать new_subtask.save() после .create() —
    #                     # потому что .create() уже сохраняет объект.


    # ____ 3. Создание записи:  SubTasks  для "Prepare presentation":
    #     - title: "Create slides".
    #     - description: "Create presentation slides".
    #     - status: "New".
    #     - deadline: Today's date + 1 day
    # SubTask.objects.create(title="Create slides", description="Create presentation slides",
    #                        status='New', deadline=date.today() + timedelta(days=1), task=task, )


    # ____ 4. Чтение записей:  Tasks со статусом "New": Вывести все задачи, у которых статус "New":
    # tasks_new = Task.objects.filter(status="New").all()
    # for task in tasks_new:
    #     print(f'\t\033[34m{task}\033[0m')

    # ____ 5. Чтение записей:  SubTasks с просроченным статусом "Done": Вывести все подзадачи,
    # у которых статус "Done", но срок выполнения истек:
    # subtask_done_overdue = SubTask.objects.filter(status="Done", deadline__lt=date.today())
    # for s_task in subtask_done_overdue:
    #     print(f'\t\033[33m{s_task.title}\033[0m with Deadline {s_task.deadline}.')

    # ____ 6. Изменение записей:  Измените статус "Prepare presentation" на "In progress":
    # Task.objects.filter(title="Prepare presentation").update(status="In progress")
    # task_status_change = Task.objects.filter(title="Prepare presentation")
    # for task in task_status_change:
    #     print(f'\tFor task \033[32m{task.title}\033[0m the New Status is \033[33m{task.status}\033[0m.')

    # ____ 7. Изменение записей:  Измените срок выполнения для "Gather information" на два дня назад:
    print(f'\033[40;33m{'':=<70}\033[0m')
    # SubTask.objects.filter(title="Gather information").update(deadline=date.today() - timedelta(days=2))
    # task_deadline_change = SubTask.objects.filter(title="Gather information")
    # for s_task in task_deadline_change:
    #     print(f"\tFor the SubTask \033[32m'{s_task.title}'\033[0m New Deadline is \033[33m{s_task.deadline}\033[0m.")

    # ____ 8. Изменение записей:  Измените описание для "Create slides" на "Create and format presentation slides":
    # SubTask.objects.filter(title="Create slides").update(description="Create and format presentation slides")
    # subtask_descript_change = SubTask.objects.filter(title="Create slides")
    # for s_task in subtask_descript_change:
    #     print(f"\tFor the SubTask \033[32m'{s_task.title}'\033[0m New Description is \033[33m{s_task.description}\033[0m.")

    # ____ 8. Удаление записей:  Удалите задачу "Prepare presentation" и все ее подзадачи:
    print(f'\033[40;33m{'':=<70}\033[0m')
    task_delete = Task.objects.get(title="Prepare presentation")
    task_delete.delete()
    tasks_after_del = Task.objects.all()
    for task in tasks_after_del:
        print(f'\t\033[34m{task.title}\033[0m.')


    return HttpResponse("<h1>Test Request to hw_04 to app 'hw_02_task_manager'.</h1>")



    # ///////   home_work_06.md    /////////

# _____ 1.2.2. Представление для создания задачи

from .models import Task
from rest_framework import generics
from .serializers import TaskSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# _____ 2. Эндпоинты для  -->  2.1. Список всех задач (GET /hw_02_task_manager/tasks/)

from rest_framework.generics import ListAPIView

class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# _____ 2. Эндпоинты для  -->  2.2. Получение задачи по ID (`GET /hw_02_task_manager/tasks/<int:pk>/`)

from rest_framework.generics import RetrieveAPIView

class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# _____ 3. Агрегирующий эндпоинт для статистики задач  -->  3.1. View для статистики

from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

class TaskStatisticsView(APIView):
    def get(self, request):
        total_tasks = Task.objects.count()
        new_tasks = Task.objects.filter(status='New').count()
        in_progress_tasks = Task.objects.filter(status='In Progress').count()
        done_tasks = Task.objects.filter(status='Done').count()
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now(), status__in=['New', 'In Progress']).count()

        return Response({
            "total": total_tasks,
            "new": new_tasks,
            "in_progress": in_progress_tasks,
            "done": done_tasks,
            "overdue": overdue_tasks
        })

# _____ 5. ДОПОЛНИТЕЛЬНО  -->  5.2.2. Подключение Swagger и ReDoc  -->  Примечания
# from rest_framework.generics import GenericAPIView
# from .serializers import TaskStatisticsSerializer  # нужно создать этот сериализатор
#
# class TaskStatisticsView(GenericAPIView):
#     serializer_class = TaskStatisticsSerializer
#
#     def get(self, request):
#         data = {
#             "total_tasks": 10,
#             "completed_tasks": 3,
#         }
#         return Response(data)

