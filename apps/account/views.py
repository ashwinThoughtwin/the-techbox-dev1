from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages


class Login(View):

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('dashboard')
        else:
            messages.error(request, " Username or password is Incorrect  ")
            return render(request, 'account/login.html')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'account/login.html')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect("login")

