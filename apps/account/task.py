from celery import shared_task
from django.core.mail import send_mail
from apps.dashboard.models import ToolsIssue
import datetime
from django.conf import settings

import pytz

ist = pytz.timezone("Asia/Calcutta")


@shared_task()
def status_change():
    print(ist)
    x = ist.localize(datetime.datetime.now())
    issue = ToolsIssue.objects.all()
    print(x)

    for data in issue:
        if data.submitDate < x:
            data.timeOut = True
            data.save()

    return None


def mail_To_Timeover_Employee(subject,message,email_from,recipient_list):

    send_mail(subject, message, email_from, recipient_list)
    return None
