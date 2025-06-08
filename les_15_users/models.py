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

    age = models.IntegerField()
    rating = models.FloatField(default=0.0)
    country = models.CharField(choices=countries, default='DE', help_text='Where are you born?')




