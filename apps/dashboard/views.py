from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import EmployeeForm, TechToolForm,AssignToolForm
from django.contrib import messages
from django.views.generic import UpdateView


class DashBoard(View):

    @method_decorator(login_required(login_url="/"))
    def get(self, request):
        data = {}
        employees = Employee.objects.all()
        data['employees'] = employees
        tools = TechTool.objects.all()
        data['numberofemp'] = employees.count()
        data['numberoftools'] = tools.count()
        issued_tools = ToolsIssue.objects.all()
        data['issued_tools'] = issued_tools
        data['tools'] = tools

        trainee = 0
        tl = 0
        jd = 0
        sd = 0
        data['assigned_to_tl'] = 0
        data['assigned_to_sd'] = 0
        data['assigned_to_jd'] = 0
        data['assigned_to_trainee'] = 0
        issuedcount = issued_tools.count()

        for i in issued_tools:
            if i.empName.designation =='1':
                tl += 1

            elif i.empName.designation == '2':
                sd += 1

            elif i.empName.designation == '3':
                jd += 1

            elif i.empName.designation == '4':
                trainee += 1

        if trainee > 0:
            data['assigned_to_trainee'] = ((trainee * 100) / issuedcount)
        if jd > 0:
            data['assigned_to_jd'] += ((jd * 100) // issuedcount)
        if sd > 0:
            data['assigned_to_sd'] += ((sd * 100) // issuedcount)
        if tl > 0:
            data['assigned_to_tl'] += ((tl * 100) // issuedcount)

        return render(request, 'dashboard/dashboard.html', data)


class AddTechTools(View):

    def post(self, request):
        add_too_form = TechToolForm(request.POST)
        if add_too_form.is_valid():
            add_too_form.save()

        return redirect("techtool_list")

    def get(self, request):
        form = TechToolForm
        return render(request, 'dashboard/techtool_add.html', {'form': form})


class TechToolList(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        data = {}
        tools = TechTool.objects.all()
        data['tools'] = tools
        return render(request, 'dashboard/techtool-list.html', data)


class UpdateTechTools(View):

    def post(self, request, pk):
        tool = TechTool.objects.get(id=pk)
        tool_form = TechToolForm(request.POST,instance=tool)
        if tool_form.is_valid():

            status = request.POST.get('status')
            if status == 'Yes':
                tool_form.status = True
                tool_form.save()

            else:
                print(status)
                tool_form.status = False
                tool_form.save()

            print(request.POST)
            # tool.save()

            return redirect("techtool_list")

    def get(self, request,pk):

        form = TechToolForm()
        return render(request, 'dashboard/update-tool.html', {'form': form})


class DeleteTechTools(View):

    def get(self, request, pk):
        tool = TechTool.objects.get(id=pk)

        tool.delete()

        return redirect("techtool_list")


# Employee views


class AddEmployees(View):

    def get(self, request):
        form = EmployeeForm

        return render(request, 'dashboard/add-employee.html', {'form': form})

    def post(self, request, *args, **kwargs):
        try:
            emp_form = EmployeeForm(request.POST, request.FILES)
            print(request.POST)
            if emp_form.is_valid():
                emp_form.save()
                return redirect('employee_list')
            else:
                return HttpResponse("not valid")

        except Exception as e:
            print(e)
        return render(request, 'dashboard/add-employee.html')


class EmployeeList(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request):
        data = {}
        employees = Employee.objects.all()
        data['employees'] = employees

        return render(request, 'dashboard/employee-list.html', data)


class EmployeeDetail(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request, pk):
        data = {}
        employee = Employee.objects.get(pk=pk)
        data['employee'] = employee

        return render(request, 'dashboard/employee-profile.html', data)


class EmployeeUpdate(View):

    def get(self, request, pk):
        form = EmployeeForm
        return render(request, 'dashboard/update-employee.html', {'form': form})

    @method_decorator(login_required(login_url="/login/"))
    def post(self, request, pk):

        employee = Employee.objects.get(id=pk)
        emp_upd_form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if emp_upd_form.is_valid():
            emp_upd_form.save()
            return redirect('employee_list')
        else:
            return HttpResponse("update not valid ")


class EmployeeDelete(View):

    @method_decorator(login_required(login_url="/login/"))
    def get(self, request, pk):
        data = {}
        employee = Employee.objects.get(pk=pk)
        employee.delete()

        return redirect('employee_list')


class AssignTools(View):

    def get(self, request):
        data = {}
        # employees = Employee.objects.all()
        # data['employees'] = employees
        # tools = TechTool.objects.all()
        # data['tools'] = tools
        assign_from = AssignToolForm
        data['assign_from']=assign_from

        return render(request, 'dashboard/assign-tool.html', data)

    def post(self, request, *args, **kwargs):
        assign_form =AssignToolForm(request.POST)

        if assign_form.is_valid():
            assign_form.save()
            return redirect('tools_issued')
        else:
            return HttpResponse("no tool issued")


class ToolIssued(View):

    def get(self, request):
        issued_tools = ToolsIssue.objects.all()

        return render(request, 'dashboard/tool-issue.html', {'issued_tools': issued_tools})
