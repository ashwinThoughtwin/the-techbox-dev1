from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from apps.dashboard.models import ToolsIssue
from time import sleep
import datetime
import pytz
ist=pytz.timezone("Asia/Calcutta")

@shared_task()
def mailToAssignedemp():
    print(ist)
    x=ist.localize(datetime.datetime.now())
    issue = ToolsIssue.objects.all()
    for data in issue:

        if data.submitDate >= x:
            subject = f'Hello {data.empName.name} time over'
            message = f'Hi  your techtool- {data.techTool.name} due time is over after  please submit the tool or  ' \
                      f'contact to office admin for extend your usage time. '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [data.empName.email, ]
            send_mail(subject, message, email_from, recipient_list)
            data.delete()

            return None




