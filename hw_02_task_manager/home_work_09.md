Python Advanced - Django  
22.07.2025

## <div style="color: #9000F0">Домашнее задание 15 (9 in Django): <br> Проект "Менеджер задач" — Замена функций представлений на Generic Views для задач и подзадач</div>    
Используя <m style="color: #9000F0">Generic Views</m>, замените существующие классы представлений 
для задач (Tasks) и подзадач (SubTasks) на соответствующие классы для полного 
CRUD (Create, Read, Update, Delete) функционала.  
Агрегирующий эндпойнт для статистики задач оставьте как есть.  
Реализуйте для этих наборов представлений:  
- фильтрацию, 
- поиск, 
- сортировку.

###  Задание 1.  Замена представлений для задач (Tasks) на Generic Views  
Шаги для выполнения:
1. Замените классы представлений для задач на Generic Views:  
   - Используйте ListCreateAPIView для создания и получения списка задач.
   - Используйте RetrieveUpdateDestroyAPIView для получения, обновления и удаления задач.
2. Реализуйте фильтрацию, поиск и сортировку:
   - Реализуйте фильтрацию по полям status и deadline.
   - Реализуйте поиск по полям title и description.
   - Добавьте сортировку по полю created_at.

###  Задание 2.  Замена представлений для подзадач (SubTasks) на Generic Views  
Шаги для выполнения:
1. Замените классы представлений для подзадач на Generic Views:
   - Используйте ListCreateAPIView для создания и получения списка подзадач.
   - Используйте RetrieveUpdateDestroyAPIView для получения, обновления и удаления подзадач.
2. Реализуйте фильтрацию, поиск и сортировку:
   - Реализуйте фильтрацию по полям status и deadline.
   - Реализуйте поиск по полям title и description.
   - Добавьте сортировку по полю created_at.

###  Оформление ответа:
1. Предоставьте решение: 
   - Прикрепите ссылку на гит.
2. Скриншоты тестирования: 
   - Приложите скриншоты из браузера или Postman, подтверждающие:
     - успешное создание, 
     - обновление, 
     - получение, 
     - удаление данных через API.

<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  




### <m style="color: #008000">Источники</m>  
<m style="color: #606060">Видео - уроки от *16.07.2025*</m>  [<font color="#696969">[1 - ▶  Video 27, 2:26:00]</font>](#v1).  
[1] ▶ Video 27 "Python Adv 27: Основы работы с Django REST Framework. Часть 3" (3:17:20), *16.07.2025*: <m id="v1">https://player.vimeo.com/video/1101836539?h=a6cc7637f4</m>.  
[2] ▶ Video 28 "https://player.vimeo.com/video/1101836539?h=a6cc7637f4" (1:34:08), *16.07.2025*: <m id="v2">https://player.vimeo.com/video/1101850131?h=c32bbfde1f</m>.  
[3] Presentation _"Основы работы с Django REST Framework. Часть 3 (1)"_ <a id="p1">Les27-Django_25-REST_p3-16_07.pdf</a>. 
--->  GenericAPIView, Миксины, Generic Views, кастомный функционал в Generic Views.   
[4] Conspectus <a id="c1">Les27-Django_25---REST_p3-16_07.pdf</a>.  
[5] Presentation _"Основы работы с Django REST Framework. Часть 3 (2)"_ <a id="p2">Les27-Django_26-REST_p3-16_07.pdf</a>. 
--->  Атрибуты: lookup_field,  lookup_url_kwarg, filter_backends. Методы: get_object(), get_serializer_context().  
[6] Conspectus <a id="c2">Les27-Django_26---REST_p3-16_07.pdf</a>.  
[7] Приложение **home_work_08**: файл <m id="hw7">home_work_08.md</m>.  
[8] Руководство по оформлению Markdown файлов: https://gist.github.com/Jekins/2bf2d0638163f1294637.  




<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border: 2px outset #8A2BE2; margin: 60px 0 40px 0; padding: 5px 0 5px 25px;">ОТЧЕТ</div>


### <m style="color: #008000">Миграции</m>  

<div style="margin: 40px 20px 20px 0;">
<m style="color: #F00000; border: 2px solid #6B0000; padding: 10px;"> NB ! </m> 
<b style="color: #F00000; border: 1px solid black; padding: 5px;">!!! ВСЕГДА</b> после изменения в моделях (НЕ в сериализаторе) выполнять и применят миграции.
</div>  

Запускать команды `python manage.py shell`, `migrate`, `runserver` — находясь в корне проекта, рядом с <a>manage.py</a>
  (см. [<font color="#696969">[8 - hw_09]</font>](#hw6)).

После изменений в МОДЕЛЯХ сделать и применить миграции [<font color="#696969">[1 - ▶  Video 20, 57:60]</font>](#v1):  
```bash
    python manage.py makemigrations hw_02_task_manager
    python manage.py migrate hw_02_task_manager
```
Запустить локальный сервер Django с помощью <a>manage.py</a> в терминале [<font color="#696969">[1 - ▶  Video 20, 57:60]</font>](#v1):  
```bash
   python manage.py runserver
```

---



## <m id="s1" style="color: #008000">1. Замена представлений для задач (Tasks) на Generic Views</m>  

<div style="margin: 20px 20px 20px 0;">
<b style="color: #F00000; border: 2px solid #6B0000; padding: 10px; margin: 0 10px 0 0;"> NB ! </b> <b style="color: red">1.</b> ПЕРЕИМЕНОВАТЬ нынешний файл <m style="color: red">views.py</m>  в <a>x_old_views.py</a>.
<p style="margin: 0 0 0 65px;"><b style="color: red">2.</b> СОЗДАТЬ новый с именем <a>views.py</a> и уже в него внести чистый код для этой ДЗ.
<p>
<p style="margin: 0 0 0 65px;"> Так как на лекции 23.07.2025 и практике 9 24.07.2025 добавлены Аутентификация и Авторизация,
для успешного окончания этой ДЗ необходимо выполнить такие действия:
<p style="margin: 0 0 0 65px;"><b style="color: red">ИЛИ </b> ОТКЛЮЧИТЬ АУТЕНТИФИКАЦИЮ в 
<m style="color: limegreen">config /</m> <a>settings.py</a> и в <m style="color: limegreen">config /</m> <a>urls.py</a>.
<p style="margin: 0 0 0 65px;"><b style="color: red">ИЛИ --> НЕ подходит, пока не пропишешь настройки в ПРЕДСТАВЛЕНИЯ!!!</b> 
в config-настройках <a>settings.py</a> в блоке REST_FRAMEWORK включить настройку БАЗОВОЙ АУТЕНТИФИКАЦИИ:
</div>

```python
'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.BasicAuthentication',
]
```
Смотри решение для замены представлений для задач (Tasks) на Generic Views у [ChatGPT](https://chatgpt.com/s/t_687fa06f88d08191805b974a29c112e7).

---

### <m id="ss1.1" style="color: #008000">1.1. Импорты</m>  
Скопировать из старого <a>views.py</a> все необходимые импорты из <m style="color: #f08000">Tasks</m> и 
сериализатор <m style="color: #f08000">TaskSerializer</m>.  
Добавить код и документацию к Представлению.

### <m id="ss1.2" style="color: #008000">1.2. Класс для создания и списка задач</m>  
Добавить код и документацию к Представлению.

### <m id="ss1.3" style="color: #008000">1.3. Класс для получения/обновления/удаления задачи</m>  
Добавить код и документацию к Представлению.

---

### <m id="ss1.4" style="color: #008000">1.4. Результаты выполнения задания 1 в браузере</m>  

#### <m id="ss1.4" style="color: #008000">1.4.1. Домашняя страница - приветствие </m>  
Зайти на домашнюю страницу и проверить работу приложения: http://127.0.0.1:8000/hw-02/home/.  
На домашней странице будет видно приветствие: "Welcome to the Task Manager!".  

---

#### <m id="ss1.4.2" style="color: #008000">1.4.2. Создание задачи и получение списка задач </m>  
Перейти по ссылке: http://127.0.0.1:8000/hw-02/tasks/.

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 1 ⋙ </b> Получение списка задач

<img src="figs/hw_09/task_1/img_t1_1.png" width="800" style="margin: 0 0 0 40px"/>  

<m id="img1.1" style="margin: 40px; color:#606060;">Fig. 1.1. Список из 5-ти задач на странице,
отсортированный по умолчанию по ID.</m>

<img src="figs/hw_09/task_1/img_t1_2.png" width="800" style="margin: 0 0 0 40px"/>  

<m id="img1.2" style="margin: 40px; color:#606060;">Fig. 1.2. Следующая (2-я) страница списка задач (окончание) на странице,
отсортированный по умолчанию по ID: http://127.0.0.1:8000/hw-02/tasks/?page=2.</m>

<img src="figs/hw_09/task_1/img_t1_3.png" width="700" style="margin: 0 0 0 40px"/>  

<m id="img1.3" style="margin: 40px; color:#606060;">Fig. 1.3. Список из 5-ти первых задач на странице,
отсортированный по умолчанию по ID.</m>

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 2 ⋙ </b> Создание новой задачи

<img src="figs/hw_09/task_1/img_t1_3_1.png" width="800" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_1/img_t1_3_2.png" width="700" style="margin: 0 0 0 40px"/>

<m id="img1.4" style="margin: 40px; color:#606060;">Fig. 1.4. Создание новой задачи по url http://127.0.0.1:8000/hw-02/tasks/.</m>

---

#### <m id="ss1.4.3" style="color: #008000">1.4.3. Получение, обновление и удаление задач</m>  

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 1 ⋙ </b> Получение детальной информации о задаче

<img src="figs/hw_09/task_1/img_t1_4_1.png" width="800" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_1/img_t1_4_2.png" width="700" style="margin: 0 0 0 40px"/>

<m id="img1.3" style="margin: 40px; color:#606060;">Fig. 1.3. Детальная информация о задаче по ID: http://127.0.0.1:8000/hw-02/tasks/3/.</m>


##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 2 ⋙ </b> Обновление задачи и ее удаление

<img src="figs/hw_09/task_1/img_t1_5_1.png" width="800" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_1/img_t1_5_2.png" width="900" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_1/img_t1_5_3.png" width="700" style="margin: 0 0 0 40px"/><br/>  

<m id="img1.5" style="margin: 40px; color:#606060;">Fig. 1.5. Обновление задачи. Результаты в: 
Postman; PyCharm DB; Browser Chrome.</m>

---

#### <m id="ss1.4.4" style="color: #008000">1.4.4. Фильтрация, поиск и сортировка задач </m>
В Django REST Framework по умолчанию даты в фильтрах ожидаются в формате YYYY-MM-DD.  
Но можно добавить поддержку пользовательских форматов — таких как 25.07.2025, 25/07/2025 и 
даже других — с помощью кастомного фильтра или кастомного FilterSet от django-filter.  
СДЕЛАТЬ переопределение метода filterset_fields, чтобы ДОБАВИТЬ кастомное преобразование даты.  
Решение смотри у [ChatGPT](https://chatgpt.com/s/t_6881d7993ddc819199444408ba03be6c) с созданием файла <a>filters.py</a> 
и без создания [ChatGPT](https://chatgpt.com/s/t_6881d9f1b7748191a6fac211be34eb4c).


##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 1 ⋙ </b> Фильтрация по: `status`, `deadline`

<img src="figs/hw_09/task_1/img_t1_6_1.png" width="700" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_1/img_t1_6_2.png" width="700" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_1/img_t1_6_3.png" width="900" style="margin: 0 0 0 40px"/>

<m id="img1.6" style="margin: 40px; color:#606060;">Fig. 1.6. Результат ФИЛЬТРАЦИИ по <m style="color:#00a000;">status</m> задач в: 
Postman; Browser Chrome.</m>


<img src="figs/hw_09/task_1/img_t1_7_1.png" width="700" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_1/img_t1_7_2.png" width="700" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_1/img_t1_7_3.png" width="900" style="margin: 0 0 0 40px"/>

<m id="img1.7" style="margin: 40px; color:#606060;">Fig. 1.7. Результат ФИЛЬТРАЦИИ задач по <m style="color:#00a000;">deadline</m>, 
url http://127.0.0.1:8000/hw-02/tasks/?status=&deadline=2025-06-25 в: Postman; browser Chrome.</m>


<img src="figs/hw_09/task_1/img_t1_8_1.png" width="700" style="margin: 0 0 0 40px"/><br>

<img src="figs/hw_09/task_1/img_t1_8_2.png" width="700" style="margin: 0 0 0 40px"/>

<m id="img1.8" style="margin: 40px; color:#606060;">Fig. 1.8. Список задач на Monday: 
http://127.0.0.1:8000/hw-02/tasks/by-day/?day=monday.</m>


<img src="figs/hw_09/task_1/img_t1_9_1.png" width="700" style="margin: 0 0 0 40px"/><br>

<img src="figs/hw_09/task_1/img_t1_9_2.png" width="800" style="margin: 0 0 0 40px"/>

<m id="img1.9" style="margin: 40px; color:#606060;">Fig. 1.9. Статистика задач: 
http://127.0.0.1:8000/hw-02/tasks/statistics/.</m>

---

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 2 ⋙ </b> Поиск задачи по: `title`, `description`

<img src="figs/hw_09/task_1/img_t1_10_1.png" width="700" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_1/img_t1_10_2.png" width="800" style="margin: 0 0 0 40px"/>

<m id="img1.10" style="margin: 40px; color:#606060;">Fig. 1.10. Поиск задачи по: `title`.</m>

---

##### <b id="s1.5.3" style="color: #008000; margin: 0 20px 0 0;">⋘ 3 ⋙ </b> Сортировка  по: `created_at`  

<img src="figs/hw_09/task_1/img_t1_11_1.png" width="700" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_1/img_t1_11_2.png" width="900" style="margin: 0 0 0 40px"/>

<m id="img1.11" style="margin: 40px; color:#606060;">Fig. 1.11. Поиск задачи по: `title`.</m>

<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  




## <m id="s2" style="color: #008000">2. Замена представлений для подзадач (SubTasks) на Generic Views</m>  
Смотри решение у [ChatGPT](https://chatgpt.com/s/t_687fa06f88d08191805b974a29c112e7).  

### <m id="s2.1" style="color: #008000">2.1. Импорты</m>  
В файл <a>hw_02_task_manager / views.py</a> добавить необходимые импорты из модели 
<m style="color: #f08000">SubTask</m> и сериализатора <m style="color: #f08000">SubTaskCreateSerializer</m>.  

---

### <m id="s2.2" style="color: #008000">2.2. Список и создание подзадач</m>  
Добавить код и документацию к Представлению.

---

### <m id="s2.3" style="color: #008000">2.3. Подробности, обновление и удаление подзадачи</m>  
Добавить код и документацию к Представлению.

---

### <m id="s2.4" style="color: #008000">2.4. Результаты выполнения задания 2</m>  

#### <m id="ss2.4.1" style="color: #008000">2.4.1. Создание новой подзадачи и получения СПИСКА подзадач </m>  

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 1 ⋙ </b> Получение списка подзадач

Перейти по эндпоинту: http://127.0.0.1:8000/hw-02/subtasks/?page=1 или http://127.0.0.1:8000/hw-02/subtasks/?page=2.

<img src="figs/hw_09/task_2/img_t2_1.png" width="700" style="margin: 0 0 0 40px"/>

<m id="img1" style="margin: 40px; color:#606060;">Fig. 2.1. Вид страницы со списком первых 5-ти подзадач 
по эндпоинту http://127.0.0.1:8000/hw-02/subtasks/.</m>

<img src="figs/hw_09/task_2/img_t2_2.png" width="900" style="margin: 0 0 0 40px"/>  

<m id="img2.2" style="margin: 40px; color:#606060;">Fig. 2.2. Список из 5-ти задач на странице,
отсортированный по умолчанию по ID: http://127.0.0.1:8000/hw-02/subtasks/.</m>

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 2 ⋙ </b> Создание новой подзадачи

<img src="figs/hw_09/task_2/img_t2_3.png" width="900" style="margin: 0 0 0 40px"/>  

<m id="img2.3" style="margin: 40px; color:#606060;">Fig. 2.3. Создание новой задачи по url http://127.0.0.1:8000/hw-02/subtasks/.</m>

---

#### <m id="ss2.4.2" style="color: #008000">2.4.2. Получение, обновление и удаление подзадач </m>  

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 1 ⋙ </b> Получение детальной информации о подзадаче

<img src="figs/hw_09/task_2/img_t2_4.png" width="900" style="margin: 0 0 0 40px"/>  

<m id="img2.4" style="margin: 40px; color:#606060;">Fig. 2.4. Детальная информация о задаче по ID: http://127.0.0.1:8000/hw-02/subtasks/7/.</m>

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 2 ⋙ </b> Обновление задачи и ее удаление

<img src="figs/hw_09/task_2/img_t2_5_1.png" width="700" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_2/img_t2_5_2.png" width="700" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_2/img_t2_5_3.png" width="900" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_2/img_t2_5_4.png" width="900" style="margin: 0 0 0 40px"/>  

<m id="img2.5" style="margin: 40px; color:#606060;">Fig. 2.5. Обновление подзадачи по url http://127.0.0.1:8000/hw-02/subtasks/14/. 
Результаты в: Postman; PyCharm DB; Browser Chrome.</m>

<img src="figs/hw_09/task_2/img_t2_6_1.png" width="900" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_2/img_t2_6_2.png" width="800" style="margin: 0 0 0 40px"/><br/>  

<img src="figs/hw_09/task_2/img_t2_6_3.png" width="900" style="margin: 0 0 0 40px"/>  

<m id="img2.6" style="margin: 40px; color:#606060;">Fig. 2.6. Удаление подзадачи по url http://127.0.0.1:8000/hw-02/subtasks/15/. 
Результаты в: Postman; PyCharm DB; Browser Chrome.</m>

---

#### <m id="ss2.4.3" style="color: #008000">2.4.3. Фильтрация, поиск и сортировка подзадач </m>

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 1 ⋙ </b> Фильтрация по полям `status` и `deadline`

<img src="figs/hw_09/task_2/img_t2_7_1.png" width="700" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_2/img_t2_7_2.png" width="700" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_2/img_t2_7_3.png" width="900" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_2/img_t2_7_4.png" width="800" style="margin: 0 0 0 40px"/>

<m id="img2.7" style="margin: 40px; color:#606060;">Fig. 2.7. Результат ФИЛЬТРАЦИИ по <m style="color:#00a000;">status</m> задач в: 
Postman; Browser Chrome.</m>


##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 2 ⋙ </b> Поиск по полям `title` и `description`

<img src="figs/hw_09/task_2/img_t2_8_1.png" width="700" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_09/task_2/img_t2_8_2.png" width="900" style="margin: 0 0 0 40px"/>

<m id="img2.8" style="margin: 40px; color:#606060;">Fig. 2.8. Поиск подзадач по <m style="color:#00a000;">title</m> и 
<m style="color:#00a000;">description</m> в: Postman; Browser Chrome.</m>

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 2 ⋙ </b> Сортировка по полю `created_at`

<img src="figs/hw_09/task_2/img_t2_9.png" width="900" style="margin: 0 0 0 40px"/>

<m id="img2.9" style="margin: 40px; color:#606060;">Fig. 2.9. Сортировка подзадач по <m style="color:#00a000;">created_at</m>.
Результаты тестирования в: Postman.</m>

<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  




## <m id="s3" style="color: #008000">3. Проверка настроек приложения</m>  
Смотри решение у [ChatGPT](https://chatgpt.com/s/t_687fa06f88d08191805b974a29c112e7).  

### <m id="s3.1" style="color: #008000">3.1. Фильтры</m> `django_filters`  

Установить фильтры в <a>settings.py</a>, если ещё не добавлены:
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}
```

---

### <m id="s3.2" style="color: #008000">3.2. Пакет</m> `django-filter`  

Убедиться, что установлен пакет `django-filter`:
```bash
    pip list
    # Или сразу проверить версию:
    
    # Или установить, если нет:
    pip install django-filter
```

---

### <m id="s3.3" style="color: #008000">3.3. Представления из прежней версии</m> <a>views.py</a>  

#### <m id="s3.3.1" style="color: #008000">3.3.1. Статистика задач</m>  
Как переписать сериализатор для статистики `TaskStatisticsView` в __GenericAPIView__: [ChatGPT](https://chatgpt.com/s/t_687fc539f2e081918ff8c8262c56d628).  
Можно переписать представление `TaskStatisticsView`, используя `GenericAPIView`.  
НО! технически это не требуется — ведь `GenericAPIView` применяется, когда нужно работать 
с `queryset`'ом и сериализацией данных. А в этом случае просто считается статистика и возвращается словарь.

Тем не менее, **можно адаптировать** код, если нужно привести всё к единому стилю с `GenericAPIView`.

Однако, `APIView` вполне корректно и его можно просто скопировать из старой версии <a>views.py</a>, потому что:
- НЕ ведется работа напрямую с сериализаторами или моделями, НЕ возвращаются списки объектов.
- Просто агрегируется статистика — и `APIView` тут прекрасно подходит.


#### <m id="s3.3.1" style="color: #008000">3.3.1. Статистика задач</m>  
Как переписать сериализатор для статистики `TaskStatisticsView` в __GenericAPIView__: [ChatGPT](https://chatgpt.com/s/t_687fc539f2e081918ff8c8262c56d628).  


<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  




## <m id="s4" style="color: #008000">4. GitHub</m>
- Запуште проект в Git-репозиторий и прикрепите как решение ссылку на него.

Ссылка на отчет по ДЗ <a>home_work_09.md</a> со скриншотами: https://github.com/odnabu/Django-Python-Advanced/blob/main/hw_02_task_manager/home_work_09.md.  

Ссылка на приложение по ДЗ <a>hw_02_task_manager</a>: https://github.com/odnabu/Django-Python-Advanced/tree/main/hw_02_task_manager.  

Ссылка на весь проект <a>DjangoProject</a>: https://github.com/odnabu/Django-Python-Advanced/tree/main.  


<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #8A2BE2; padding: 5px; margin: 40px 0 40px 0"></div>

[//]: # ([<font color="#696969">[1 - ▶  Video 22, 48:00]</font>]&#40;#v1&#41;)
[//]: # ([<font style="color: #606060;">[2, слайд 32]</font>]&#40;#p1&#41;)

[//]: # (<div style="margin: 40px 0 40px 0"></div>)

[//]: # (<m style="color: #8A2BE2; margin: 20px 40px; padding: 5px; background: #000000;">▣ ⚜️ ☑️ ✔️ 🟪 ■ ※ ⁂ ⁙ ⁘ ⨠  ■ ◲◳ ◆ ◇ ◈ ◀ ▶ ◁ ▷ ▹ ▼ ▲ ▽ △ ▢ ₪₪₪</m>   )  

[//]: # (<div style="font: small-caps 120% sans-serif; color: #8A2BE2; margin: 0 0 0 0px; padding: 0 15px 0 0;">▣ &nbsp;&nbsp; Выполните запросы:</div>  )
[//]: # (🔷🔹 🟩 ❇️♾️⚜️✳️❎✅☑️✔️🟪🔳🔲  )
[//]: # (■ ⁜ ※ ⁂ ⁙ ⁘ ⫷ ⫸ ⩕ ⨠ ⨝ ⋘ ⋙ ∵ ∴ ∶ ∷ ■ ◪ ◩ ◲ ◳ ◆ ◇ ◈ ▼ ▽ ◀ ▶ ◁ ▷ ▹ ▲ △ ▢ ₪₪₪  )


[//]: # (<div style="color: #F00000; margin: 40px 20px 20px 0;">)

[//]: # (<m style="border: 2px solid #6B0000; padding: 10px;"> NB ! </m>)

[//]: # (</div>)


[//]: # (&nbsp;&nbsp; spaces)
[//]: # (<div style="font: small-caps 120% sans-serif; color: #8A2BE2; padding: 0 15px 0 0;">▣ &nbsp;&nbsp; Выполните запросы:</div>  )

[//]: # (<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>)



[//]: # (== RegEx в PyCharm ==)

[//]: # (Как найти все тексты между тегами <a>...</a> в PyCharm)

[//]: # (1️⃣ Открой нужный файл в PyCharm.)

[//]: # (2️⃣ Нажми Ctrl + F — откроется строка поиска.)

[//]: # (3️⃣ Нажми на .∗ значок ".*", чтобы включить режим RegEx &#40;регулярных выражений&#41;.)

[//]: # (4️⃣ Введи такой шаблон:)

[//]: # (<a>&#40;.*?&#41;</a>)

[//]: # (📌 Что означает шаблон:)

[//]: # (- <a> и </a> — буквально ищем открывающий и закрывающий теги.)

[//]: # (- &#40;.*?&#41; — захватывает любой текст между ними, включая кириллицу, пробелы и спецсимволы.)

[//]: # (- ? — делает захват нежадным, чтобы не схватывало всё сразу до последнего </a>.)

[//]: # (✨ Хочешь выделить или заменить текст?)

[//]: # (Если ты нажмёшь Ctrl + Shift + R — откроется Поиск и замена по шаблону.)

[//]: # (Можно заменить на, например:)

[//]: # ([ссылка: \1])

[//]: # ( \1 — это то, что попало в скобки &#40;.*?&#41;.)

