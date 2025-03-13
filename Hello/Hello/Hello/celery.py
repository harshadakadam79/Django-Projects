import os
from ..celery_config import app as celery_app  
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hello.settings')

# Use the existing Celery app instance
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

# Define Celery Beat Schedule (AFTER initializing `celery_app`)
celery_app.conf.beat_schedule = {
    "send_bulk_emails_daily": {
        "task": "your_app.tasks.send_bulk_emails",
        "schedule": crontab(hour=10, minute=0),  # Runs daily at 10 AM
    },
}
