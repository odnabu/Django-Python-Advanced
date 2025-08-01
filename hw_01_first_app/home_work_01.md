Вам необходимо самостоятельно создать Django проект и добавить его в Git.

---
## <span style="color: #008000">1. Создание проекта:</span>
- Создайте новый Python-проект в PyCharm.
- Установите фреймворк Django.
- Создайте структуру Django-проекта с помощью команды в консоли.

<span style="color: #606060">Сделано на уроке 2.06.2025.</span>  
Создание Django-проекта с именем <span style="color: #F00000">config</span> в созданном 
новом проекте Python:   
```
    django-admin startproject config        # __ NB! __ <project_name>  ==  config
```
Я свой назвала сначала <span style="background: #404040; padding: 5px">DjangoProject</span>, а потом переименовала в 
DjangoProject_config, что повлекло за собой много <span style="background: #800000; padding: 5px">ПРОБЛЕМ</span> 
с переименованием аргументов в разных файлах настроек Django-проекта.



---
## <span style="color: #008000">2. Настройка переменных окружения:</span>
- Создайте файл .env в корне проекта и добавьте переменные SECRET_KEY, DEBUG и ALLOWED_HOSTS.
- Установите библиотеку django-environ для работы с переменными окружения.
- Считайте переменные SECRET_KEY, DEBUG и ALLOWED_HOSTS из .env файла в settings.py.

<span style="color: #606060">См. видео урока от 2.06.2025  ▶  Video 13, 3:11:40 - 1-st Lecture to Django (Intro).  
link:</span> https://player.vimeo.com/video/1089675502?h=23260e4621  
+++   
<span style="color: #606060">файлы DjangoProject_config/settings.py и DjangoProject_config/urls.py.</span>  


<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border: 2px outset #8A2BE2; padding: 5px;">        ДЕЙСТВИЯ</div>  


### <span style="color: #8A2BE2">**1)** Создание Django-приложения:</span>  
<span style="color: #606060">См. Les13-Django_13-Django_INTRO-1.pdf, слайд 67.</span>  
```
  python manage.py startapp <app_name>
```


### <span style="color: #8A2BE2">**2)** Регистрация приложения в проекте  ▶</span>  <a>DjangoProject_config / settings.py</a>:  
<span style="color: #606060">См. Les13-Django_13-Django_INTRO-1.pdf, слайд 75.</span>  
```python
INSTALLED_APPS = [
    # Встроенные приложения:
    'django.contrib.admin',
    ...,
    'django.contrib.staticfiles',
    # Моё приложение:
    'hw_01_first_app',      # ИЛИ 'myapp.apps.MyappConfig'.
]
```


### <span style="color: #8A2BE2">**3)** Создание представления (Views)  ▶</span>  <a>hw_01_first_app / views.py</a>:  
<span style="color: #606060">См. Les13-Django_13-Django_INTRO-1.pdf, слайд 76.</span>  
```python
    from django.http import HttpResponse

    def hello_django(request):                                      # __ NB! __   hello_django.
        return HttpResponse("<h1>Hello, world!</h1>")
```


### <span style="color: #8A2BE2">**4)** Определение URL-маршрута</span> <a>hw_01_first_app / urls.py</a>:  
<span style="color: #606060">См. Les13-Django_13-Django_INTRO-1.pdf, слайд 77.</span>  
```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('hw_01/', views.hello_django, name='hello_django'),    # __ NB! __  'hw_01/'  and  hello_django.
    ]
```


### <span style="color: #8A2BE2">**5)** Подключение маршрутов приложения к проекту</span> <a>DjangoProject_config / urls.py</a>:  
<span style="color: #606060">См. Les13-Django_13-Django_INTRO-1.pdf, слайд 78.</span>

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('les_01_begins/', include('les_14_begins.urls')),  # Подключение маршрутов приложения les_01_begins.
    path('hw_01_first_app/', include('hw_01_first_app.urls')),  # Подключение маршрутов приложения hw_01_first_app.
]
```


### <span style="color: #8A2BE2">**6)** <a style="color: #F00000;">_ NB! _</a> Проверить ПУТЬ к config-файлу в</span> <a>manage.py</a>:  
<span style="color: #606060">См. Les13-Django_13-Django_INTRO-1.pdf, слайд 76.</span>  
Лучше чтобы папка с config-настройками называлась просто "config".  
Если папка с <a>settings.py</a> называется DjangoProject_config (а не config), то нужно внести 
изменения в настройки:  

Открыть <a>manage.py</a> и найти строку:
```python
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
```
Заменить её на:
```python
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject_config.settings')
```
Ту же самую правку нужно внести и в: <a>wsgi.py</a>, <a>asgi.py</a>.  
Там тоже есть строка с `DJANGO_SETTINGS_MODULE`.
А в <a>settings.py</a> внести правку в СТРОКИ:
```python
    ROOT_URLCONF = 'DjangoProject_config.urls'
    WSGI_APPLICATION = 'DjangoProject_config.wsgi.application'
```


### <span style="color: #8A2BE2; padding: 0px; ">**7)** Проверить работу приложения:</span>  
<span style="color:#FFD700">NB! __ ЗАКОММЕНТИРОВАТЬ</span> в <a>settings.py</a> 
ненужное приложение (<a id="img1">Fig. 1</a>):  
<img src="figs/img_1.png" width="350" alt="Закомментировать НЕнужное приложение."/>

Создать <span style="color:#F00000">СУПЕРЮЗЕРА</span>, <span style="color: #606060">См. Video 15.1 42:30, link: https://player.vimeo.com/video/1090076209?h=56080a1f80</span>  
```
python manage.py createsuperuser
```
> Username (leave blank to use 'odnab'): odnabu  
> Email address: od@django.com  


Запустить локальный сервер Django с помощью manage.py в терминале:
```
python manage.py runserver
```
Перейти по адресу http://127.0.0.1:8000/hw-01, чтобы увидеть стандартную начальную страницу 
Django с текстом приветствия из <a>hw_01_first_app/views.py</a> (<a id="img2">Fig. 2</a>):  

<img src="figs/img_2.png" width="350" alt="Добавить в адресной строке /hw-01, как в приложении."/>  

<span style="color: #606060">См. Video 14, 00:01:00, link: https://player.vimeo.com/video/1089688434?h=2eb8652d7a</span>.  



---

## <span style="color: #008000">3. Настройка базы данных:</span>
- Добавьте в .env файл настройки для подключения к MySQL.
- Реализуйте в settings.py возможность выбора между SQLite и MySQL в зависимости от переменной MYSQL в .env файле.

<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border: 2px outset #8A2BE2; padding: 5px;">        ДЕЙСТВИЯ</div>  


### <span style="color: #8A2BE2">**1)** Настройки для подключения к MySQL:</span>  
<span style="color: #606060">См. Les14-Django_PrfS4.pdf, слайд 16.</span>  
<span style="color: #606060">См. Video 14, 39:10.</span>  
Настройки в <a>.env</a> файле для всех переменных для подключения к MySQL и переменная `MYSQL=True`:  
```python
    MYSQL=True                  # __ NB! __ Но пока здесь лучше поставить False.
    DB_NAME=my_db_name
    DB_USER=my_user_name
    DB_PASSWORD=my_password
    DB_HOST=localhost
    DB_PORT=3306
```


### <span style="color: #8A2BE2">**2)** Возможность выбора между SQLite и MySQL:</span>  
Установить клиент через терминал:
```
pip install mysqlclient
```
Внести изменения в <a>settings.py</a> по примеру в <span style="color: #606060">Les14-Django_PrfS4.pdf, 
слайд 18</span>.  



---

## <span style="color: #008000"> 4. Создание и регистрация приложения:</span>
- Создайте новое приложение в вашем проекте Django.
- Зарегистрируйте приложение в настройках проекта (settings.py).

По 2-му подпункту см. [<font color="#696969">[Fig. 1]</font>](#img1).



---

## <span style="color: #008000"> 5. Реализация представления и маршрута:</span>
- Определите простое представление, которое будет возвращать заголовком текст "Hello, <your_name>".
- Определите URL-маршрут к вашему представлению внутри приложения.
- Подключите маршруты вашего приложения к основному файлу urls.py проекта.

<span style="color: #606060">См. Video "Additional practicum 1: Django models (Library Project)",
3:14:10.</span>  

По 1-му подпункту должно получиться так в браузере (<a id="img3">Fig. 3</a>):  

<img src="figs/img_3.png" width="350" alt="Добавить в адресной строке /home/od, как в приложении."/>  

По 2-му подпункту для URL внутри приложения (<a id="img4">Fig. 4</a>):  

<img src="figs/img_4.png" width="450" alt="Добавление URL внутри приложения."/>  

По 3-му подпункту для URL приложения в файле urls.py проекта (<a id="img5">Fig. 5</a>):  

<img src="figs/img_5.png" width="650" alt="Добавление URL приложения в файле urls.py проекта."/>  



---

## <span style="color: #008000"> 6. Тестирование:</span>
- Запустите локальный сервер и перейдите по созданному URL адресу для проверки корректности реализации.

См. рисунки [<font color="#696969">[Fig. 2]</font>](#img2), 
[<font color="#696969">[Fig. 3]</font>](#img3).  



---

## <span style="color: #008000"> 7. Фиксация зависимостей:</span>
- Зафиксируйте текущие версии всех зависимостей в файле requirements.txt.  

```
pip freeze > hw_01_first_app/requirements_hw_1.txt
```


---

## <span style="color: #008000"> 8. Git</span>
- Запуште проект в Git-репозиторий и прикрепите как решение ссылку на него.

Ссылка на приложение по ДЗ <a>hw_01_first_app</a>: https://github.com/odnabu/Django-Python-Advanced/tree/main/hw_01_first_app.  

Ссылка на весь проект <a>DjangoProject</a>: https://github.com/odnabu/Django-Python-Advanced/tree/main.  

---
[//]: # (<span style="color: #8A2BE2; margin: 20px 10px;">▣</span> )

