# encoding: ISO8859-1
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer la configuraci�n de Celery y le indicamos que use el archivo settings.py de nuestro proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales.settings')

# Crear una instancia de la aplicaci�n Celery
app = Celery('sales')

# Configurar Celery mediante el archivo de configuraci�n de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks en todas las aplicaciones Django
app.autodiscover_tasks()
