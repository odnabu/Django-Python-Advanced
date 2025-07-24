# 27.07.2025 - Pr 8: Задание 1: Представления и маршруты для модели Category

from rest_framework.routers import DefaultRouter
from django.urls import path, include

from les_18_shop.views import CategoryViewSet, SupplierViewSet, ProductListCreateView, ProductRetrieveUpdateDestroyView, \
    ProductDetailViewSet, AddressViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet, OrderStatisticsView

# Создаем экземпляр роутера:
router = DefaultRouter()

# Регистрируем наш ViewSet.
# 'category' - это префикс URL, по которому будут доступны наши категории.
# CategoryViewSet - представление, которое будет обрабатывать запросы.
router.register('category', CategoryViewSet)

# 27.07.2025 - Pr 8: Задание 2: Представления и маршруты для модели Supplier
router.register('supplier', SupplierViewSet)


# 27.07.2025 - Pr 8: Задание 3: Представления и маршруты для модели Product
# Пути нельзя добавить в router, потому что ProductListCreateView(ListCreateAPIView). Поэтому добавляются они сразу в urlpatterns.

# 27.07.2025 - Pr 8: Задание 3: Представления и маршруты для модели ProductDetail
router.register('product-detail', ProductDetailViewSet)

# 27.07.2025 - Pr 8: Задание 5: Представления и маршруты для модели Address
router.register('address', AddressViewSet)

# 27.07.2025 - Pr 8: Задание 6: Представления и маршруты для модели Customer
router.register('customer', CustomerViewSet)

# 27.07.2025 - Pr 8: Задание 7: Представления и маршруты для модели Order
router.register('order', OrderViewSet, basename='order')

# 27.07.2025 - Pr 8: Задание 8: Представления и маршруты для модели OrderItem
router.register('order-item', OrderItemViewSet)

# Основной список маршрутов нашего приложения.
# Мы просто включаем в него все URL, которые сгенерировал роутер.
urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    # 24.07.2025 - Pr 10: Задание 3. Добавление эндпоинта для статистики. Часть 1
    path('order-statistics/', OrderStatisticsView.as_view(), name='order-statistics'),
]

