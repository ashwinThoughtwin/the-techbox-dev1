from django import forms
import datetime
from apps.dashboard.models import Employee, TechTool, ToolsIssue
from phone_field import PhoneField
from django.contrib.admin.widgets import AdminDateWidget

DESIGNATION = (
    ('1', ' team leader'),
    ('2', ' senior developer'),
    ('3', ' junior developer'),
    ('4', ' trainee developer'),
)


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Name',
        'id': "emp-name",

    }))
    image = forms.FileField(widget=forms.FileInput(attrs={
        'class': "form-control",
        'id': "emp-image"
    }))
    designation = forms.ChoiceField(choices=DESIGNATION, widget=forms.Select(attrs={
        'class': "form-control",
        'id': "emp-designation"

    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee address',
        'id': "emp-address"
    }))

    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Mobile',
        'id': "emp-mobile"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Email',
        'id': "emp-email"

    }))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Date of Birth',
        'id': "emp-dob"

    }))

    class Meta:
        model = Employee

        fields = ('name', 'image', 'designation', 'address', 'mobile', 'email', 'date_of_birth')


class TechToolForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Tool  Name',
        'id': "tool-name"
    }))
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': "form-control",

        'id': "tool-status"
    }), required=False)

    class Meta:
        model = TechTool
        fields = ('name', 'status')


class AssignToolForm(forms.ModelForm):
    empName = forms.ModelChoiceField(queryset=Employee.objects.all(), widget=forms.Select(attrs={
        'class': "form-control"

    }))
    techTool = forms.ModelChoiceField(queryset=TechTool.objects.all(), widget=forms.Select(attrs={
        'class': "form-control"

    }))
    # borrowTime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
    #     'class': "form-control ",
    #     ' id ': "datepicker1",
    #     'type' : "datetime-local"
    # }))
    submitDate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'class': "form-control ",
        ' id ': "datepicker2",
        'type': "datetime-local",
        'min': datetime.datetime.now(),

    }))

    class Meta:
        model = ToolsIssue
        fields = ('empName', 'techTool', 'submitDate')
