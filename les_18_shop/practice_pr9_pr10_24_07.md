24.07.2025   
## <div style="color: #9000F0">Lesson 34, Practice 9</div>    
app "shop".

See Les34-Django_Pr9.pdf  and  Les34-Django_PrfS9-24_07.pdf


### 24.07.2025 - Pr 9: Задание 1.1. Настройка BasicAuthentication
Настройте базовую аутентификацию.
1. Откройте файл settings.py.
2. Добавьте BasicAuthentication в настройки.
Проверить в браузере по эндпоинту http://127.0.0.1:8000/shop/product/.


### ЗАКОДИРОВАТЬ логин и пароль
Можно сделать в https://www.base64encode.org/.

Через сам Postman: 
![img_4.png](img_4.png)

Через ВНЕШНЕЕ кодирование:
![img_5.png](img_5.png)

Чат, объясни, пожалуйста, почему в Хром и Едж не появляется плашка с вводом догина и пароля при 
попытке перейти по адресу http://127.0.0.1:8000/shop/product/. Я тестирую аутентификацию. ОС Виндовс 11.
https://chatgpt.com/s/t_6881e331fc908191bd9f25a92654b314


### 24.07.2025 - Pr 9: Задание 2.1. Настройка TokenAuthentication
Настройте аутентификацию с использованием токенов.
1. Добавьте приложение rest_framework.authtoken в INSTALLED_APPS в settings.py.
2. Выполните миграции для создания таблицы токенов.
3. Добавьте TokenAuthentication в настройки.

Через Браузер с ТОКЕНОМ не получится работать!!!

```
{
    "token": "8a5263caaf1624c0a1a4a81da2466c6e7e4957e8"
}
```

![img_6.png](img_6.png)

![img_7.png](img_7.png)

![img_8.png](img_8.png)



### 24.07.2025 - Pr 9: Задание 3.1. Настройка JWTаутентификации
Настройте аутентификацию с использованием JWT.
1. Установите пакет djangorestframework-simplejwt.
2. Добавьте настройки для JWTAuthentication.

Сначала установить:
```shell
  pip install djangorestframework-simplejwt
```

Результат в Постмане:  

```python
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MzQzMDQ0NywiaWF0IjoxNzUzMzQ0MDQ3LCJqdGkiOiJlYTlkN2RkYWUyZWI0MDAzOWI0NmE2MTEzNzAzODIwMSIsInVzZXJfaWQiOiIxIn0.MmudSBdIVPncJ6WPJLnrf2X-UIv4OM5xMfAJs54_3bQ",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzNDI2ODQ3LCJpYXQiOjE3NTMzNDQwNDcsImp0aSI6IjMyNDdiZDAzYTI3NjQ0OTNhODFiZDgyM2I3ZGFmYTUwIiwidXNlcl9pZCI6IjEifQ.tiDyCRsRuMZu2cheYVyUs-odSDM6vMp0AU2zMjTcBGw"
}
```
![img_9.png](img_9.png)

РЕЗУЛЬТАТ получения списка продуктов в Постмане:

![img_10.png](img_10.png)



---

### 24.07.2025 - Pr 9: Задание 4.3. Использование разрешений для остальных представлений
Настройте разрешения для остальных представлений, обсудив какие необходимо применить.

![img_11.png](img_11.png)



---

### 24.07.2025 - Pr 10: Задание 1. Извлечение пользователя из объекта запроса

```python

class OrderViewSet(viewsets.ModelViewSet):
    # ВРЕМЕННО, чтобы с ТОКЕНОМ не морочиться:
    authentication_classes = [BasicAuthentication]

    # Явно указываем классы разрешений для этого представления.
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer

    def get_queryset(self):
        """
        Этот метод определяет список объектов для отображения.
        Мы фильтруем заказы, оставляя только те, где поле `user`
        совпадает с текущим пользователем.
        Таким образом, каждый пользователь видит только свои заказы.
        """
        return Order.objects.filter(user=self.request.user)

    # Переопределяем метод perform_create
    def perform_create(self, serializer):
        """
        При создании заказа мы автоматически подставляем текущего пользователя
        в поле `user`. `self.request.user` — это и есть текущий
        авторизованный пользователь.
        """
        serializer.save(user=self.request.user)

```
POST Customers:
![img_12.png](img_12.png)
![img_14.png](img_14.png)

GET ORDERS:  
![img_16.png](img_16.png)



---

### 24.07.2025 - Pr 10: Задание 2. Создание кастомных классов разрешений

```python
class OrderViewSet(viewsets.ModelViewSet):
    # ВРЕМЕННО, чтобы с ТОКЕНОМ не морочиться:
    authentication_classes = [BasicAuthentication]

    # Явно указываем классы разрешений для этого представления.
    # +
    # 24.07.2025 - Pr 10: Задание 2. Создание кастомных классов разрешений
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer
    ...
```
![img_17.png](img_17.png)


---

### 24.07.2025 - Pr 10: Задание 3. Добавление эндпоинта для статистики. Часть 1

```python
    AUTH_USER_MODEL = env('AUTH_USER_MODEL', default='auth.User')
```
![img_18.png](img_18.png)
![img_19.png](img_19.png)

