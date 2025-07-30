# hw_02_task_manager/urls.py

# from django.contrib import admin      # ЗДЕСЬ admin уже НЕ нужен, т.к. прописан глобально для всего проекта в config.
from django.urls import path, include
# _____ Импортирование ВСЕХ классов представлений из файла hw_02_task_manager / views.py:
# from . import views
# from hw_02_task_manager.views import welcome_to_the_app
from hw_02_task_manager.views import WelcomeToTheAppView
# --------------------------------------------------------------------------
#       ///////   home_work_10.md    /////////
from rest_framework.routers import DefaultRouter
from hw_02_task_manager.views import CategoryViewSet

# Создаем экземпляр роутера:
router = DefaultRouter()
# Регистрируем ViewSet.
#   'category' - это префикс URL, по которому будут доступны наши категории.
#   CategoryViewSet - представление, которое будет обрабатывать запросы.
router.register(r'categories', CategoryViewSet)     # , basename='category' - похоже, что это тут НЕ нужно.
# --------------------------------------------------------------------------


#       ///////   home_work_06.md    /////////
# _____ hw_06:  1.2.3 Маршрут (URL) для обращения к представлению
# _____ hw_06:  2. Эндпоинты для  -->  2.3. Подключение маршрутов
from hw_02_task_manager.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    # _____ hw_10:  маршрут для routers:
    path('', include(router.urls)),
    # -------------------------------------

    # path('for-admin/', AdminView.as_view(), name='admin-data’),   # 23.07.2025 Les 33  -  http://127.0.0.1:8000/admin/
    # path('admin/', view=test), # http://127.0.0.1:8000/admin/
    # path('admin/', admin.site.urls), # - Маршрут 'admin/' обрабатывается встроенным админ-интерфейсом Django.
    # path('home/', welcome_to_the_app, name='welcome_to_the_app'),       # hw_02/  and  welcome_to_the_app: http://127.0.0.1:8000/hw-02/home/
    path('home/', WelcomeToTheAppView.welcome_to_the_app, name='welcome_to_the_app'),       # hw_02/  and  welcome_to_the_app: http://127.0.0.1:8000/hw-02/home/
    path('tasks/create/', TaskListCreateView.as_view(), name='task-create'),  # hw_06: http://127.0.0.1:8000/hw-02/tasks/create/
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),           # hw_06: http://127.0.0.1:8000/hw-02/tasks/

    # ВСЕ ДИНАМИЧЕСКИЕ ссылки tasks/<int:pk>/, которые содержат <int:pk>, ЛУЧШЕ размещать ПОСЛЕ эндпоинта tasks.
    # Смотри код ниже для hw_08:  1.2. URL-маршрут.
    # path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),    # hw_06: http://127.0.0.1:8000/hw-02/tasks/8/
    #                                                                                 # hw_06: http://127.0.0.1:8000/hw-02/tasks/7/?subtask_titles=true
]

# _____ hw_06:  3. Агрегирующий эндпоинт для статистики задач  -->  3.2. Добавление маршрута
from hw_02_task_manager.views import TaskStatisticsView

urlpatterns += [
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),      # hw_06: http://127.0.0.1:8000/hw-02/tasks/statistics/
]

# _____ hw_06:  5. ДОПОЛНИТЕЛЬНО  -->  5.2.2. Подключение Swagger и ReDoc
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns += [
    # Схема OpenAPI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),     # hw_06: http://127.0.0.1:8000/hw-02/swagger/
    # Redoc UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),              # hw_06: http://127.0.0.1:8000/hw-02/redoc/
]



#       ///////   home_work_07.md    /////////
# _____ hw_07:  5.3. Маршруты в файле urls.py:
from hw_02_task_manager.views import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns += [
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),      # hw_07: http://127.0.0.1:8000/hw-02/subtasks/
                                                                                               # hw_08: http://127.0.0.1:8000/hw-02/subtasks/?page=1
                                                                                               # hw_08: http://127.0.0.1:8000/hw-02/subtasks/?page=2&page_size=3
                                                                                               # hw_08: http://127.0.0.1:8000/hw-02/subtasks/?task__title=Homework
                                                                                               # hw_08: http://127.0.0.1:8000/hw-02/subtasks/?status=done
                                                                                               # hw_08: http://127.0.0.1:8000/hw-02/subtasks/?task_title=Creating&status=in%20progress
                                                                                               # hw_09: http://127.0.0.1:8000/hw-02/subtasks/?status=Done
                                                                                               # hw_09: http://127.0.0.1:8000/hw-02/subtasks/?search=Creating
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(),                  # hw_07: http://127.0.0.1:8000/hw-02/subtasks/8/
         name='subtask-detail-update-delete'),
]



#       ///////   home_work_08.md    /////////
# _____ hw_08:  1.2. URL-маршрут
from hw_02_task_manager.views import TaskByWeekdayView

urlpatterns += [
    path('tasks/by-day/', TaskByWeekdayView.as_view(), name='tasks-by-day'),            # hw_08: http://127.0.0.1:8000/hw-02/tasks/by-day/
                                                                                              # hw_08: http://127.0.0.1:8000/hw-02/tasks/by-day/?day=monday
    # ВСЕ ДИНАМИЧЕСКИЕ ссылки tasks/<int:pk>/, которые содержат <int:pk>, ЛУЧШЕ размещать после эндпоинта tasks.
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),              # hw_06: http://127.0.0.1:8000/hw-02/tasks/8/
                                                                                              # hw_06: http://127.0.0.1:8000/hw-02/tasks/7/?subtask_titles=true
]


# %%%%%%%%%%%%%%%%%%%%%%%       LESSONS 33 and 34 to Authentication     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 23.07.2025 - Python Adv 33: Введение в аутентификацию и авторизацию.
# части кода с урока по app "library" - в УЧЕБНЫХ целях.
from hw_02_task_manager.views import (ProtectedDataView,
                                      PublicView,
                                      AdminView)
# Связывание представления с url:
urlpatterns += [
    path('protected/', ProtectedDataView.as_view(), name='protected-data'),     # les_33: http://127.0.0.1:8000/hw-02/protected/
    # 23.07.2025 - Python Adv 34: Практикум 9,  1:13:00:  PERMISSIONS.
    path('public/', PublicView.as_view(), name='public-data'),                  # les_34:  http://127.0.0.1:8000/hw-02/public/
    # 23.07.2025 - Python Adv 34: Практикум 9, 1:15:40.
    # Пермишен ниже позволяет Админу получить доступ к представлению AdminView, но НЕ позволяет
    # # обычному пользователю получить доступ.
    path('admin/', AdminView.as_view(), name='admin'),
]

# ---------------------------------------------------------------------------------------------------------------


#       ///////   home_work_12.md    /////////
# _____ hw_12:  2. Реализация пермишенов для API.
# Здесь url добавлять НЕ нужно, т.к. по условию ДЗ нужно прописать СТАНДАРТНЫЕ из DRF - DjangoModelPermissions.



