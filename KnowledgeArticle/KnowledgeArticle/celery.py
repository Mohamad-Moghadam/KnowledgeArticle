import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KnowledgeArticle.settings')

app = Celery('KnowledgeArticle')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()