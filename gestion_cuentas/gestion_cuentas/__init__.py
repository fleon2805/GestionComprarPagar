from __future__ import absolute_import, unicode_literals

# Importa Celery para que se cargue automáticamente
from .celery import app as celery_app

__all__ = ['celery_app']
