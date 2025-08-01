# _____ home_work_15.md:  Если задача переходит в новый статус, или закрывается - тот,
# кому принадлежит эта задача, должен получать Email уведомление на свою почту.




# --------------------------------------------------------------------------------------
# ИЗ примера для library от Bandylo:
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from hw_02_task_manager.models import Task
# @receiver - это декоратор для подключения функции к сигналу.
# Первый аргумент - сам сигнал (post_save).
# sender=Task - указывает, что мы слушаем сигнал только от модели Task.
@receiver(post_save, sender=Task)
def task_saved_handler(sender, instance, created, **kwargs):
    # 'created' - это флаг, который говорит нам, был ли объект создан
    if created:
        print(f'\t\033[31m{'*'*50}\033[m\n'
              f'\tНовая задача создана: {instance.title}\n'
              f'\t\033[31m{'*'*50}\033[m')
    else:
        print(f'\t\033[32m{'='*50}\033[m\n'
              f'\tОбновлена задача: {instance.title}\n'
              f'\t\033[32m{'='*50}\033[m')


@receiver(post_save, sender=Task)
def notify_admin_on_new_task(sender, instance, created, **kwargs):
    if created:
        print("Отправка письма администратору...")
        send_mail(
            subject=f'Новая задача в системе: {instance.title}',
            message=f'Пользователь {instance.owner.username} добавил новую задачу "{instance.title}" (ID: {instance.id}).',
            from_email='noreply@example.com',
            recipient_list=['admin@example.com'],
        )
# --------------------------------------------------------------------------------------



# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from hw_02_task_manager.models import Task
#
#
# @receiver(pre_save, sender=Task)
# def notify_owner_on_status_change(sender, instance, **kwargs):
#     if not instance.pk:
#         return  # Пропускаем новую задачу — она только создаётся
#
#     old_instance = Task.objects.get(pk=instance.pk)
#
#     if instance.status != old_instance.status:
#         # Проверка: уведомление на этот статус уже отправлялось?
#         if instance.last_notified_status == instance.status:
#             return
#
#         # Уведомляем
#         if instance.owner and instance.owner.email:
#             send_mail(
#                 subject=f'\t\033[33m{'='*50}\033[m\n'
#                         f"\tИзменение статуса задачи: {instance.title}",
#                 message=(
#                     f'\tЗдравствуйте, {instance.owner.username}!\n\n'
#                     f'\tСтатус вашей задачи "{instance.title}" был изменён на "{instance.status}".\n'
#                     f'\t\033[33m{'='*50}\033[m\n\t'
#                 ),
#                 from_email='noreply@taskmanager.local',
#                 recipient_list=[instance.owner.email],
#                 fail_silently=True
#             )
#
#         # Обновим поле, чтобы не слать снова на тот же статус
#         instance.last_notified_status = instance.status



