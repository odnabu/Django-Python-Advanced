# Link on GitHub: https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/factories.py

# FactoryBoy см. VIDEO P.6, 1:02:40.
# url: https://player.vimeo.com/video/1107052048?h=4bc883f8d0

# __ NB! __  --> How to install package factory-boy in PowerShell -->
#       pip install factory-boy
import factory

from library.models import SimpleBook


# ___  ГЕНЕРАТОР случайной книги  ___
class SimpleBookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SimpleBook

    # VIDEO P.6, 1:06:00.
    title = factory.Faker('sentence', nb_words=4)       # Класс Faker генерирует случайное предложение из 4-х слов.
    author = factory.Faker('name')                              # Класс Faker генерирует случайное имя.
    publication_date = factory.Faker('date')
