from django import forms
from apps.dashboard.models import Employee, TechTool,ToolsIssue
from phone_field import PhoneField

DESIGNATION = (
    ('1', ' team leader'),
    ('2', ' senior developer'),
    ('3', ' junior developer'),
    ('4', ' trainee developer'),
)


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Name'
    }))
    image = forms.FileField(widget=forms.FileInput(attrs={
        'class': "form-control"
    }))
    designation = forms.ChoiceField(choices=DESIGNATION, widget=forms.Select(attrs={
        'class': "form-control"

    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee address'
    }))

    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Mobile'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Email'
    }))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Date of Birth'

    }))

    class Meta:
        model = Employee

        fields = ('name', 'image', 'designation', 'address', 'mobile', 'email', 'date_of_birth')


class TechToolForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Name'
    }))
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': "form-control",
        'placeholder': 'Employee Name'
    }), required=False)

    class Meta:
        model = TechTool
        fields = ('name', 'status')


class AssignToolForm(forms.ModelForm):
    empName = forms.ModelChoiceField(queryset=Employee.objects.all(),widget=forms.Select(attrs={
        'class': "form-control"

    }))
    techTool = forms.ModelChoiceField(queryset=TechTool.objects.all(), widget=forms.Select(attrs={
        'class': "form-control"

    }))
    borrowTime = forms.DateTimeField(    widget = forms.SelectDateWidget(attrs={
        'class': "form-control",
        'placeholder': 'Assign Date or Time'

    }))
    submitDate = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={
        'class': "form-control ",
        'placeholder': 'Submit Date or Time'

    }))


    class Meta:
        model = ToolsIssue
        fields = ('empName','techTool','borrowTime','submitDate')
