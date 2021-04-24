from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from .task import mail_To_Timeover_Employee

from django.conf import settings
from apps.dashboard.models import ToolsIssue



class Login(View):

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(request.POST)
        user = authenticate(
                username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('dashboard')
        else:
            messages.error(request," Username or password is Incorrect  ")
            return render(request, 'account/login.html')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'account/login.html')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect("login")


def sendmailToEmp(request):

    issue = ToolsIssue.objects.all()
    for emp in issue:
        subject = f'Hello {emp.empName.name} time over'
        message = f'Hi your techtool- {emp.techTool.name} Usage Time is Expired Please Submit {emp.techTool.name} if ' \
                  f'in office you already Submit then skip this mail Have A Good !'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [emp.empName.email, ]

        mail_To_Timeover_Employee.delay(subject,message,email_from,recipient_list)
    return HttpResponse("mail sended ")
