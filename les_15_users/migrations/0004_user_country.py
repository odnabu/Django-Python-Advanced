# Generated by Django 5.2.1 on 2025-06-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('les_15_users', '0003_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('PT', 'Portugal'), ('ES', 'Spain'), ('MV', 'Maldives'), ('DE', 'Germany')], default='DE'),
        ),
    ]
