# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 1: Сериалайзер для модели Category

from rest_framework import serializers
from .models import *
import re


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 2: Сериалайзер для модели Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 3: Сериалайзеры для модели Product
# Задание 3.1. Сериалайзер для получения данных

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'category', 'supplier', 'price', 'quantity', 'article', 'available']



# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 3: Сериалайзеры для модели Product
# Задание 3.2. Сериалайзер для создания и обновления данных

class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 4: Сериалайзеры для модели ProductDetail
# Задание 4.1 Сериалайзер для получения данных

class ProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductDetail
        fields = '__all__'


# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 4: Сериалайзеры для модели ProductDetail
# Задание 4.2. Сериалайзер для создания и обновления данных

class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        # fields = '__all__'
        fields = ['product', 'description', 'manufacturing_date', 'expiration_date', 'weight']


# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 5: Сериалайзер для модели Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 6: Сериалайзеры для модели Customer
# Задание 6.1. Сериалайзер для получения данных

class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Customer
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_joined', 'deleted', 'deleted_at']
        read_only_fields = ['date_joined', 'deleted', 'deleted_at']


# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 6: Сериалайзеры для модели Customer
# Задание 6.2. Сериалайзер для создания и обновления данных

class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    # 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
    # Задача 6: Сериалайзеры для модели Customer
    # Задание 6.3. Валидация номера телефона
    def validate_phone_number(self, value):
        if not re.match(r'^\d{10,15}$', value):
            raise serializers.ValidationError('Phone number must have from 10 to 15 numbers.')
        # if len(value) < 10 or len(value) > 15:
        #     raise serializers.ValidationError('Phone number must have from 10 to 15 numbers.')
        # if not value.isdigit():
        #     raise serializers.ValidationError('Phone number must be digit.')
        return value


# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 7: Сериалайзеры для модели Order
# Задание 7.1. Сериалайзер для получения данных

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)      # , many=True

    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['customer', 'order_date']
        read_only_fields = ['order_date']


# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 7: Сериалайзеры для модели Order
# Задание 7.2. Сериалайзер для создания и обновления данных

class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date']

# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 8: Сериалайзеры для модели OrderItem
# Задание 8.1. Сериалайзер для получения данных

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'

# 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
# Задача 8: Сериалайзеры для модели OrderItem
# Задание 8.2. Сериалайзер для создания и обновления данных

class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    # 17.07.2025 Lesson 29, Practice 7, Presentation - Les28-Django_Pr7.pdf
    # Задача 8: Сериалайзеры для модели OrderItem
    # Задание 8.3. Валидация количества товара
    def validate_quantity(self, value):
        if value > 1000:
            raise serializers.ValidationError('Quantity must be less than 1000.')
        return value

