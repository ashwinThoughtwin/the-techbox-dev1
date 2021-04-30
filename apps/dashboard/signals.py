from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import TechTool
from apps.dashboard.task import send_mail_after_create_techtool


@receiver(post_save, sender=TechTool)
def create_tool(sender, instance, created, **kwargs):
    if created:
        name = instance.name

        subject = f'{name} is  created '
        message = f'Hi {name} is created successfully'
        recipient_list = ['virendrakapoor45@gmail.com', ]

        send_mail_after_create_techtool.delay(subject,message,recipient_list)
        print('created')
