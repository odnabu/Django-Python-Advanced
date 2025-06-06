"""
WSGI config for DjangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Так как я ПЕРЕИМЕНОВАЛА папку с настройками из DjangoProject в DjangoProject_config, то
# НЖНО внести правки во ВСЕ файлы настроек:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject_config.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')

application = get_wsgi_application()
