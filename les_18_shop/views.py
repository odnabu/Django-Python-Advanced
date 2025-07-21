from django.shortcuts import render
from rest_framework import viewsets
from les_18_shop.models import Category, Supplier, ProductDetail, Address
from les_18_shop.serializers import CategorySerializer, SupplierSerializer, AddressSerializer


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


