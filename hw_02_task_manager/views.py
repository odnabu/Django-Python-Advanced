from django.shortcuts import render
from django.http import HttpResponse

# _____  Для home_work_06.md:  _____
# from hw_02_task_manager.models import Task        # See home_work_04
from rest_framework import generics
from hw_02_task_manager.serializers import TaskSerializer, SubTaskSerializer, TaskDetailSerializer
# _____  Для home_work_07.md:  _____
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from hw_02_task_manager.models import SubTask        # See home_work_04
from hw_02_task_manager.serializers import SubTaskCreateSerializer
from django.shortcuts import get_object_or_404
# _____  Для home_work_08.md:  _____
# from hw_02_task_manager.models import Task, SubTask        # See home_work_04
from rest_framework.pagination import PageNumberPagination
# from hw_02_task_manager.serializers import TaskSerializer    # See home_work_06
import datetime
from rest_framework.request import Request





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

class TaskCreateView(generics.CreateAPIView):
    """
    Создание задачи.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# _____ 2. Эндпоинты для  -->  2.1. Список всех задач (GET /hw_02_task_manager/tasks/)

from rest_framework.generics import ListAPIView

class TaskListView(ListAPIView):
    """
    Список всех задач.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# _____ 2. Эндпоинты для  -->  2.2. Получение задачи по ID (`GET /hw_02_task_manager/tasks/<int:pk>/`)

from rest_framework.generics import RetrieveAPIView

class TaskDetailView(RetrieveAPIView):
    """
    Получение детальной информации о задаче по ID.
    """
    queryset = Task.objects.all()

    # ДОПОЛНИТЕЛЬНО к "home_work_07.md":
    # Добавление возможности переключения сериализаторов в зависимости от параметра ?subtask_titles=true.
    # Сначала закомментировать строку ниже:
    # serializer_class = TaskSerializer
    # Затем обновить TaskDetailView, чтобы сериализатор выбирался по параметру:
    def get_serializer_class(self):
        subtask_title = self.request.query_params.get('subtask_titles')
        if subtask_title and subtask_title.lower() in ['1', 'true', 'yes']:
            return TaskDetailSerializer
        return TaskSerializer




# _____ 3. Агрегирующий эндпоинт для статистики задач  -->  3.1. View для статистики

from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

class TaskStatisticsView(APIView):
    """
    Статистика задач.
    """

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



    # ///////   home_work_07.md    /////////

# _____ 5.1. Представление для создания и получения списка подзадач:

# _____ home_work_08: 2. Пагинация в отображении списка подзадач:
class SubTaskPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class SubTaskListCreateView(APIView, PageNumberPagination):
    """
    home_work_08:
        - Пагинация в отображении списка подзадач.
        - Отображение и создание подзадач с возможностью фильтрации по названию задачи и статусу.
    """
    # serializer = SubTaskCreateSerializer(subtasks, many=True)
    # return Response(serializer.data)

    pagination_class = SubTaskPagination

    # Получение СПИСКА подзадач
    # +++
    # _____ home_work_08: 2. Пагинация в отображении списка подзадач:
    def get(self, request):
        subtasks = SubTask.objects.all().order_by('-created_at')     # Сортировка по убыванию даты создания.

        # Получение query-параметров:
        task_title = request.query_params.get('task_title')
        status_filter = request.query_params.get('status')

        # Фильтрация по названию главной задачи:
        if task_title:
            subtasks = subtasks.filter(task__title__icontains=task_title)

        # Фильтрация по статусу подзадачи:
        if status_filter:
            subtasks = subtasks.filter(status__iexact=status_filter)

        # Пагинация:
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(subtasks, request)

        # Краткая информация о подзадаче из сериализатора SubTaskSerializer для отображения в СПИСКЕ подзадач:
        serializer = SubTaskSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    # ____________________________________________________

    # Создание СПИСКА подзадач:
    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# _____ 5.2. Класс представлений для получения, обновления и удаления подзадач:

class SubTaskDetailUpdateDeleteView(APIView):
    """
    Получение, обновление и удаление подзадач.
    """

    # Указание ID (является PRIMARY_KEY - pk) подзадачи в БД для дальнейшего вызова его в методах:
    def get_object(self, pk):
        return get_object_or_404(SubTask, pk=pk)

    # Получение ОДНОЙ подзадачи по ID и вывод в браузере:
    def get(self, request, pk):
        subtask = self.get_object(pk)
        serializer = SubTaskCreateSerializer(subtask)
        return Response(serializer.data)

    # Обновление ОДНОЙ подзадачи по ID и вывод в браузере:
    def put(self, request, pk):
        subtask = self.get_object(pk)
        serializer = SubTaskCreateSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Удаление ОДНОЙ подзадачи по ID и вывод в браузере:
    def delete(self, request, pk):
        subtask = self.get_object(pk)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    # ///////   home_work_08.md    /////////

# _____ 1. Эндпоинт на получение списка всех задач по дню недели

class TaskByWeekdayView(APIView):
    """
    Получение списка всех задач по дню недели.
    """

    def get(self, request):
        day_param = request.query_params.get('day', '').strip().lower()

        # Если никакой параметр запроса не передавался - по умолчанию выводить все записи:
        if not day_param:
            tasks = Task.objects.all()
        else:
            # Сопоставление английских дней недели с номерами (monday = 0, sunday = 6)
            day_name_to_number = {
                'monday': 0,
                'tuesday': 1,
                'wednesday': 2,
                'thursday': 3,
                'friday': 4,
                'saturday': 5,
                'sunday': 6,
            }

            if day_param not in day_name_to_number:
                return Response({f"\033[90;31mERROR\033[0m": "Not valid weekday name."}, status=400)

            weekday_number = day_name_to_number[day_param]

            # Фильтрация по дню недели:
            tasks = Task.objects.filter(deadline__week_day=weekday_number + 2)
            # +1 — потому что в Django 1=sunday, 2=monday... 7=saturday

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)



