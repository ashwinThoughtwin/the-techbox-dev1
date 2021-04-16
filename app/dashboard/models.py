from django.db import models
from phone_field import PhoneField

# Create your models here.
DESIGNATION = (
    ('1', ' team leader'),
    ('2', ' senior developer'),
    ('3', ' junior developer'),
    ('4', ' trainee developer')
)


class TechTool(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(choices=DESIGNATION, max_length=100)
    address = models.CharField(max_length=150)
    mobile = PhoneField(blank=True, help_text='Contact mobile number')
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class ToolsIssue(models.Model):
    empName = models.ForeignKey(Employee, on_delete=models.CASCADE)
    techTool = models.ForeignKey(TechTool, on_delete=models.CASCADE)
    borrowTime = models.DateTimeField()
    submitDate = models.DateTimeField()

    def __str__(self):
        return self.techTool.name
