from django.contrib import admin
from hw_02_task_manager.models import Category, Task, SubTask

# Register your models here.

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)

