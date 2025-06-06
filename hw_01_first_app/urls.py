from django.urls import path
from . import views

urlpatterns = [
    path('home/<str:name>/', views.hello_user, name='home'),
    path('hw-01/', views.hello_django_app, name='hello_django'),
]

