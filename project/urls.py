from project.views import test
from django.urls import path


urlpatterns = [
    path('test-proj', view = test),
]

