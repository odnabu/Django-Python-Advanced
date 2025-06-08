from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome_to_the_app(request):                                      # __ NB! __   hello_django.
    return HttpResponse("<h1>Welcome to the Task Manager!</h1>")
