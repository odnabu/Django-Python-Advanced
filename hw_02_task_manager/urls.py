from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.welcome_to_the_app, name='welcome_to_the_app'),  # __ NB! __  'hw_02/'  and  welcome_to_the_app.
]
