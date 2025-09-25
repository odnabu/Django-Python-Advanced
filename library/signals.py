# Link on GitHub: https://github.com/viacheslav-bandylo/111124-projects/blob/main/library/signals.py

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from library.models import Book



# @receiver - это декоратор для подключения функции к сигналу.
# Первый аргумент - сам сигнал (post_save).
# sender=Book - указывает, что мы слушаем сигнал только от модели Book.
@receiver(post_save, sender=Book)
def book_saved_handler(sender, instance, created, **kwargs):
    # 'created' - это флаг, который говорит нам, был ли объект создан
    if created:
        print(f'New Book was created: {instance.title}.')
    else:
        print(f'The Book was updated: {instance.title}.')


@receiver(post_save, sender=Book)
def notify_admin_on_new_book(sender, instance, created, **kwargs):
    if created:
        print("Sending mail with notify to admin...")
        send_mail(
            subject=f'New Book in the sistem: {instance.title}.',
            message=f'User {instance.owner.username} has added a new Book "{instance.title}"',
            from_email='no_reply@example.com',
            recipient_list=['admin@example.com']
        )


# ??????????????
# def book_saved_handler(sender, instance, created, **kwargs):
#     if created:
#         print(f'Новая книга создана: {instance.title}')
#     else:
#         print(f'Книга обновлена: {instance.title}')
#
# # Подключаем функцию к сигналу вручную
# post_save.connect(book_saved_handler, sender=Book)

