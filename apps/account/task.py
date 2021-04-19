from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from apps.dashboard.models import ToolsIssue
from time import sleep


def mailToAssignedemp():
    sleep(20)
    empName = ToolsIssue.objects.get(id=5)
    subject = 'welcome to GFG world'
    message = f'Hi {empName.empName.name}, your techtool due time is over after some days please submit the tool or  ' \
              f'contact to office admin for extend your usage time. '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [empName.empName.email, ]
    send_mail(subject, message, email_from, recipient_list)
    return None
