# Video 13, 3:20:40 - 1-st Lecture to Django (Intro). link: https://player.vimeo.com/video/1089675502?h=23260e4621

from les_01_begins.views import hello
from django.urls import path

urlpatterns = [path("hello", view=hello, name="hello")]

