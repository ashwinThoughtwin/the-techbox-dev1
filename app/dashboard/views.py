from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import  UpdateView


class AddEmployees(View):

    def get(self, request):
        print(DESIGNATION)
        designations = []
        for d in DESIGNATION:
            designations.append(d[1])
        return render(request, 'dashboard/add-employee.html', {'designations': designations})

    def post(self, request, *args, **kwargs):
        try:
            designations = []
            for d in DESIGNATION:
                designations.append(d[1])
            name = request.POST.get('name')
            designation = request.POST.get('designation')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            date_of_birth = request.POST.get('dob')
            print(request.POST)

            employee = Employee.objects.create(name=name, designation=designation, address=address,
                                               mobile=mobile, email=email, date_of_birth=date_of_birth)
            return redirect('employee_list')

        except Exception as e:
            print(e)
        return render(request, 'dashboard/add-employee.html')


class AddTechTools(View):

    def post(self, request):
        name = request.POST.get('name')
        TechTool.objects.create(name=name)
        return HttpResponse("created")

    def get(self, request):
        return render(request, 'dashboard/techtool_add.html')


class AddTechTools(View):

    def post(self, request):
        name = request.POST.get('name')
        TechTool.objects.create(name=name)
        return HttpResponse("created")

    def get(self, request):
        return render(request, 'dashboard/techtool_add.html')


class EmployeeList(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        data = {}
        employees = Employee.objects.all()
        data['employees'] = employees

        return render(request, 'dashboard/employee-list.html', data)


class EmployeeDetail(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request,pk):
        data = {}
        employee = Employee.objects.get(pk=pk)
        data['employee'] = employee

        return render(request, 'dashboard/employee-profile.html', data)

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'dashboard/add-employee.html'
    # context_object_name = 'update_form'
    fields = ('name','designation','address','email','mobile','date_of_birth')
    success_url = '/dashboard/'

#     need to work





class EmployeeDelete(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request,pk):
        data = {}
        employee = Employee.objects.get(pk=pk)
        employee.delete()

        return redirect('employee_list')





class TechToolList(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        data = {}
        tools = TechTool.objects.all()
        data['tools'] = tools
        return render(request, 'dashboard/techtool-list.html', data)




class DashBoard(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        data = {}
        employees = Employee.objects.all()
        data['employees'] = employees
        tools = TechTool.objects.all()
        data['tools'] = tools

        return render(request, 'dashboard/dashboard.html', data)
