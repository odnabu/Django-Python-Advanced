# hw_02_task_manager/urls.py

from django.urls import path
# _____ Импортирование ВСЕХ классов представлений из файла hw_02_task_manager / views.py:
from . import views


# urlpatterns = [
#     path('home/', views.welcome_to_the_app, name='welcome_to_the_app'),  # __ NB! __  'hw_02/'  and  welcome_to_the_app.
# ]


#       ///////   home_work_06.md    /////////

# _____ 1.2.3 Маршрут (URL) для обращения к представлению
from .views import TaskCreateView

# urlpatterns = [
#     path('admin/', view=test), # http://127.0.0.1:8000/admin/
#     path('home/', views.welcome_to_the_app, name='welcome_to_the_app'),  # __ NB! __  'hw_02/'  and  welcome_to_the_app: http://127.0.0.1:8000/hw-02/home/
#     path('tasks/create/', TaskCreateView.as_view(), name='task-create'), # __ NB! __  'hw_06': http://127.0.0.1:8000/hw-02/tasks/create/
# ]


# _____ 2. Эндпоинты для  -->  2.3. Подключение маршрутов
from .views import TaskListView, TaskDetailView

urlpatterns = [
    # path('admin/', view=test), # http://127.0.0.1:8000/admin/
    path('home/', views.welcome_to_the_app, name='welcome_to_the_app'),     # __ NB! __  'hw_02/'  and  welcome_to_the_app: http://127.0.0.1:8000/hw-02/home/
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),    # __ NB! __  'hw_06': http://127.0.0.1:8000/hw-02/tasks/create/
    path('tasks/', TaskListView.as_view(), name='task-list'),               # __ NB! __  'hw_06': http://127.0.0.1:8000/hw-02/tasks/
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # __ NB! __  'hw_06': http://127.0.0.1:8000/hw-02/tasks/8/
]

# _____ 3. Агрегирующий эндпоинт для статистики задач  -->  3.2. Добавление маршрута
from .views import TaskStatisticsView

urlpatterns += [
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),      # __ NB! __  'hw_06':
                                                                                  #
]


# _____ 5. ДОПОЛНИТЕЛЬНО  -->  5.2.2. Подключение Swagger и ReDoc
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns += [
    # Схема OpenAPI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]



#       ///////   home_work_07.md    /////////

# _____ 5.3. Маршруты в файле urls.py:
from .views import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns += [
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(),
         name='subtask-detail-update-delete'),
]
