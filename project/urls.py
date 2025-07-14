# File urls.py

from project.views import test, list_project, list_task
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', view=test), # http://127.0.0.1:8000/admin/
    path('test', view=test), # http://127.0.0.1:8000/project/my_path
    path('projects', view=list_project), # http://127.0.0.1:8000/project/projects
    path('tasks', view=list_task), # http://127.0.0.1:8000/project/projects
    # path('project/admin/', view=test) ## http://127.0.0.1:8000/project/admin/
]

