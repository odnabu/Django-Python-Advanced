from les_01_begins.views import hello
from django.urls import path

urlpatterns = [path("hello", view=hello, name="hello")]

