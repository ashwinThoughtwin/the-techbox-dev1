from django.db import models
from phone_field import PhoneField

# Create your models here.
DESIGNATION = (
    ('PYTHON TEAM LEADER', 'python team leader'),
    ('PYTHON SENIOR DEV', 'python senior developer'),
    ('PYTHON JUNIOR DEV', 'python junior developer'),
    ('PYTHON TRAINEE DEV', 'python trainee developer'),

    ('ROR TEAM LEADER', 'ror team leader'),
    ('ROR SENIOR DEV', ' ror senior developer'),
    ('ROR JUNIOR DEV', 'ror junior developer'),
    ('ROR TRAINEE DEV', 'ror trainee developer'),

    ('FRONTEND TEAM LEADER', 'frontend team leader'),
    ('FRONTEND SENIOR DEV', 'frontend senior developer'),
    ('FRONTEND JUNIOR DEV', 'frontend junior developer'),
    ('FRONTEND TRAINEE DEV', 'frontend trainee developer'),
)


class TechTool(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

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


class Schedule(models.Model):
    empName = models.ForeignKey(Employee, on_delete=models.CASCADE)
    techTool = models.ForeignKey(TechTool, on_delete=models.CASCADE)
    borrowTime = models.DateTimeField(auto_now_add=True)
    SubmitDate = models.DateTimeField()

    def __str__(self):
        return self.techTool.name
