"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # http://127.0.0.1:8000/admin/
    path('les_01_begins/', include('les_14_begins.urls')),  # Подключение маршрутов приложения les_01_begins.
                    # При этом в браузере нужно ввести: http://127.0.0.1:8000/les_01_begins/<адрес из VIEWS>.
    # path('', include('hw_01_first_app.urls')),          # Подключение маршрутов ТОЛЬКО из приложения hw_01_first_app.
                    # Если несколько приложений, то пустые кавычки '' здесь НЕЛЬЗЯ использовать!.
    path('hw_01_first_app/', include('hw_01_first_app.urls')),  # Так нужно делать, если у меня в
                    # проекте Пайчарм НЕ одно приложение, как сейчас: les_01_begins, hw_01_first_app.
                    # При этом в браузере нужно ввести: http://127.0.0.1:8000/hw_01_first_app/<адрес из VIEWS>
                    # (у меня для 1-ой функции ендпоинт hw-01/ и по нему выводится приветственное сообщение в браузере).
    path('hw-02/', include('hw_02_task_manager.urls')),
]
