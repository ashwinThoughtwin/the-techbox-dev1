from django.urls import path
from . import views

urlpatterns = [
    path('add-employee/', views.AddEmployees.as_view(), name='add_employee'),
    path('update/<int:pk>/', views.EmployeeUpdate.as_view(), name='update'),

    path('add-techtool/', views.AddTechTools.as_view(), name='add_techtool'),
    path('dashboard/', views.DashBoard.as_view(), name='dashboard'),
    path('employee-list/', views.EmployeeList.as_view(), name='employee_list'),
    path('profile/<int:pk>/', views.EmployeeDetail.as_view(), name='profile'),
    path('delete/<int:pk>/', views.EmployeeDelete.as_view(), name='emp_delete'),

    path('techtool-list/', views.TechToolList.as_view(), name='techtool_list'),

]
