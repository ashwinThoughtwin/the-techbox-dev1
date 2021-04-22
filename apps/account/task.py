from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from apps.dashboard.models import ToolsIssue
from time import sleep
import datetime

@shared_task()
def mailToAssignedemp():
    sleep(10)

    subject = 'welcome to GFG world'
    message = f'Hi  your techtool due time is over after some days please submit the tool or  ' \
              f'contact to office admin for extend your usage time. '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['virendrakapoor45@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    return None


