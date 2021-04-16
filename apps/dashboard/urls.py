from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='dashboard'),

    path('add-employee/', views.AddEmployees.as_view(), name='add_employee'),
    path('update-employee/<int:pk>/', views.EmployeeUpdate.as_view(), name='update_employee'),
    path('delete-employee/<int:pk>/', views.EmployeeDelete.as_view(), name='delete_employee'),
    path('employee-list/', views.EmployeeList.as_view(), name='employee_list'),
    path('employee-detail/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),

    path('add-techtool/', views.AddTechTools.as_view(), name='add_techtool'),
    path('update-techtool/<int:pk>/', views.UpdateTechTools.as_view(), name='update_techtool'),
    path('delete-techtool/<int:pk>/', views.DeleteTechTools.as_view(), name='delete_techtool'),
    path('techtool-list/', views.TechToolList.as_view(), name='techtool_list'),

    path('assign-tool/', views.AssignTools.as_view(), name='assign_tool'),
    path('tool-issue/', views.ToolIssued.as_view(), name='tools_issued'),

]
