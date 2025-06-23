from django.core.validators import MinValueValidator, MaxValueValidator    # Список валидаторов: https://django.fun/docs/django/5.0/ref/validators/
from django.db import models

# Create your models here.

class User(models.Model):

    countries = [
        ('PT', 'Portugal'),
        ('ES', 'Spain'),
        ('MV', 'Maldives'),
        ('DE', 'Germany'),
    ]

    # id = models.BigAutoField(verbose_name='id_user', primary_key=True)    # НО так лучше НЕ делать, пока учишься!.

    first_name = models.CharField(max_length=50, null=True, blank=True)
    #       null - в БД без значений.
    #       blank - в ФОРМАХ без значений.
    # После изменений в МОДЕЛИ:
    #   - python manage.py makemigrations.
    #   - python manage.py migrate.

    last_name = models.CharField(max_length=70, verbose_name='Family name')
    # verbose_name - то что будет ОТОБРАЖАТЬСЯ вместо Last Name.

    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(140)])
    rating = models.FloatField(default=0.0)
    country = models.CharField(choices=countries, default='DE', help_text='Where are you born?')



class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')     # O2O - One-to-One.
    married = models.BooleanField()     # O2O - One-to-One.


# ______  ANOTHER  MODELS only for Demonstration  _________________________________________________________
# class Actor(models.Model):
#     name = models.CharField(max_length=50)
#
# class Movie(models.Model):
#     title = models.CharField(max_length=60)
#     actors = models.ManyToManyField(Actor, related_name='movies')


# ////////////////   TO   LESSON  from 23-06-25, See Video Video 20, 48:00    //////////////////////
class Actor(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=255)
    experience = models.IntegerField()
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=32)
    actors = models.ManyToManyField(Actor, related_name="movies")
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        if self.director:       # Если нет директора / режисера:
            return f'Director: {self.director.name}. Title: {self.title}'
        else:
            return f'Title: {self.title}'

