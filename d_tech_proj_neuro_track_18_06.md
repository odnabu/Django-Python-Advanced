German Technikum 14 - Django  
Bedov Dmitrii  
18.06.2025  

## <div style="color: #9000F0">Technischer Unterricht. <br>
Aufgabe 6: ein Projekt "NeuroTrack" (Django)</div>    
 
####  Задание 1.  
- Добавить настройку инлайн форм для админ класса задач. 
При создании задачи должна появиться возможность создавать сразу и подзадачу.

####  Задание 2.   
- Названия задач могут быть длинными и ухудшать читаемость в Админ панели, поэтому требуется 
выводить в списке задач укороченный вариант – первые 10 символов с добавлением «...», 
если название длиннее. При этом при выборе задачи для создания подзадачи должно отображаться 
полное название. Необходимо реализовать такую возможность.

####  Задание 3.  
- Реализовать свой action для Подзадач, который поможет выводить выбранные в 
Админ панели объекты в статус Done.



<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  

### <span style="color: #008000">Источники</span>  
<span style="color: #606060">Видео - урок от 23.06.2025</span> [<font color="#696969">[1 - ▶  Video 20]</font>](#v1).  
1. ▶ Video 20 "Инлайн формы в Admin панели" (23.06.2025): <a id="v1">https://player.vimeo.com/video/1095537775?h=756820df7e.</a>    
2. Presentation <a id="p1">Les13-Technical_Python_13_New-Django-18-06-25.pdf.pdf.</a>  
3. Conspectus <a id="c1">Les20-Python Adv_L20---Инлайн формы-23_06.pdf.</a>  
4. Приложение **home_work_02**: файл <a id="hw4">home_work_04.md</a>.  
5. Руководство по оформлению Markdown файлов: https://gist.github.com/Jekins/2bf2d0638163f1294637.



<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border: 2px outset #8A2BE2; margin: 60px 0 40px 0; padding: 5px 0 5px 25px;">ОТЧЕТ</div>

## <a id="s1" style="color: #008000">1. Настройка инлайн-форм для админ класса задач</a>  

### <a id="s1.1" style="color: #008000">1.1. Код для подключения инлайн-форм</a>  
В приложении **home_work_02** в файле <a>admin.py</a> добавить код для настроек Инлайн-форм 
по примеру в **les_15_users** на уроке [<font color="#696969">[1 - ▶  Video 20, 48:00]</font>](#v1).

<div style="margin: 20px 20px 20px 0;">
<b style="color: #F00000; border: 2px solid #6B0000; padding: 10px; margin: 0 10px 0 0;"> NB ! </b>
Чтобы настроить ИНЛАЙНЫ в Админке, нужно сначала переместить код для 
SubTaskAdmin и для SubTaskInline <b style="color: red">ВЫШЕ</b> TaskAdmin!
</div>


