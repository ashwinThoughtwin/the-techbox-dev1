from django.contrib import admin
from .models import TechTool, Employee, ToolsIssue

admin.site.register(TechTool)
admin.site.register(Employee)
admin.site.register(ToolsIssue)