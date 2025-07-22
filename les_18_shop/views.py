from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from les_18_shop.models import Category, Supplier, ProductDetail, Address, Customer, Order, OrderItem
from les_18_shop.serializers import (CategorySerializer, SupplierSerializer,
                                     AddressSerializer,
                                     CustomerSerializer, CustomerCreateUpdateSerializer,
                                     OrderSerializer, OrderCreateUpdateSerializer,
                                     OrderItemSerializer, OrderItemCreateUpdateSerializer)


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

    def get_serializer_class(self):
        # Для чтения данных:
        if self.request.method == 'GET':
            return ProductSerializer
        # Для изменения или удаления (PUT, PATCH, DELETE):
        return ProductCreateUpdateSerializer


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()

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


# 27.07.2025 - Pr 8: Задание 6: Представления и маршруты для модели Customer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()

    # Задание 9.2: Настройка фильтрации для модели Customer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer


# 27.07.2025 - Pr 8: Задание 7: Представления и маршруты для модели Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer


# 27.07.2025 - Pr 8: Задание 8: Представления и маршруты для модели OrderItem
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer


# 27.07.2025 - Pr 8: Задание 9: Добавление filter_backends


