Python Advanced - Django  
29.07.2025

## <div style="color: #9000F0">Домашнее задание 19 (13 in Django): <br> Проект "Менеджер задач" — .</div>    
__Цель:__  


###  Задание 1. 
Шаги для выполнения (см. начало [<font color="#696969">[3, p. 77]</font>](#p1), [<font color="#696969">[4, s. 22]</font>](#c1)):
1. 

###  Задание 2.  
Шаги для выполнения:


###  Задание 3.   

###  Оформление ответа:
1. Предоставьте решение: Прикрепите ссылку на гит.
2. Скриншоты тестирования: 
   - Приложите скриншоты из Postman, подтверждающие: 
     - успешное использование JWT токенов и соблюдение пермишенов при работе с задачами, 
     - пагинацию страниц при HTTP GET ответах.

<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  


### <m style="color: #008000">Источники</m>  
<m style="color: #606060">Видео - уроки от *\_.07.2025*</m>  [<font color="#696969">[1 - ▶  Video \_, c \_:\_:\_]</font>](#v1).  
[1] ▶ Video \_ "" (\_:\_:\_), *\_.07.2025* начиная 
<m style="color: red">c \_:\_:\_</m>: <m id="v1"></m>.  
[2] ▶ Video \_ "" (\_:\_:\_), *\_.07.2025* начиная 
<m style="color: red">c \_:\_</m>: <m id="v2"></m>.  
[3] Presentation \_ _""_.  
<a id="p1"></a>. 
<m style="color: #606060">——▷  </m>   
[4] Conspectus \_ <a id="c1"></a>.  
[5] Presentation \_ _""_.  
<a id="p2"></a>. 
<m style="color: #606060">——▷  </m>.   
[6] Conspectus \_ <a id="c2"></a>.  
[7] Приложение **home_work_12**: файл <m id="hw7">home_work_12.md</m>.  
[8] Руководство по оформлению Markdown файлов: https://gist.github.com/Jekins/2bf2d0638163f1294637.  
[9] Шпаргалка по Markdown: https://gist.github.com/fomvasss/8dd8cd7f88c67a4e3727f9d39224a84c.




<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border: 2px outset #8A2BE2; margin: 60px 0 40px 0; padding: 5px 0 5px 25px;">ОТЧЕТ</div>


### <m style="color: #008000">Миграции</m>  

<div style="margin: 40px 20px 20px 0;">
<m style="color: #F00000; border: 2px solid #6B0000; padding: 10px;"> NB ! </m> 
<b style="color: #F00000; border: 1px solid black; padding: 5px;">!!! ВСЕГДА</b> после изменения в моделях (НЕ в сериализаторе) выполнять и применять миграции.
<p style="margin: 0 0 0 55px;"><b style="color: #F00000; border: 1px solid black; padding: 5px;">ПРИМЕНЯТЬ</b> миграции так же нужно в ситуациях:
<p style="margin: 0 0 0 70px;">1. Склонирован/получен проект с миграциями.
<p style="margin: 0 0 0 70px;">2. Применения уже готовых .py-файлы миграций.
<p style="margin: 0 0 0 70px;">3. На сервере (или в другом окружении).
<p style="margin: 0 0 0 70px;">4. После восстановления базы данных нужно применить все миграции.
<p style="margin: 0 0 0 70px;"><b style="color: #F00000;">5.</b> После изменения настроек БД или установки приложения. 
Например, добавления в файл настроек нового приложения, предоставляющего токен. 
</div>  

Детально, когда нужно выполнять `python manage.py migrate` БЕЗ `makemigrations` см. тут [ChatGPT](https://chatgpt.com/s/t_6887c91d9ad481919a0d65104ad52b99).

Запускать команды `python manage.py shell`, `migrate`, `runserver` — находясь в корне проекта, рядом с <a>manage.py</a>
  (см. [<font color="#696969">[8 - hw_10]</font>](#hw6)).

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



## <m id="s1" style="color: #008000">1. </m>  

<div style="margin: 20px 20px 20px 0;">
<b style="color: #F00000; border: 2px solid #6B0000; display: inline-block; padding: 10px; margin: 0 10px 0 0;"> NB ! </b>Так как на консультации 1 от 28.07.2025 пофиксили проблемы с обновлением токена 
для Аутентификации и Авторизации для всего проекта благодаря решению Макса Полякова, то теперь в настройках
<m style="color: limegreen">config /</m> <a>settings.py</a> и в <m style="color: limegreen">config /</m> <a>urls.py</a>
можно ничего не отключать опцию, связанную с Аутентификацией.
</div>

Описание реализации настройки JWT-аутентификации по шагам смотри в:  
1. записи урока [<font color="#696969">[1 - ▶  Video 33]</font>](#v1) начиная <m style="color: red">c 1:52:35</m>.
2. записи урока [<font color="#696969">[2 - ▶  Video 34]</font>](#v2) начиная <m style="color: red">c 20:40</m>.
3. тексте презентации и конспекте (начало) [<font color="#696969">[3, s. 40], [4, p. 15]</font>](#p1).
4. тексте презентации и конспекте (продолжение) [<font color="#696969">[5, s. 7], [6, p. 2]</font>](#p2)
5. решении для этой задачи от [ChatGPT](https://chatgpt.com/s/t_688899135da88191bddc291ff171104b).  
6. примере реализации [settings.py from V. Bandylo on GitHub](https://github.com/viacheslav-bandylo/111124-projects/blob/main/config/settings.py). 


<div style="font: small-caps 120% sans-serif; color: #9000F0; padding: 0 15px 0 0;">▣ &nbsp;&nbsp; ТЕОРИЯ</div>

<m style="color: #9000F0">Аутентификация</m> - <m style="color: red">КТО</m> - процесс проверки подлинности 
пользователя или устройства, запрашивающего доступ к ресурсу [<font color="#696969">[1 - ▶  Video 33, 1:54:50]</font>](#v1).  
По-сути __проверка ПРАВ пользователя__ [<font color="#696969">[1 - ▶  Video 33, 1:54:25]</font>](#v1).    
В контексте DRF _означает_ __установление личности пользователя__.  

<m style="color: #9000F0">Авторизация</m> - <m style="color: red">ЧТО разрешено</m> - процесс определения, имеет ли 
аутентифицированный пользователь право доступа к конкретным ресурсам или действиям [<font color="#696969">[1 - ▶  Video 33, 1:55:20]</font>](#v1).  
Можно сказать, что программа решает, в какие места пользователю открыт доступ, после того как личность уже 
установлена [<font color="#696969">[1 - ▶  Video 33, 1:54:25]</font>](#v1).  
В DRF это _осуществляется_ с помощью __разрешений, прав и других критериев__.  

<m style="color: #9000F0">JWT (JSON Web Token)</m> - компактный, URL-безопасный способ передачи утверждений 
между двумя сторонами. Используется для аутентификации пользователей в API.  
<m style="color: #9000F0">Структура JWT:</m>  
1. Заголовок (header): Содержит метаданные, такие как тип токена и алгоритм шифрования.
2. Полезная нагрузка (payload): Содержит утверждения и другую информацию о пользователе.
3. Подпись (signature): Подписывает токен, чтобы убедиться, что он не был изменен.

### <m id="ss1.1" style="color: #008000">1.1. </m>  
В файле настроек <a>settings.py</a> проверить наличие кода (после всех лекций и практик) для:    


---

### <m id="ss1.2" style="color: #008000">1.2. </a>  
Проверить маршруты для получения и обновления токенов в <a>DjangoProject_config / urls.py</a>.  

---

### <m id="ss1.3" style="color: #008000">1.3. Проверка токенов через Postman или браузер:</m>  
Поскольку я уже сгенерировала refresh-токен в <a>home_work_10.md</a> и он будет валиден еще как минимум неделю (сегодня 29.07.2025),
а access-токен обновляется через <a>DjangoProject_config / middleware.py</a> автоматически, пока валиден refresh-токен (10 дней), 
признаться, мне не хочется сейчас тратить драгоценное время на повторение тех же действий с генерацией токенов в
Postman и размещением скриншотов в отчете к этой ДЗ. При желании результаты генерации токенов можно еще раз увидеть 
в <a>home_work_10.md</a> начиная с п. "1.4. Результаты выполнения задания 1 в браузере". 

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ 1 ⋙ </b> Получение JWT  
<m style="color: limegreen">POST</m> <a>/api/token/</a> (см. [<font color="#696969">[3, s. 86-91]</font>](#p1), 
[ChatGPT](https://chatgpt.com/s/t_688899135da88191bddc291ff171104b)): 



<img src="figs/hw_13/img_1.png" width="900" style="margin: 0 0 0 40px"/><br>  

<img src="figs/hw_13/task_1/img_2.png" width="900" style="margin: 0 0 0 40px"/>

<m id="img1.1" style="margin: 40px; color:#606060;">Fig. 1.1. Выполнение POST-запроса в Postman для получения JWT-токена.</m>


<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  



## <m id="s2" style="color: #008000">2. Реализация пермишенов для API</m>    
Описание реализации разрешений (Permissions) по шагам смотри:  
1. в записи урока [<font color="#696969">[1 - ▶  Video 33]</font>](#v1) <m style="color: red">c 2:40:25</m>.
2. <b style="color: #F00000; border: 2px solid #6B0000; display: inline-block; padding: 10px; margin: 0 10px 0 0;"> NB ! </b> в записи урока "Python Adv 34: Практикум 9" от 23.07.2025 <m style="color: red">c 1:09:20</m> <font color="#696969">[1 - ▶  Video 34]</font>.<br> <m style="color: lime">Именно в этом видео начинаются PERMISSIONS</m>.
3. в тексте презентации и конспекте (продолжение) [<font color="#696969">[5, s. 32]</font>](#p2)
4. в решении для этой задачи от [ChatGPT](https://chatgpt.com/s/t_688899135da88191bddc291ff171104b).  
5. в примере реализации ["library" from V. Bandylo on GitHub](https://github.com/viacheslav-bandylo/111124-projects/blob/main/config/settings.py). 


<b style="color: #F00000; border: 2px solid #6B0000; display: inline-block; padding: 10px; margin: 0 10px 0 0;"> NB ! </b> Непосредственно код для <m style="color: #9000F0">Представлений</m> по примеру на видео: 

- [<font color="#696969">[1 - ▶  Video 33]</font>](#v1) <m style="color: red">c 2:40:25</m>, 
- в коде файла <a>views.py</a> [views.py to "library" from V. Bandylo on GitHub](https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/views.py).


<div style="font: small-caps 120% sans-serif; color: #9000F0; padding: 0 15px 0 0;">▣ &nbsp;&nbsp; ТЕОРИЯ</div>

<m style="color: #9000F0">Permissions</m> - разрешения в DRF определяют, какие пользователи 
имеют доступ к различным ресурсам API.

<m style="color: #9000F0">Кастомный permission:</m>    
- Создать файл <a>permissions.py</a> в приложении <a>hw_02_task_manager/</a>.  
- Далее либо добавить в него ИЛИ код из [permissions.py to "library" from V. Bandylo on GitHub](https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/permissions.py) 
ИЛИ код из решения [ChatGPT](https://chatgpt.com/s/t_688899135da88191bddc291ff171104b) и отредактировать:
```python
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Только владелец может редактировать. Остальные — только читать.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

```

Далее прописать <m style="color: #9000F0">СТАНДАРТНЫЕ пермишены</m> из DRF - DjangoModelPermissions для всех 
Представлений приложения.  

После связать представления с url в файле <a>hw_02_task_manager / urls.py</a>, см. 
[<font color="#696969">[1 - ▶  Video 33, 2:44:40]</font>](#v1).






---

### <m id="s2.1" style="color: #008000">2.1. </m> 
В файл <a>DjangoProject_config / settings.py</a> добавить настройки по примерам в источниках выше.  
При этом сделать сведения кода для оптимизации его работы.  


##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ Шаг 1 ⋙ </b> 


##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ Шаг 2 ⋙ </b> Д


##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ Шаг 3 ⋙ </b> 

##### <b style="color: #008000; margin: 0 20px 0 0;">⋘ Шаг 4 ⋙ </b> 

---

### <m id="s2.2" style="color: #008000">2.2. </m>  

<img src="figs/hw_13/task_1/img_1.png" width="900" style="margin: 0 0 0 40px"/>

<m id="img1" style="margin: 40px; color:#606060;">Fig. 2.1. Результат логирования GET-запросов в <a>db_logs.log</a></m>

<img src="figs/hw_13/task_1/img_2.png" width="500" style="margin: 0 0 0 40px"/>

<m id="img1" style="margin: 40px; color:#606060;">Fig. 2.1. Результат логирования GET-запросов в <a>http_logs.log</a></m>

<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  



## <m id="s3" style="color: #008000">3. GitHub</m>
- Запуште проект в Git-репозиторий и прикрепите как решение ссылку на него.

Ссылка на отчет по ДЗ <a>home_work_12.md</a> со скриншотами: .  

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


