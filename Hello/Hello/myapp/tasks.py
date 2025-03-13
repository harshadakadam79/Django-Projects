from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_bulk_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'your-email@example.com',  # Replace with your sender email
        recipient_list,
        fail_silently=False,
    )
    return f"Emails sent to {len(recipient_list)} users!"
