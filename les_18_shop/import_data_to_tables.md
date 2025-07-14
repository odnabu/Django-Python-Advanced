26.06.2025   
## <div style="color: #9000F0">Lesson 23, Practice 6</div>    
Les23-Copy of Django_Pr6.pdf  

<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  

### <span style="color: #008000">Интро</span>  

> Добавьте через shell наборы данных из файла store_data.py:  
>> from store_data import *  <br>
>> export_data()

a) сохранить файл с данными store_data.py в корень Проекта.
b) Запустить Шелл:
```
python manage.py shell
```
c) Выполнить команды из примера в задании.


<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  

<div style="margin: 20px 20px 20px 0;">
<b style="color: #F00000; border: 2px solid #6B0000; padding: 10px; margin: 0 10px 0 0;"> NB ! </b>
Если в Шелле <b style="color: red"> НЕ </b> выполняются команды импорта-экспорта данных
из файла в таблицы приложения:
</div>

<img src="figs_les23_pr6/img.png" width="350" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 0 40px; padding: 2px 10px 2px 10px; ">Fig. 1.</div>

1. выйти из Шелл, если он запущен (Ctrl+z) ИЛИ:
```shell
  exit()
```
2. удалить папку с миграциями ___ЦЕЛИКОМ___.  
3. Удалить все таблицы, связанные с приложением: простым выделением и правой кнопкой мыши 
выбрать в контекстном меню команду Drop.  

<img src="figs_les23_pr6/img_1.png" width="350" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 0 40px; padding: 2px 10px 2px 10px; ">Fig. 2.</div>

4. Удалить ВСЕ записи, связанные с приложением, в таблице с миграциями в ___консоли для БД___ через команду:
```python
delete from django_migrations
where app = "les_18_shop";
```
<img src="figs_les23_pr6/img_2.png" width="500" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 0 40px; padding: 2px 10px 2px 10px; ">Fig. 3.</div>

5. сделать и применить  миграции (лучше для конкретного приложения).
```
 python manage.py makemigrations les_18_shop
 python manage.py migrate les_18_shop
```
<img src="figs_les23_pr6/img_3.png" width="550" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 0 40px; padding: 2px 10px 2px 10px; ">Fig. 4.</div>

5. запустить заново Шелл.

<img src="figs_les23_pr6/img_4.png" width="450" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 0 40px; padding: 2px 10px 2px 10px; ">Fig. 5.</div>

6. снова выполнить команды експорта данных (см. рис. выше - красным):
```shell
  from store_data import *
```
```shell
  export_data()
```
7. Теперь МОЖНО выполнять команды в консоли :)  (см. рис. выше - зеленым)

<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  

## <a style="color: #008000">ВОЗВРАЩАЕМСЯ к выполнению заданий:</a>  


<div style="font: bold normal 110% sans-serif; color: #8A2BE2; white-space: pre; border-top: 2px dotted #008000; padding: 5px;"></div>  

### <span style="color: #008000">Задача 1</span>  
Цель: Вычислить общую стоимость всех продуктов в базе данных.
Инструкция:
1. Используйте модель Product.
2. Рассчитайте общую стоимость всех продуктов (цена умноженная на количество) в базе данных.

```shell
from django.db.models import Sum, F
from les_18_shop.models import Product
total_sum = Product.objects.aggregate(total=Sum(F('price') * F('quantity')))
total_sum
```

<img src="figs_les23_pr6/img_5.png" width="600" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 5px 40px; padding: 2px 10px 2px 10px; ">Fig. 6.</div>

<img src="figs_les23_pr6/img_6.png" width="600" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 0 40px; padding: 2px 10px 2px 10px; ">Fig. 7.</div>

```shell
avg_price_products = Product.objects.values('category__name').annotate(avg_price=Avg('price')).order_by('category__name')
avg_price_products
```

<img src="figs_les23_pr6/img_7.png" width="600" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 0 40px; padding: 2px 10px 2px 10px; ">Fig. 8.</div>

```shell
for item in avg_price_products:
  print(f"Category: {item['category__name']}, Avg_Price: {item['avg_price']}")
```
<img src="figs_les23_pr6/img_8.png" width="600" style="margin: 0 0 0 40px; border-bottom: 1px solid dimgrey; "/>  

<div style="color: dimgrey; margin: 0 0 0 40px; padding: 2px 10px 2px 10px; ">Fig. 9.</div>


### <span style="color: #008000">Задача 2</span>  
Средняя цена продуктов по категориям 
Цель: Вычислить среднюю цену продуктов для каждой категории. 
Инструкция: 
1. Используйте модели Product и Category. 
2. Группируйте продукты по категориям и вычислите среднюю цену для каждой категории.

```shell

```



--- 
Pattern
### <span style="color: #008000">Задача __</span>  
```shell

```


