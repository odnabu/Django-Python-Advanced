# Link on GitHub: https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/serializers.py

from rest_framework import serializers
from django.utils import timezone
from library.models import Book, Publisher, Genre, SimpleBook
from library.validators import validate_title_length



# \\\\\   Сериализатор в Django REST Framework?   /////
# 🔹 Сериализатор — это «переводчик» между сложными объектами,
# (например, Django-моделями) и простыми структурами данных (словарями, JSON).
# Он умеет:
#   - Преобразовывать модель → JSON (для отдачи ответа клиенту).
#   - Преобразовывать JSON → объект модели (для создания/обновления).
#   - Проверять входные данные (валидация).



# # ----------------------------------------------------------------
# # ЗАКОММЕНТИРОВАТЬ весь этот сериалайзер!!!!!!!!!!!!!!!!!!!!
# # See Les22-Django_22-REST_p1_Serializer-26_06.pdf, page 60.
# # Используется для сериализации массива книг:
# class BookListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         # Сокращенные поля для списка книг:
#         fields = ['id', 'title', 'author']
# # ----------------------------------------------------------------




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Сериалайзер добавления в БД ИЗДАТЕЛЯ.
class PublisherSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Publisher
        fields = '__all__'



# Сериалайзер добавления в БД НОВОЙ  КНИГИ.
# Посяснения от Chat смотри тут: https://chatgpt.com/s/t_68b92bdab62081919079199a9896988e.
class BookCreateSerializer(serializers.ModelSerializer):
    """
    Creating a new Book with validations of the title.
    """
    # created_at = serializers.DateTimeField(read_only=True)

    # Явно объявляем поле title и вешаем кастомный валидатор validate_title_length
    # (функция вне сериализатора). Он сработает до методов validate_* внутри сериализатора:
    title = serializers.CharField(validators=[validate_title_length])

    # Числовое поле. Если в модели тип Integer/PositiveInteger — это просто «поверх» модельного поля,
    # чтобы задать/переопределить поведение (messages, required и т.п.):
    amount_pages = serializers.IntegerField()

    # SlugRelatedField — это связь «по слагу», а не по первичному ключу:
    publisher = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Publisher.objects.all(),       # Writeable slug-based relation.
    )
    #   - Вход (write): в запросе клиент присылает строку со значением поля slug издателя
    #     (например, "penguin-books"). DRF ищет объект Publisher по slug=... в переданном queryset.
    #   - Выход (read): в ответе сериализатор вернёт строку-слаг (а не объект, и не id).
    #   - Рекомендуется, чтобы Publisher.slug был уникальным — иначе при записи DRF не сможет однозначно найти объект.

    # Коротко про SlugRelatedField:
    #   - Делает внешний ключ «по строке» (slug), а не по id.
    #   - Требует queryset= для записи.
    #   - В ответах сериализует сам slug.
    #   - Хорош, когда хотите читаемые URL-совместимые значения в API и стабильную ссылку на связанные объекты.

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['created_at', 'id']
        #   - fields='__all__' — берём все поля модели.
        #   - read_only_fields — клиент не может присылать эти поля; но вы можете задавать их на сервере (как ниже в create), и они будут выводиться.

    # --- CREATE ---
    # Переопределение метода создания книги: добавление серверного значения created_at,
    # так как поле read-only и пользователь его не присылает.
    def create(self, validated_data):
        # сервер сам ставит created_at, т.к. в Meta поле было скрыто от клиента read_only:
        validated_data['created_at'] = timezone.now()
        # super() вызывает "родительскую" реализацию create() у ModelSerializer
        return super().create(validated_data)
        # Зачем super()?
        # ModelSerializer.create() внутри DRF аккуратно создаёт модель:
        # делает instance = Model.objects.create(**validated_data) + корректно обрабатывает многие аспекты
        # (в т.ч. M2M после instance.save() и т.д.).
        # Мы лишь «вклиниваемся», добавляем своё поле, а всю стандартную механику отдаем «родителю».


    # super() — это встроенная функция Python, которая позволяет обратиться к
    # методу родительского класса. Chat: https://chatgpt.com/s/t_68b7dfc273ac8191861c755617c7add3
    # В сериалайзерах DRF super() обычно используется, когда мы переопределяем методы
    # сериалайзера, например:
    #   create()
    #   update()
    #   validate()
    #   to_representation()
    # 🔍 Здесь super().create(validated_data):
    #   1) берёт готовые данные,
    #   2) вызывает стандартную реализацию метода create у ModelSerializer,
    #   3) и автоматически создаёт объект в базе.
    # Мы лишь "вклинились", добавив created_at.
    # ✨ Итого:
    #   + super() в сериалайзерах DRF позволяет не переписывать заново логику, которая уже реализована в ModelSerializer (сохранение объекта, обновление, базовая валидация).
    #   + Ты добавляешь свою кастомную логику до или после вызова родительского метода.
    #   + Без super() пришлось бы вручную копировать весь код из DRF.

    # --- UPDATE ---
    # Перед обновлением «нормализуем» заголовок (обрезаем пробелы, приводим к Title Case):
    def update(self, instance, validated_data):
        # Мягкая нормализация только если поле пришло:
        if 'title' in validated_data:
            # Дополнительная логика: проверяем название книги и удаляем пробелы (или другие указанные символы)
            # в НАЧАЛЕ и в КОНЦЕ строки:
            validated_data['title'] = validated_data['title'].strip().title()
        return super().update(instance, validated_data)
        # super().update(...) выполнит стандартное обновление атрибутов и instance.save().

    # ==============================================================================
    # Ключевая мысль про super(): расширяем, а не переписываем базовую логику DRF.
    # Это избавляет от дублирования кода и ошибок.
    # ==============================================================================


    # \\\\\   Валидаторы  /////

    # --- field-level validation ---
    # Полевой валидатор: DRF вызовет этот метод только для поля amount_pages и передаст одно значение value:
    def validate_amount_pages(self, value):
        if value < 1:
            raise serializers.ValidationError("Amount of Pages can't be less then 1.")
        return value

    # --- object-level validation (кросс-полевая) ---
    # ⚠️ Здесь есть ошибка сигнатуры.
    # def validate_discount_price(self, data):
    #     if data.get('discount_price') and data.get('price'):
    #         if data['discount_price'] > data['price']:
    #             raise serializers.ValidationError("Discounted price can't be higher then regular price.")
    #     return data
        # Метод с именем validate_<fieldname> должен выглядеть как
        #   def validate_discount_price(self, value):
        #   и валидировать только одно поле.
        # Но вы сверяете два поля (discount_price и price) — это сквозная (object-level) валидация.
        # Для неё нужен метод:
        #   def validate(self, attrs):
        #       # здесь доступны все поля сразу:
        #       ...
        # Иначе DRF передаст сюда одно значение, и data.get(...)  __РУХНЕТ__.

    # ИСПРАВЛЕННЫЙ кросс-полевой валидатор:
    def validate(self, attrs):
        price = attrs.get('price', getattr(self.instance, 'price', None))
        discount = attrs.get('discount_price', getattr(self.instance, 'discount_price', None))

        if discount is not None and price is not None and discount > price:
            raise serializers.ValidationError(
                {"discount_price": "Discounted price can't be higher than regular price."}
            )
        return attrs
    # Почему так лучше:
    #   - Правильная кросс-полевая валидация (validate(self, attrs)),
    #      работает и для POST, и для PATCH (мы подхватываем значения из instance, если поле не пришло в частичном обновлении).
    #   - super() используется ровно там, где должен — мы добавляем своё поведение и доверяем DRF рутину создания/обновления.
    #   - SlugRelatedField остаётся записываемым: на вход — слаг, на выход — слаг.

    # =================================================================
    # https://chatgpt.com/s/t_68b92d902f4481919b3bb58b38d2450d
    # \\\\\\\  instance в методах сериализатора  ///////
    # Когда ты переопределяешь update(self, instance, validated_data), то:
    # instance — это объект модели, который уже существует в БД и его нужно обновить.
    # Например, если в базе есть книга с id=5, то при запросе PUT /books/5/ DRF достанет её
    # из базы и передаст сюда в параметре instance.
    # 👉 то есть instance — это старое состояние объекта, до изменений.
    # 👉 а validated_data — это новые данные из запроса (уже прошедшие валидацию).

    # \\\\\\  Можно ли поменять имена параметров?  ///////
    # Технически да 😅
    #   - Python не требует именно instance или attrs.
    #   - Важно только, чтобы позиция аргумента совпадала.
    # Например, можно написать:
    # def update(self, obj, new_data):
    #     ...
    # И всё будет работать.
    #
    # Но 👇
    #   - instance и validated_data — это де-факто стандартные имена, их придерживается
    #     Django REST Framework.
    #   - То же самое с attrs в validate.
    #   - Если поменять, код станет менее читаемым для других разработчиков (и для тебя самой через пару месяцев 🙃).
    # ✅ Поэтому лучше придерживаться именно этих имён.
    # Это не магия и не зарезервированные слова, но это стандарт, чтобы всем было понятно без лишних вопросов.
    # =================================================================

    # ==============================================================================
    # https://chatgpt.com/s/t_68bd20d5fb58819180ace0aceeec6ad6

    # \\\\\\   SLUG  ///////
    # Slug — это “человекочитаемый” идентификатор объекта, обычно используемый в URL.
    # 🔹 В переводе с английского slug — «пуля, снаряд», но в веб-разработке это слово
    # стало означать короткий текстовый ярлык, который удобно вставлять в адрес ссылки.
    #   Пример:
    #       У тебя есть статья с заголовком:
    #       "10 советов, как учить Python"
    #       Для URL тебе лучше использовать что-то короткое и удобное:
    #       https://example.com/articles/10-sovetov-kak-uchit-python
    #   Вот эта часть 10-sovetov-kak-uchit-

    # \\\\\\   Для чего нужен  SLUG  ///////
    # 1. SEO — поисковым системам легче индексировать и понимать адреса.
    #   /article/15
    #       менее понятен, чем
    #   /article/kak-uchit-python
    # Удобство пользователя — читатель сразу понимает, о чём страница.
    # Уникальность — обычно slug делают уникальным в пределах таблицы
    # (например, для постов в блоге).
    # 2. В Django:
    # В моделях часто есть поле SlugField, например:
    #       from django.db import models
    #       from django.utils.text import slugify
    #
    #       class Article(models.Model):
    #           title = models.CharField(max_length=200)
    #           slug = models.SlugField(unique=True, blank=True)
    #
    #           def save(self, *args, **kwargs):
    #               if not self.slug:
    #                   # автоматически создаём slug из title:
    #                   self.slug = slugify(self.title)
    #               super().save(*args, **kwargs)
    # Здесь slugify("10 советов, как учить Python") превратит строку в:
    #   10-sovetov-kak-uchit-python

    # Как slug используется на практике в Django-роутах, например, для доступа к статьям
    # через slug, а не через id: https://chatgpt.com/s/t_68bd21f7d23c81918de7108bf6f07367.
    # ==============================================================================



# Сериалайзер для преобразования модель/JSON и переопределение ПРЕДСТАВЛЕНИЯ входных данных по КНИГЕ:
#   - модель: модель → JSON -для отдачи ответа клиенту.
# или
#   - JSON: JSON → объект модели - для создания/обновления.
class BookSerializer(serializers.ModelSerializer):
    """

    """
    # 📌 BookSerializer
    # Это «общий» сериализатор.
    # Он выводит все поля (fields='__all__), и в to_representation может убирать поле genres, если не передан флаг в context.
    # То есть он универсальный: иногда показывает меньше данных, иногда больше.

    class Meta:
        model = Book
        fields = '__all__'               # сериализуем все поля модели.
        read_only_fields = ['owner']     # Делаем поле 'owner' только для чтения.

    # Метод, который определяет, как объект модели будет отображён в JSON.
    # По умолчанию ModelSerializer делает это автоматически.
    # Но если нам нужно изменить вывод (например, скрыть какие-то поля),
    # мы можем переопределить to_representation.
    def to_representation(self, instance):
        # Получаем стандартное представление модели в виде словаря:
        representation = super().to_representation(instance)

        # Проверяем флаг, который мы передали из представления. По сути
        # проверяем, есть ли в контексте ключ 'include_related'.
        # Если его нет, то убираем поле 'genres' из JSON:
        if not self.context.get('include_related'):
            # Если флаг false, удаляем поле (ключ) 'genres' из ответа:
            representation.pop('genres', None)
        # возвращаем итоговое представление данных:
        return representation
        # Итог. Здесь логика такая:
        #   - По умолчанию сериализатор вернёт все поля (__all__).
        #   - Но если в context при инициализации сериализатора не передали
        #     include_related=True, то поле genres будет убрано из ответа.
        # 📌 Это удобно, если ты хочешь иногда отдавать данные с жанрами, а иногда — без (например, чтобы не грузить лишнюю инфу при списке книг).

    # ==============================================================================
    # https://chatgpt.com/s/t_68bd2abbdad88191ab3e5c50c2fc9537

    # \\\\\\   context у сериализатора  ///////
    # Когда ты создаёшь экземпляр сериализатора в DRF, ему можно передавать дополнительную информацию через аргумент context.
    # Это обычный словарь dict, в котором можно хранить всё, что тебе может пригодиться внутри сериализатора.
    # Например:
    #   - сам request (часто нужен для получения текущего пользователя),
    #   - какие-то параметры, влияющие на то, что показать/скрыть,
    #   - дополнительные флаги (include_related, expand, и т.п.).

    # \\\\\\   Где context используется по умолчанию  ///////
    # DRF автоматически передаёт в context объект request, если ты используешь
    # сериализатор через generic views или viewsets.
    # Например:
    #   serializer = BookSerializer(book, context={'request': request})
    # Теперь внутри сериализатора можно получить request:
    #   self.context['request']

    # \\\\\\   Как передать свой context?  ///////
    # Ты сама решаешь, что туда положить. Например, если хочешь управлять выводом genres:
    #   # пример в views.py
    #   def book_detail(request, pk):
    #       book = get_object_or_404(Book, pk=pk)
    #
    #       serializer = BookSerializer(
    #             book,
    #           context={'include_related': True}  # добавили наш флаг в контекст
    #       )
    #       return Response(serializer.data)
    # 📌 Теперь в методе to_representation сериализатора условие:
    #   if not self.context.get('include_related'):
    #         representation.pop('genres', None)
    # будет работать так:
    #   - если include_related=True, то genres останется в JSON;
    #   - если include_related не передали или он False → поле genres уберётся.
    # ✨ То есть "не передали" означает, что при создании сериализатора в аргумент
    # context={...} не добавили наш ключ include_related. В этом случае сериализатор
    # работает по умолчанию и скрывает genres.
    # ==============================================================================




# Сериалайзер для преобразования модель/JSON входных данных по КНИГЕ:
#   - модель: модель → JSON -для отдачи ответа клиенту.
# или
#   - JSON: JSON → объект модели - для создания/обновления.
class BookDetailSerializer(serializers.ModelSerializer):
    """

    """
    # 📌 BookDetailSerializer
    # Его ключевые особенности:
    # 1. Явно указаны поля publisher и genres:
    #       - Оба они — связи с другими моделями (ForeignKey и ManyToManyField).
    #       - По умолчанию DRF сериализовал бы их через id или через __str__ (в зависимости от настроек).
    #       - А тут используется PrimaryKeyRelatedField, который явно говорит:
    #         👉 выводить не вложенный объект, а только его первичный ключ (id).
    #   Пример вывода:
    #       {
    #           "id": 1,
    #           "title": "Как учить Python",
    #           "publisher": 3,     # только ID издателя!
    #           "genres": [2, 5]    # список ID жанров!
    #       }

    # publisher = PublisherSerializer()
    # publisher = serializers.StringRelatedField()

    # publisher = serializers.SlugRelatedField(
    #     slug_field='slug',
    #     queryset=Publisher.objects.all(),
    # )

    publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Book
        fields = '__all__'

    # 2. Отличие от BookSerializer:
    #   - BookSerializer может быть более «гибким» и работать с кастомной логикой
    #     (to_representation, скрытие полей).
    #   - BookDetailSerializer нужен именно для детального представления, когда важно
    #     отразить связи через ID, чтобы потом удобно обновлять/создавать записи.
    # 📌 То есть, если BookSerializer больше про "вывод красиво и выборочно",
    # то BookDetailSerializer — "удобство CRUD-операций" (создание/обновление/детальный просмотр).

    # ==============================================================================
    # https://chatgpt.com/s/t_68bd2bee9f9c8191ae45b97de641edd1

    # \\\\\\   Что делает PrimaryKeyRelatedField?  ///////
    # Это специальное поле сериализатора, которое работает со связанными моделями.
    #   - PrimaryKeyRelatedField(queryset=Publisher.objects.all()) означает:
    #       + при сериализации → возвращать только ID издателя;
    #       + при ДЕсериализации (например, при создании книги через POST) → принимать ID и искать по нему объект из указанного queryset.
    #   - many=True у жанров значит, что это список ID (так как связь ManyToMany).
    # Пример создания книги через API:
    #       {
    #           "title": "Новая книга",
    #           "publisher": 3,
    #           "genres": [1, 4]
    #       }
    # Здесь 3 — id издателя, [1, 4] — id жанров. Сериализатор сам найдёт нужные объекты и свяжет их.
    # ✨ Таким образом:
    #   - BookSerializer — гибкий, можно прятать или показывать genres по контексту.
    #   - BookDetailSerializer — для CRUD, связи (publisher, genres) работают через
    #     PrimaryKeyRelatedField, т.е. принимают и отдают ID вместо вложенных объектов.
    # ==============================================================================



# Сериалайзер для преобразования модель/JSON входных данных по ЖАНРАМ.
class GenreSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Genre
        fields = '__all__'



# Сериалайзер для преобразования модель/JSON входных данных по ????????????????.
class SimpleBookSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = SimpleBook
        fields = '__all__'
