# Link on GitHub: https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/urls.py

from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter

from library.views import create_genre, BookListCreateView, BookDetailUpdateDeleteView, \
    ExpensiveBooksView, GenreDetailUpdateDeleteView, GenreViewSet, \
    books_by_date_view, lazy_load_demo, create_book_and_publisher_view, \
    ProtectedDataView, PublicView, AdminView, \
    ReadOnlyOrAuthenticatedView, UserBookListView, \
    SimpleBookListCreateView        # , book_list_create, book_detail_update_delete,


router = DefaultRouter()
router.register('genres', GenreViewSet)

urlpatterns = [
    # _____ Через простые эндпоинты в методах типа book_list_create. _____
    # Для получения всех книг и создания новой книги:
    # path('books/', book_list_create, name='book-list-create'),
    # Для операций с одной книгой:
    # path('books/<int:pk>/', book_detail_update_delete, name='book-detail-update-delete'),
    # Маршрут для создания жанра:
    # path('genres/', create_genre, name='create-genre'),
    # Для получения всех книг и создания новой книги:
    # path('books/', BookListCreateView.as_view(), name='book-list-create'),
    # Для операций с одной книгой:
    # path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),

    # _____ Через ViewSet's _______________________________________________
    # Для получения всех книг и создания новой книги:
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    # Для операций с одной книгой:
    path('books/<int:pk>', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),
    path('books/expensive', ExpensiveBooksView.as_view(), name='book-expensive'),
    # Маршруты для создания жанра, его редактирования, удаления:
    # path('genres', create_genre, name='create-genre'),
    # path('genres/<str:name>', GenreDetailUpdateDeleteView.as_view(), name='genre-detail-update-delete'),

    path('', include(router.urls)),
    re_path(r'^books/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', books_by_date_view, name='books-by-date'),
    path('lazy_load/', lazy_load_demo, name='lazy-load-demo'),
    # _____  ТРАНЗАКЦИЯ  _____
    path('books/transaction', create_book_and_publisher_view, name='create-book-and-publisher'),

    path('user-books/', UserBookListView.as_view(), name='user-book-list'),
    path('protected/', ProtectedDataView.as_view(), name='protected-data'),
    path('public/', PublicView.as_view(), name='public-data'),
    path('for-admin/', AdminView.as_view(), name='admin-data'),
    path('read-anon/', ReadOnlyOrAuthenticatedView.as_view(), name='read-anon'),
    path('simple-books/', SimpleBookListCreateView.as_view(), name='simple-book-liste-create'),
]
