# from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def hello_user(request, name):
    return HttpResponse(f"<h1>{name}, Welcome to the my 1-st Application.</h1>")


def hello_django_app(request):
    return HttpResponse("<h1>1-st Home Work 1 with Application on Django.</h1>")




