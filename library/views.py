# Link on GitHub: https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/views.py

from datetime import datetime
from django.db.models import Avg, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, action
from rest_framework.exceptions import NotFound
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView, ListAPIView)
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser,
                                        IsAuthenticatedOrReadOnly, DjangoModelPermissions)
from rest_framework.response import Response
from rest_framework import status, filters, mixins
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from django.db import reset_queries, connection, transaction

from library.models import Book, Genre, Publisher, SimpleBook
from library.permissions import IsOwnerOrReadOnly, CanGetGenresStatisticPermission
from library.serializers import (BookSerializer, BookDetailSerializer,
                                 # BookListSerializer,
                                 BookCreateSerializer, GenreSerializer, SimpleBookSerializer)



#
class ReadOnlyOrAuthenticatedView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({"message": "This is readable by anyone, but modifiable only by authenticated users."})

    def post(self, request):
        # Этот метод будет доступен только аутентифицированным пользователям:
        return Response({"message": "Data created by authenticated user."})


#
class AdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "Hello, Admin!"})



#
class PublicView(APIView):
    permission_classes = [AllowAny]

    # ??????????????????? format=None
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK, data={'message': 'This endpoint has access for anyone!'})


#
class ProtectedDataView(APIView):
    # Указываем, какие классы аутентификации использовать для этого представления.
    # Здесь мы явно переопределяем или подтверждаем BasicAuthentication.
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [TokenAuthentication]

    # Если JWTAuthentication установлен как DEFAULT_AUTHENTICATION_CLASSES,
    # здесь можно просто указать разрешения. DRF сам проверит токен.

    # Указываем, какие классы разрешений использовать.
    # IsAuthenticated означает, что только аутентифицированные пользователи имеют доступ.
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Если запрос дошел сюда, значит, пользователь аутентифицирован и авторизован.
        # request.user теперь содержит объект пользователя.
        return Response({'message': f'Hello, authenticated user {request.user.username}!',
                         'user': request.user.username})


# \\\\\\\\   @api_view   /////////////////////////////////////////////////////////////////////

# ___  Декоратор @api_view  ___
# Les22-Django_22-REST_p1_Serializer-26_06.pdf, pp. 46-52.
# Позволяет легко создавать Function-Based
# Views для обработки различных типов HTTP запросов.
#   ● Используется для определения типов HTTP-запросов.
#   ● Автоматически преобразует функцию в View.
# Принимает список методов, таких как GET, POST, PUT, PATCH, DELETE
# Упрощает создание API, автоматически обрабатывая многие задачи.


# See   Les22-Django_22-REST_p1_Serializer-26_06.pdf, page 60.
# @api_view(['GET', 'POST'])
# def book_list_create(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookListSerializer(books, many=True)       # ГДЕ:
#         #   books - Данные, которые будут сериализироваться - массив со всеми книгами.
#         #   many=True - Подтверждение того, что это массив.
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookCreateSerializer(data=
#         # 2. Проверяем, корректны ли данные. Если нет - вызовется исключение:
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# serializer.is_valid()
# 🔹 Проверяет, корректны ли входные данные, которые сериализатор получил
#    (например, из POST-запроса).
# 🔹 Выполняет всю валидацию, включая:
#       - проверку типов данных,
#       - обязательных полей,
#       - ограничений (max_length, unique и т.д.),
#       - кастомных validate_ методов.
#     Возвращает:
#       - True, если всё ок,
#       - False, если данные невалидные.
#
# raise_exception=True
# 🔹 Говорит DRF: если данные не прошли валидацию — сразу выбросить
#    исключение ValidationError.
# 🔹 DRF автоматически обработает это исключение и вернёт клиенту
#    красивый JSON-ответ с кодом 400 Bad Request.


# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail_update_delete(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = BookDetailSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = BookCreateSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response({'message': 'Book deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


#
@api_view(['POST'])
def create_genre(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Возвращаем ошибки, если данные некорректны:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
@api_view(['GET'])
def books_by_date_view(request, year=None, month=None, day=None):
    # Django автоматически передает захваченные 'year', 'month', 'day' в функцию:
    books = Book.objects.filter(publication_date__year=year,
                                publication_date__month=month,
                                publicztion_dat__day=day)
    serializer = BookSerializer(books, many=True)
    return Response({'date': f"{year}-{month}-{day}", 'books': serializer.data})


#
@api_view(['GET'])
def lazy_load_demo(request):
    # Endpoint for testing lazy load.
    reset_queries()

    # ___  NB!  ____________________
    # Этот код ОЧЕНЬ НЕЭФФЕКТИВЕН!
    # 1-й запрос: получить ВСЕ книги:
    # books = Book.objects.all()
    # _______________________________

    # Оптимизация с помощью select_related:
    books = Book.objects.select_related('publisher').all()      # 🔶 Всего ОДИН запрос!
    print(connection.queries)
    for book in books:
        # Для КАЖДОЙ книги делается ОТДЕЛЬНЫЙ запрос к БД, чтобы получить издателя:
        print(book.publisher.name)      # N дополнительных запросов.
    print(connection.queries)
    print("#" * 100)
    reset_queries()

    # Оптимизация с помощью prefetch_related:
    books = Book.objects.prefetch_related('genres').all()        # 🔶 Всего ДВА запроса!
    for book in books:
        print("Book: ", book.title)
        # Доступ к book.genres.all() теперь НЕ вызывает новых запросов:
        for genre in book.genres.all():
            print("   - Genre: ", genre.name)
    print(connection.queries)
    print("#" * 100)
    reset_queries()

    books = Book.objects.select_related('publisher').prefetch_related('genres').all()    # 🔶 Все еще 2 запроса!
    for book in books:
        print("Book: ", book.title)
        print(book.publisher.name)
        # Доступ к book.genres.all() теперь не вызывает новых запросов:
        for genre in book.genres.all():
            print("   - Genre: ", genre.name)
    print(connection.queries)

    return Response({"data": 'Success!'})



# _____  ТРАНЗАКЦИЯ  в  методе POST  _____
# Создание КНИГИ и ИЗДАТЕЛЯ.
@api_view(['POST'])
def create_book_and_publisher_view(request):
    try:
        # Все, что находится внутри этого блока, — одна ТРАНЗАКЦИЯ:
        with transaction.atomic():
            # 1. Создаем издателя:
            publisher = Publisher.objects.create(name="Super Publisher", established_date=datetime.now())
            # Искусственно создадим ошибку, чтобы проверить откат:
            if not request.data.get('title'):
                raise ValueError("The NAME of the Book is obligate!")

            # 2. Создаем книгу:
            # Этот код не выполнится, если возникнет ошибка выше
            book = Book.objects.create(
                title=request.data.get('title'),
                publisher=publisher
            )
        # Если блок with завершился без ошибок, транзакция фиксируется (commit).
    except Exception as e:
        # Если внутри блока with произошла любая ошибка, все изменения в БД
        # (создание Publisher) будут отменены (rollback):
        return Response({'error': str(e)}, status=400)

    return Response({'status': 'Book and Publisher are created.'})



# _____  ТРАНЗАКЦИЯ  в  ДЕКОРАТОРЕ  @transaction.atomic  _____
# Создание КНИГИ и ИЗДАТЕЛЯ.
@api_view(['POST'])
@transaction.atomic     # Декоратор применяет транзакцию ко всей функции!
def create_book_and_publisher_view(request):
    try:
        # 1. Создаем издателя:
        publisher = Publisher.objects.create(name='Name of a new Publisher')

        # 2. Создаем книгу:
        book = Book.objects.create(
            title='A new Book',
            publisher=publisher
        )

        # ... другая логика ...

    except Exception as e:
        # Если здесь произойдет ошибка, вся транзакция будет отменена
        # и ни книга, ни издатель не будут сохранены в БД.
        return Response({'error': str(e)}, status=400)

    seriralizer = BookSerializer(book)
    return Response(seriralizer.data)




# \\\\\\\\   APIView   /////////////////////////////////////////////////////////////////////

# See   Les24-Django_24-REST_p2-14_07-pyth_25.pdf, page 58, 60.
# Представление для списка и создания объектов модели Book через APIView:
# class BookListCreateView(APIView, PageNumberPagination):
#     page_size = 2
#
#     # ПЕРЕопределение метода GET для представления списка и создания объектов модели Book:
#     def get(self, request):
#
#         # _____  Filter  _____
#         filters = {}
#         title = request.query_params.get('title')
#         published_year = request.query_params.get('pub_year')
#         if title:
#             filters['title'] = title
#         if published_year:
#             filters['published_year'] = published_year
#
#         books = Book.objects.filter(**filters)
#
#         # _____  Sorting  _____
#         # Получаем параметр 'sort_by'. Если его нет, по умолчанию сортируем по 'title':
#         sort_by = request.query_params.get('sort_by', 'title')
#         # Получаем параметр 'sort_order'. По умолчанию сортируем по возрастанию ('asc'):
#         sort_order = request.query_params.get('sort_order', 'asc')
#         # Если порядок сортировки 'desc' (убывание)... :
#         if sort_order == 'desc':
#             # ...добавляем минус перед именем поля для убывающей сортировки:
#             sort_by = f'-{sort_by}'
#         # Применяем сортировку:
#         books = books.order_by(sort_by)
#
#         # _____  Pagination  _____
#         requested_page_size = self.get_page_size(request)
#         self.page_size = requested_page_size
#         result = self.paginate_queryset(books, request, view=self)
#
#         serializer = BookListSerializer(result, many=True)
#         return self.get_paginated_response(serializer.data)
#
#     def get_page_size(self,request):
#         page_size_param = request.query_params.get('page_size')
#         if page_size_param and page_size_param.isdigit():
#             return int(page_size_param)
#         return self.page_size
#
#     # ПЕРЕопределение метода POST для представления списка и создания объектов модели Book:
#     def post(self, request):
#         serializer = BookCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # Представление для одного объекта (чтение, обновление, удаление):
# class BookDetailUpdateDeleteView(APIView):
#
#     # Переопределение метода получения данных из БД:
#     def get(self, request, pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookDetailSerializer(book)
#         return Response(serializer.data)
#
#     # Переопределение метода корректирования данных в БД:
#     def put(self, request, pk):
#         try:
#             book = Book. objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookCreateSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # Переопределение метода удаления данных из БД:
#     def delete(self, request, pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# \\\\\\\\   GenericAPIView   /////////////////////////////////////////////////////////////////////

# Представление для списка и создания объектов модели Book через GenericAPIView:
#   Les27-Django_25-REST_p3-16_07.pdf:
#       - GenericAPIView - s. 7.
#       - class BookListView(GenericAPIView) - s. 12.
# class BookListCreateView(GenericAPIView):
#     # 1. Указываем, что мы работаем со всеми объектами модели Book:
#     queryset = Book.objects.all()
#     # 2. Указываем, что для преобразования будем использовать BookSerializer:
#     serializer_class = BookSerializer
#
#     # ___ Метод для обработки GET-запроса (получение списка):
#     def get(self, request, *args, **kwargs):
#         # 1. Получаем набор всех книг с помощью встроенного метода:
#         queryset = self.get_queryset()
#         # 2. Сериализуем набор объектов (many=True указывает, что объектов много):
#         serializer = self.get_serializer(queryset, many=True)
#         # 3. Возвращаем ответ в формате JSON:
#         return Response(serializer.data)
#
#     # ___ Метод для обработки POST-запроса (создание объекта):
#     def post(self, request, *args, **kwargs):
#         # 1. Передаем данные из запроса в сериализатор:
#         serializer = self.get_serializer(data=request.data)
#         # 2. Проверяем, корректны ли данные. Если нет - вызовется исключение:
#         serializer.is_valid(raise_exception=True)
#         # 3. Сохраняем новый объект в базу данных:
#         serializer.save()
#         # 4. Возвращаем созданный объект и статус 201 CREATED:
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



# Представление для одного объекта (чтение, обновление, удаление):
# class BookDetailUpdateDeleteView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     # Метод для обработки GET-запроса (получение одного объекта):
#     def get(self, request, *args, **kwargs):
#         # 1. Получаем один конкретный объект по его pk (id) из URL:
#         book = self.get_object()
#         # 2. Сериализуем его:
#         serializer = self.get_serializer(book)
#         # 3. Возвращаем ответ:
#         return Response(serializer.data)
#
#     # Метод для обработки PUT-запроса (полное обновление):
#     def put(self, request, *args, **kwargs):
#         # 1. Получаем один конкретный объект по его pk (id) из URL:
#         book = self.get_object()
#         # 2. Сериализуем его:
#         serializer = self.get_serializer(book, data=request.data)
#         # 3. Проверяем, корректны ли данные. Если нет - вызовется исключение:
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     # Метод для обработки PATCH-запроса (частичное обновление):
#     def patch(self, request, *args, **kwargs):
#         # 1. Получаем один конкретный объект по его pk (id) из URL:
#         book = self.get_object()
#         # partial=True говорит сериализатору, что обновление частичное:
#         serializer = self.get_serializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     # Метод для обработки DELETE-запроса (удаление):
#     def delete(self, request, *args, **kwargs):
#         # 1. Получаем один конкретный объект по его pk (id) из URL:
#         book = self.get_object()
#         book.delete()
#         # Возвращаем пустой ответ со статусом 204 NO CONTENT:
#         return Response(status=status.HTTP_204_NO_CONTENT)





# \\\\\\\\   PAGINATION   /////////////////////////////////////////////////////////////////////

# Создаем свой класс пагинации:
class BookPagination(PageNumberPagination):
    page_size = 3                           # Количество элементов на странице по умолчанию.
    page_size_query_param = 'page_size'     # Имя параметра в URL для задания размера страницы.
    max_page_size = 100                     # Максимальное количество элементов на странице.


# 1. Настраиваем класс пагинации:
class BookCursorPagination(CursorPagination):
    page_size = 5
    # __ ВАЖНО __ нужно указать поле для сортировки:
    ordering = 'publication_date'



# \\\\\\\\   Generic Views  /////////////////////////////////////////////////////////////////////

# Смотри общую информацию по Views в Les24-Django_24-REST_p2-14_07-pyth_25.pdf, с. 31-37 "Class-Based Views".
# ___ Class-Based Views (CBV) - подход к созданию представлений DRF, в котором представления
#     реализуются как классы. CBV обеспечивают объектно-ориентированный подход,
#     позволяя лучше структурировать, расширять и переиспользовать код.
# CBV делятся на несколько категорий, от базовых до высокоуровневых.
# Каждая категория предоставляет различные уровни абстракции и функциональности для создания представлений.
# ___ Категории Class-Based Views:
#       💢 БАЗОВАЯ - Низкоуровневая.
#           🔷 APIView: Основной класс для создания CBV.
#                  Предоставляет методы для обработки HTTP-запросов.
#                  Создание кастомных представлений с нуля, требующих специфической логики обработки запросов.
#       💢 GenericAPIView и Миксины - Средний Уровень.
#           🔷 GenericAPIView: Расширяет APIView и добавляет базовую функциональность.
#                   Создание представлений с расширенными возможностями, требующих дополнительной
#                   функциональности без написания большого количества кода.
#           🔷 Mixin-s:  Вспомогательные классы, добавляющие функциональность CRUD к представлениям (Средний Уровень).
#                   Комбинация миксинов с GenericAPIView для быстрого создания представлений с операциями CRUD.
#       💢 Generic Views - Высокоуровневая.
#           🔷 Generic Views: Представления, которые объединяют GenericAPIView и миксины для предоставления часто
#                   используемых шаблонов представлений.
#                   Позволяют быстро создавать стандартные представления CRUD, не требуя явного написания методов для
#                   обработки запросов.
#                   ВИДЫ Generic Views:
#                       1. ListAPIView - Получение списка объектов.
#                       2. CreateAPIView - Создание нового объекта.
#                       3. RetrieveAPIView - Получение одного объекта.
#                       4. UpdateAPIView - Обновление существующего объекта.
#                       5. DestroyAPIView - Удаление объекта.
#                       6. __ListCreateAPIView__ - Комбинирует возможности получения списка и создания объекта.
#                       7. RetrieveUpdateAPIView - Комбинирует возможности получения и обновления объекта.
#                       8. RetrieveDestroyAPIView - Комбинирует возможности получения и удаления объекта.
#                       9. RetrieveUpdateDestroyAPIView - Комбинирует возможности получения, обновления и удаления объекта.
#                   "Generic Views" детально по видам - Les24-Django_24-REST_p2-14_07-pyth_25.pdf, с. 36.
#           🔷 ViewSets:
#                   ВИДЫ:
#                       1. ModelViewSet - Полный набор операций CRUD. ModelViewSet объединяет
#                          все generic-представления и миксины для создания полнофункциональных наборов представлений.
#                          Создание полных CRUD представлений для моделей с минимальной конфигурацией.
#                       2. ReadOnlyModelViewSet - Только операции чтения (retrieve - один объект и list).
#                          Для представлений, где не требуется создавать, обновлять или удалять объекты, а только читать данные.


# BookListCreateView on ListCreateAPIView класс заменяет уже существующий BookListCreateView, который был создан выше сначала в APIView,
# а потом в GenericAPIView, и впоследствии закомментирован.
# Теперь этот класс наследуется от ListCreateAPIView из rest_framework.generics, который уже умеет:
#   - обрабатывать GET для получения списка (List)
#   - обрабатывать POST для создания объекта (Create)
class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # pagination_class = BookPagination         # Вот здесь мы и подключаем пагинацию.
    # pagination_class = LimitOffsetPagination    # Просто подключаем встроенный класс пагинации.
    pagination_class = BookCursorPagination

    # Подключаем бэкенды для фильтрации, поиска и сортировки:
    filters_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Поля, по которым можно будет точно фильтровать (author=...):
    filters_fields = ['author', 'genres']
    # Поля, по которым будет работать полнотекстовый поиск (search=...):
    search_fields = ['title', 'description']
    # Поля, по которым можно будет сортировать (ordering=...):
    ordering_fields = ['publication_date', 'price']

    # ___ AUTHENTICATION ___
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ПЕРЕопределение метода создания объекта Book:
    def perform_create(self, serializer):
        # При сохранении объекта мы передаем дополнительный параметр owner,
        # в который записываем текущего пользователя из запроса.
        serializer.save(owner=self.request.user)

    # Переопределяем метод create:
    def create(self, request, *args, **kwargs):
        # Копируем данные из запроса, чтобы их можно было изменять:
        data = request.data.copy()
        # Наша кастомная логика:
        if 'author' not in data or not data['author']:
            data['author'] = 1
        # Дальше идет стандартная логика из DRF:
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create вызывает serializer.save():
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



# Класс BookDetailUpdateDeleteView on RetrieveUpdateDestroyAPIView заменяет класс BookDetailUpdateDeleteView
# выше в коде, который был сделан на основе GenericAPIView.
# Теперь класс наследуется от RetrieveUpdateDestroyAPIView из rest_framework.generics, который Умеет:
#   - обрабатывать GET для получения одного объекта (Retrieve)
#   - обрабатывать PUT/PATCH для обновления (Update)
#   - обрабатывать DELETE для удаления (Destroy)
class BookDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsOwnerOrReadOnly]

    # # Переопределяем стандартный метод получения объекта:
    # def get_object(self):
    #     # Сначала получаем pk из URL, как обычно:
    #     pk = self.kwargs.get('pk')
    #
    #     try:
    #         # Ищем объект, который соответствует pk И НЕ является забаненным:
    #         book = Book.objects.get(pk=pk, is_banned=False)
    #     except Book.DoesNotExist:
    #         # Если книга не найдена или забанена, вызываем ошибку 404:
    #         raise NotFound(detail=f"Book with id '{pk}' not found or is banned.")
    #
    #     return book

    # ===  Атрибут serializer_class:
    # Les27-Django_25-REST_p3-16_07.pdf, pp. 8, 14.
    # Указывает класс сериализатора, который будет использоваться для
    # преобразования данных между объектами Python и JSON
    # Использование:
    #   ● Указывается напрямую как атрибут класса.
    #   ● Можно переопределить метод get_serializer_class().
    # ===  Метод get_serializer_context()
    # Les27-Django_26-REST_p3-16_07.pdf, p. 22, 29.
    # Используется для предоставления контекста сериализатору.
    # Контекст позволяет сериализатору иметь доступ к дополнительной информации.
    # Метод get_serializer_context() позволяет адаптировать представление данных
    # в зависимости от условий запроса или других факторов, передаваемых через
    # контекст. Это делает API более динамичным и адаптивным.
    def get_serializer_context(self):
        # Получаем стандартный контекст:
        context = super().get_serializer_context()
        # Добавляем в него флаг из параметров запроса:
        context['include_related'] = self.request.query_params.get('include_related', 'false')
        return context



#
class GenreDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    # Говорим DRF искать объект по полю 'name' в модели Genre:
    lookup_field = 'name'

    # Этот атрибут не обязателен, если имя в URL совпадает с lookup_field,
    # но для ясности лучше его указать.
    lookup_url_kwarg = 'name'


#
class SimpleBookListCreateView(ListCreateAPIView):
    queryset = SimpleBook.objects.all()
    serializer_class = SimpleBookSerializer


# \\\\\\\\   ViewSets  /////////////////////////////////////////////////////////////////////

# #
# class GenreReadOnlyView(ReadOnlyModelViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#



#
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # +++ Используем встроенный класс разрешений:
    permission_classes = [DjangoModelPermissions, CanGetGenresStatisticPermission]

    # Новый кастомный метод:
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """
        Возвращает количество книг для каждого жанра.
        """
        # С помощью annotate добавляем к каждому жанру поле book_count:
        genres_with_book_counts = Genre.objects.annotate(book_count=Count('book'))
        # Формируем данные для ответа:
        data = [
            {
                "id": genre.id,
                "genre": genre.name,
                "book_count": genre.book_count
            }
            for genre in genres_with_book_counts
        ]
        return Response(data)




# \\\\\\\\   Mixins  /////////////////////////////////////////////////////////////////////

# #
# class GenreListRetrieveUpdateViewSet(mixins.ListModelMixin,
#                                      mixins.RetrieveModelMixin,
#                                      mixins.UpdateModelMixin,
#                                      GenericViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Класс для получения дорогих книг с переопределением метода list.
# Les27-Django_25-REST_p3-16_07.pdf, sl. 51-52.
class ExpensiveBooksView(ListAPIView):
    serializer_class = BookSerializer
    # Мы не указываем queryset, т.к. будем формировать его динамически.
    # Вместо этого мы полностью переопределяем метод get_queryset:
    def get_queryset(self):
        # 1. Вычисляем среднюю цену всех книг:
        average_price = Book.objects.aggrigate(avg_price=Avg('price'))['avg_price']
        if average_price is None:
            # Возвращаем пустой набор, если книг нет:
            return Book.objects.none()
        # 2. Возвращаем книги, цена которых выше средней:
        return Book.objects.filter(price__gt=average_price)



#
# Les35-Django_31-AuTHORisation_1-24_07.pdf, sl. 9.
class UserBookListView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # ПЕРЕопределение метода получения данных из БД:
    def get_queryset(self):
        """
        Метод определяет набор данных.
        Мы переопределяем его, чтобы вернуть книги, отфильтрованные по
        текущему пользователю.
        """
        # Фильтруем книги по полю owner:
        return Book.objects.filter(owner=self.request.user)



