from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.i18n import language
from django.db.models.functions import Concat
from django.db.models import F, Value

from project.models import Project

# Create your views (ENDPOINTS) here.

def test(req):
    # ____ ДОБАВЛЕНИЕ НОВОГО проекта:
    # new_project = Project.objects.create(name='New_Project', language='c++')    # тут c++ - с МАЛЕНЬКОЙ буквы.
    # new_project.save()  # СОХРАНИТЬ новый проект

    # ____ УДАЛЕНИЕ ненужного объекта:
    # del_projects = Project.objects.filter(id__gte=6)
    # del_projects.delete()

    # ____ Можно СРАЗУ вызвать Project и СОЗДАТЬ ЭКЗЕМПЛЯР класса:
    # Project.objects.create(name='5th Project', description='This is a description', language='Python')

    # ____ МАССОВОЕ Добавление проектов в БД:
    # project_1 = Project(name='ABC', description='hohoh', language='c')
    # project_2 = Project(name='xyz', description='Coordinates', language='py')
    # project_3 = Project(name='Beautiful Day', language='java')
    # projects = [project_1, project_2, project_3]
    # Project.objects.bulk_create(projects)

    # ____ МАССОВОЕ Обновление поля (language) для ВСЕХ проектов в БД:
    # data_projects = Project.objects.all()
    # for project in data_projects:
    #     # if project.language == 'py':
    #     #     project.language = 'java'
    #     project.language='py'
    # Project.objects.bulk_update(data_projects, ['language'])

    # ____ Обновление имен проектов с добавлением к имени языка, на котором он разрабатывается.
    # Project.objects.update(name=F('name') + F('language'))
    # Project.objects.update(name=Concat(F('name'), Value(' '), F('language')))


    return HttpResponse("You are here!")        # Нужно чтобы HttpResponse возвращался обязательно!



