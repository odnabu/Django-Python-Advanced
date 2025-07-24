from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from les_18_shop.models import Category, Supplier, ProductDetail, Address, Customer, Order, OrderItem
from les_18_shop.serializers import (CategorySerializer, SupplierSerializer,
                                     AddressSerializer,
                                     CustomerSerializer, CustomerCreateUpdateSerializer,
                                     OrderSerializer, OrderCreateUpdateSerializer,
                                     OrderItemSerializer, OrderItemCreateUpdateSerializer)

# 24.07.2025 - Pr 10: Задание 2. Создание кастомных классов разрешений
from les_18_shop.permissions import IsOwnerOrReadOnly, CanViewOrderStatistics


# 27.07.2025 - Pr 8: Задание 1: Представления и маршруты для модели Category
class CategoryViewSet(viewsets.ModelViewSet):
    """
    ЭТОТ ТЕКСТ отобразится в БРАУЗЕРЕ!
    ---
    Это представление предоставляет полный набор действий CRUD для модели Category.
    ---
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 27.07.2025 - Pr 8: Задание 2: Представления и маршруты для модели Supplier
class SupplierViewSet(viewsets.ModelViewSet):
    """
    Представления и маршруты для модели Supplier
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# 27.07.2025 - Pr 8: Задание 3: Представления и маршруты для модели Product
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from les_18_shop.models import Product
from les_18_shop.serializers import (ProductSerializer, ProductCreateUpdateSerializer,
                                     ProductDetailSerializer, ProductDetailCreateUpdateSerializer)

class ProductListCreateView(ListCreateAPIView):
    """
    Представление для получения списка продуктов и создания нового продукта.
    """
    queryset = Product.objects.all()

    # ____ Для practice_21_07.md:
    # Задание 9.1: Настройка фильтрации для модели Product
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']

    # ____ Для practice_9_24_07.md:
    # 24.07.2025 - Pr 9: Задание 1.1. Настройка BasicAuthentication
    # Явно указываем классы аутентификации для этого представления.
    # Это переопределит глобальные настройки, если они есть.
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]

    # Явно указываем классы разрешений для этого представления.
    # Пользователь должен быть аутентифицирован для доступа.
    # permission_classes = [IsAuthenticated]

    # 24.07.2025 - Pr 9: Задание 4.3. Использование разрешений для остальных представлений
    # Настройте разрешения для остальных представлений, обсудив какие необходимо применить.
    # permission_classes = [IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly]
    # permission_classes = [AllowAny]

    # Явно указываем классы разрешений для этого представления:
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ____ Для practice_21_07.md:
    # _____  Переопределяем метод ProductCreateUpdateSerializer  ______
    # Этот метод позволяет нам динамически выбирать сериалайзер:
    def get_serializer_class(self):
        # Для безопасных методов (только чтение), таких как GET:
        if self.request.method == 'GET':
            return ProductSerializer
        # Для остальных методов (POST):
        return ProductCreateUpdateSerializer




class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления одного продукта.
    """
    queryset = Product.objects.all()

    # Явно указываем классы разрешений для этого представления:
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        # Для чтения данных:
        if self.request.method == 'GET':
            return ProductSerializer
        # Для изменения или удаления (PUT, PATCH, DELETE):
        return ProductCreateUpdateSerializer


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()

    # Явно указываем классы разрешений для этого представления:
    permission_classes = [IsAuthenticatedOrReadOnly]

    # _____  Переопределяем метод ProductCreateUpdateSerializer  ______
    # Этот метод позволяет нам динамически выбирать сериалайзер:
    def get_serializer_class(self):
        # Для безопасных методов (только чтение), таких как GET:
        if self.request.method == 'GET':
            return ProductDetailSerializer
        # Для остальных методов:
        return ProductDetailCreateUpdateSerializer

# 27.07.2025 - Pr 8: Задание 5: Представления и маршруты для модели Address
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # Явно указываем классы разрешений для этого представления:
    permission_classes = [IsAdminUser]


# 27.07.2025 - Pr 8: Задание 6: Представления и маршруты для модели Customer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()

    # Явно указываем классы разрешений для этого представления:
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Задание 9.2: Настройка фильтрации для модели Customer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer


# 27.07.2025 - Pr 8: Задание 7: Представления и маршруты для модели Order
# Заменяем ВЕСЬ класс, так как queryset уже не нужен для def get_serializer_class(self):
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#
#     # Явно указываем классы разрешений для этого представления:
#     permission_classes = [IsAuthenticated]
#
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return OrderSerializer
#         return OrderCreateUpdateSerializer
#
#     # 24.07.2025 - Pr 10: Задание 1. Извлечение пользователя из объекта запроса:
#     # Переопределяем метод perform_create
#     def perform_create(self, serializer):
#         """
#         При создании заказа мы автоматически подставляем текущего пользователя
#         в поле `user`. `self.request.user` — это и есть текущий
#         авторизованный пользователь.
#         """
#         serializer.save(user=self.request.user)

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



# 27.07.2025 - Pr 8: Задание 8: Представления и маршруты для модели OrderItem
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()

    # Явно указываем классы разрешений для этого представления:
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer


# 24.07.2025 - Pr 10: Задание 1: Добавление filter_backends


# 24.07.2025 - Pr 10: Задание 3. Добавление эндпоинта для статистики. Часть 1
class OrderStatisticsView(APIView):
    # ВРЕМЕННО, чтобы с ТОКЕНОМ не морочиться:
    # authentication_classes = [BasicAuthentication]

    # Применяем наше новое разрешение и IsAuthenticated
    permission_classes = [IsAuthenticated, CanViewOrderStatistics]

    def get(self, request):
        total_orders = Order.objects.count()
        data = {
            'total_orders': total_orders,
        }
        return Response(data)

