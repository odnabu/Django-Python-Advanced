# Generated by Django 5.2.1 on 2025-06-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('les_15_users', '0002_user_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
