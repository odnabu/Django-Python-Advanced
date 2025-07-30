# *****  home_work_02-08  *************************
#   Импорты библиотек и методов:
# from datetime import datetime
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination

# *****  home_work_09  *****************************
#    Импорты библиотек и методов:
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
#    Импорты из фалов приложения:
from hw_02_task_manager.models import Task, SubTask
from hw_02_task_manager.serializers import TaskSerializer, TaskDetailSerializer, SubTaskCreateSerializer

# *****  home_work_10  *****************************
#    Импорты библиотек и методов:
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.db.models import Count
#    Импорты из фалов приложения:
from hw_02_task_manager.models import Category
from hw_02_task_manager.serializers import CategorySerializer

# *****  home_work_12  *****************************
from hw_02_task_manager.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (DjangoModelPermissions,
                                        AllowAny, IsAuthenticated, IsAdminUser,
                                        IsAuthenticatedOrReadOnly,      # Кастомный Пермишен для ДЗ 19.
                                        )



# %%%%%%%%%%%%%%%%%%%%%%%       LESSONS 33 and 34 to Authentication     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Все что ниже ДО домашек - части кода с урока по app "library" - т.е. в УЧЕБНЫХ целях.
# 23.07.2025 - Python Adv 33: Введение в аутентификацию и авторизацию


# 23.07.2025 - Python Adv 34: Практикум 9, 1:15:40.
class PublicView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK, data={'message': 'This endpoint have access for anyone!'})



# 23.07.2025 - Python Adv 34: Практикум 9, 1:15:40.
class ReadOnlyOrAuthenticatedView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({"message": "This is readable by anyone, but modifiable only by authenticated users."})

    def post(self, request):
        # Этот метод будет доступен только аутентифицированным пользователям.
        return Response({"message": "Data created by authenticated user!"})


# 23.07.2025 - Python Adv 34: Практикум 9, 1:15:40.
# Пермишен ниже позволяет Админу получить доступ к представлению AdminView, но НЕ позволяет
# обычному пользователю получить доступ.
class AdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "Hello, Admin!"})


# 23.07.2025 - Python Adv 33: Введение в аутентификацию и авторизацию, 2:44:40.
class ProtectedDataView(APIView):
    # Указываем, какие классы аутентификации использовать для этого представления.
    # Здесь мы явно переопределяем или подтверждаем BasicAuthentication.
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [TokenAuthentication]

    # Если JWTAuthentication установлен как DEFAULT_AUTHENTICATION_CLASSES,
    # здесь можно просто указать разрешения. DRF сам проверит токен.

    # Указываем, какие классы разрешений использовать.
    # IsAuthenticated означает, что только аутентифицированные пользователи имеют доступ.
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Если запрос дошел сюда, значит, пользователь аутентифицирован и авторизован.
        # request.user теперь содержит объект пользователя.
        return Response({"message": f"Hello, authenticated user {request.user.username}!", "user": request.user.username})

# --------------------------------------------------------------------------------------------------------------




# //////////////      home_work_12    Задание 2: Реализация пермишенов для API      //////////////////////////////

# ____  hw_12   Задание 2: Реализация пермишенов для API:
# https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/views.py








# //////////////      home_work_09    Задание 1: Generic Views для задач (Task)       //////////////////////////////

# Класс для создания задач и для получения списка задач:
# Этот класс заменяет прежние TaskCreateView и TaskListView в старой версии файла с Представлениями x_old_views.py.
# Теперь он наследуется от ListCreateAPIView, который уже умеет:
#   - обрабатывать GET для получения списка (List).
#   - обрабатывать POST для создания объекта (Create).
class TaskListCreateView(ListCreateAPIView):
    """
    Cоздание задачи и получение списка задач.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Подключение бэкендов для фильтрации, поиска и сортировки:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Поля, по которым можно будет точно фильтровать (status=...):
    filterset_fields = ['status', 'deadline']
    # Поля, по которым будет работать полнотекстовый поиск (search=...):
    search_fields = ['title', 'description']
    # Поля, по которым можно будет сортировать (ordering=...):
    ordering_fields = ['created_at']
    # СДЕЛАТЬ переопределение метода filterset_fields: кастомное преобразование даты.

    # _____ home_work_12:  2:  Добавление пермишенов:
    permission_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        # При сохранении объекта передается дополнительный параметр owner,
        # в который записывается текущий пользователь из запроса:
        serializer.save(owner=self.request.user)

    # # Переопределение метода create:
    # def create(self, request, *args, **kwargs):
    #     # Копирование данных из запроса, чтобы их можно было изменять:
    #     data = request.data.copy()
    #
    #     # ----------------------------------------------------------------------
    #     # Кастомная логика:             ???????? Что СЮДА вписывать вместо 'author' -- title ?????????
    #     if 'author' not in data or not data['author']:
    #         data['author'] = 1
    #
    #     # Дальше идет стандартная логика из DRF:
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     # self.perform_create вызывает serializer.save():
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



# Класс для получения/обновления/удаления задачи:
class TaskDetailView(RetrieveUpdateDestroyAPIView):
    """
    Получение, обновление и удаление задачи.
    """
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer

    # _____ home_work_12:  2:  Добавление пермишенов:
    permission_classes = [IsAdminUser]



# //////////////     home_work_09   Задание 2: Generic Views для подзадач (SubTask)       //////////////////////////////

# _____ home_work_08: 2. Пагинация в отображении списка подзадач:
class SubTaskPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class SubTaskListCreateView(ListCreateAPIView, PageNumberPagination):
    """
    Список подзадач и их создание.
    """
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

    # Подключение пагинатора со своими настройками:
    pagination_class = SubTaskPagination

    # Подключение бэкендов для фильтрации, поиска и сортировки:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Поля, по которым можно будет точно фильтровать (status=...):
    filterset_fields = ['status', 'deadline']
    # Поля, по которым будет работать полнотекстовый поиск (search=...):
    search_fields = ['title', 'description', 'task__title']
    # Поля, по которым можно будет сортировать (ordering=...):
    ordering_fields = ['created_at']

    # _____ home_work_12:  2:  Добавление пермишенов:
    permission_classes = [IsAuthenticatedOrReadOnly]


# Подробности, обновление и удаление подзадачи:
class SubTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Получение подробной информации, обновление и удаление подзадачи.
    """
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

    # _____ home_work_12:  2:  Добавление пермишенов:
    permission_classes = [IsAdminUser]


# //////////////     home_work_09   ПРЕДСТАВЛЕНИЯ из предыдущей версии views.py       //////////////////////////////

# _____ hw_02:   Домашняя страница с приветствием:

class WelcomeToTheAppView(APIView):
    def welcome_to_the_app(request):      #  hello_django.
        """
        Домашняя страница с приветствием в приложении по адресу http://127.0.0.1:8000/hw-02/home/.
        """
        return HttpResponse("<h1>Welcome to the Task Manager!</h1>")

    # _____ home_work_12:  2:  Добавление пермишенов:
    permission_classes = [AllowAny]



# _____ hw_06:  3. Агрегирующий эндпоинт для статистики задач  -->  3.1. View для статистики
class TaskStatisticsView(APIView):
    """
    Статистика задач.
    """

    # _____ home_work_12:  2:  Добавление пермишенов:
    permission_classes = [IsAuthenticated]
    # По умолчанию УЖЕ назначен IsAuthenticated в настройках проекта. НО, все равно нужно ПРОПИСЫВАТЬ настройки.

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


# _____ hw_08:  1. Эндпоинт на получение списка всех задач по дню недели
class TaskByWeekdayView(APIView):
    """
    Получение списка всех задач по дню недели.
    """

    # _____ home_work_12:  2:  Добавление пермишенов:
    permission_classes = [IsAuthenticated]
    # По умолчанию УЖЕ назначен IsAuthenticated в настройках проекта. НО, все равно нужно ПРОПИСЫВАТЬ настройки.


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

            if not day_param:
                tasks = Task.objects.all()
            elif day_param not in day_name_to_number:
                return Response({f"\033[90;31mERROR\033[0m": "Not valid weekday name."}, status=400)
            else:
                weekday_number = day_name_to_number[day_param]
                # Фильтрация по дню недели:
                tasks = Task.objects.filter(deadline__week_day=weekday_number + 2)
                # +2 — потому что в Django 1=sunday, 2=monday... 7=saturday

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)



# //////////////   home_work_10   Задание 1. CRUD для категорий с использованием ModelViewSet     ////////////////////

# _____ hw_10:  1. Создайте `CategoryViewSet`, используя `ModelViewSet` для CRUD операций.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Это представление предоставляет полный набор действий CRUD для модели Category.
    ---
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # _____ home_work_12:  2:  Добавление пермишенов:
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Мягкое удаление:
    def perform_destroy(self, instance):
        instance.delete()

    # Новый кастомный метод:
    @action(detail=False, methods=['get'])
    def count_tasks(self, request):
        """
        Возвращает количество задач для каждой категории.
        """
        # С помощью annotate добавляем к каждой категории поле task_count:
        category_with_tasks_count = Category.objects.annotate(task_count=Count('tasks'))
        # print(f"\033[31m{category_with_tasks_count}\033[0m")

        # Формируем данные для ответа:
        data = [
            {
                "id": item.id,
                "category": item.name,
                "task_count": item.task_count,
            }
            for item in category_with_tasks_count
        ]
        return Response(data)
        # return Response(category_with_tasks_count)


