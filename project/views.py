from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.i18n import language
from django.db.models.functions import Concat, ExtractWeekDay
from django.db.models import F, Value, Count, Avg
from rest_framework.response import Response

from project.models import Project, Task

from django.utils import timezone

from django.contrib.auth.models import User
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from project.serializers import ProjectListSerializer, TaskListSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views (ENDPOINTS) here.

def test(req):
    # ____ ДОБАВЛЕНИЕ НОВОГО проекта:
    # new_project = Project.objects.create(name='New_Project', language='c++')    # тут c++ - с МАЛЕНЬКОЙ буквы.
    # new_project.save()  # СОХРАНИТЬ новый проект

    # ____ УДАЛЕНИЕ ненужного объекта:
    # del_projects = Project.objects.filter(id__gte=6)
    # del_projects.delete()

    # ____ Можно СРАЗУ вызвать Project и СОЗДАТЬ ЭКЗЕМПЛЯР класса:
    # Project.objects.create(name='5th Project', description='This is a description', language='Python')

    # ____ МАССОВОЕ Добавление проектов в БД:
    # project_1 = Project(name='ABC', description='hohoh', language='c')
    # project_2 = Project(name='xyz', description='Coordinates', language='py')
    # project_3 = Project(name='Beautiful Day', language='java')
    # projects = [project_1, project_2, project_3]
    # Project.objects.bulk_create(projects)

    # ____ МАССОВОЕ Обновление поля (language) для ВСЕХ проектов в БД:
    # data_projects = Project.objects.all()
    # for project in data_projects:
    #     # if project.language == 'py':
    #     #     project.language = 'java'
    #     project.language='py'
    # Project.objects.bulk_update(data_projects, ['language'])

    # ____ Обновление имен проектов с добавлением к имени языка, на котором он разрабатывается.
    # Project.objects.update(name=F('name') + F('language'))
    # Project.objects.update(name=Concat(F('name'), Value(' '), F('language')))

    # ___ 26.06.25 Task 1: Получение всех проектов по дате, созданные до 25 Июня
    # projects = Project.objects.filter(created_at__lte="2025-06-25")
    # # projects = Project.objects.filter(created_at__gte="2025-06-25")
    # # print(projects)
    # for n, project in enumerate(projects):
    #     print(f"{n+1} - {project.name} and it wa created: {project.created_at}")
    # print(f"Number of Projects: {projects.count()}")

    # ___ 26.06.25 Task 2: Файлы проектов в день недели
    # annotated_projects = Project.objects.annotate(week_day=ExtractWeekDay('created_at'))
    # filtered_projects = annotated_projects.filter(week_day = 2)     # Все проекты, созданные в пятницу
    # for n, project in enumerate(filtered_projects, start=1):
    #     print(f"\t\033[31m{n}\033[m - {project.name}")

    # ___ 26.06.25 Task 3: Общее количество проектов
    # Модель -- способ вызова -- метод обработки данных
    # projects = Project.objects.all()
    # print(f"\tThe TOTAL number of projects is \033[31m{projects.count()}\033[m.")

    # ___ 26.06.25 Task 4: Количество ЗАДАЧ для каждого проекта
    # ___ 26.06.25 Task 5: Среднее количество задач на каждом проекте
    # projects = Project.objects.all()
    # for project in projects:
    #     task_count = project.tasks.aggregate(count=Count("id"), average_count=Avg(F("id")))
    #     print(f"\tProject {project.name}, number of Tasks: \033[31m{task_count['count']}\033[m, "
    #           f"Avg.number of Tasks: \033[34m{task_count['average_count']}\033[m")

    # ___ 26.06.25 Task 6: Количество задач для каждого Developer
    # annotated_devs = User.objects.annotate(task_count=Count('tasks__id')).values_list('username', 'task_count')
    # for user in annotated_devs:
    #     print(f"\tFor {user[0]} NUMBER of tasks is \033[31m{user[1]}\033[m")

    # ___ 26.06.25 Task 7: Сортировка задач по приоритету и дате выполнения
    # task = Task.objects.all().order_by('priority', 'due_date')
    # for task in task:
    #     print(f"\tTask title is {task.name} has priority \033[31m{task.priority}\033[m\n "
    #           f"and has deadline at: \033[31m{task.due_date}\033[m")

    # ___ 26.06.25 Task 8: Сортировка пользователей по количеству задач
    # annot_users = User.objects.all().annotate(tasks_number=Count('tasks__id'))
    # ordered_users = annot_users.order_by('-tasks_number').values_list('username', 'tasks_number')
    # for user in ordered_users:
    #     print(f"\tFor {user[0]} NUMBER of tasks is \033[31m{user[1]}\033[m")

    # ___ 26.06.25 Task 9: Пагинация для задач
    # all_tasks = Task.objects.all()
    # paginator = Paginator(all_tasks, 2)
    # tasks_per_page = paginator.get_page(1)
    # for task in tasks_per_page:
    #     print(f"{'':-<60}")
    #     print(f"\tTask - {task}, \033[35m{task.due_date}\033[m")


    return HttpResponse("You are here!")        # Нужно чтобы HttpResponse возвращался обязательно!


# ___ 26.06.25 Task 11: Первое представление для отображения списка всех проектов
@api_view(['GET'])
def list_project(request):
    projects = Project.objects.all()
    if projects.exists():
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Projects NOT found'}, status=status.HTTP_404_NOT_FOUND)


# ___ 26.06.25 Task 12: Сериализатор для модели задач (Task)
@api_view(['GET'])
def list_task(request):
    tasks = Task.objects.all()
    if tasks.exists():
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Tasks NOT found'}, status=status.HTTP_404_NOT_FOUND)




