from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *


class AddEmployees(View):

    def get(self, request):
        print(DESIGNATION)
        designations = []
        for d in DESIGNATION:
            designations.append(d[1])
        return render(request, 'dashboard/employee_add.html', {'designations': designations})

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
            return render(request, 'dashboard/employee_add.html', {'employee': employee, 'designations': designations})

        except Exception as e:
            print(e)
        return render(request, 'dashboard/employee_add.html')


class AddTechTools(View):

    def get(self,request):

        return render(request, 'dashboard/techtool_add.html')

    # def post(self, request):
    #     name = request.POST.get('name')
    #     quantity = request.POST.get('quantity')
    #     techtool = TechTool.objects.create(name=name, quantity=quantity)
    #
    #     return HttpResponse('tool added')