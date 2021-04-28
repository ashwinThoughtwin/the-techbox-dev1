from django.urls import path
from . import views
from . import views_api

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='dashboard'),

    path('add-employee/', views.AddEmployees.as_view(), name='add_employee'),
    path('update-employee/<int:pk>/', views.EmployeeUpdate.as_view(), name='update_employee'),
    path('delete-employee/', views.EmployeeDelete.as_view(), name='delete_employee'),
    path('employee-list/', views.EmployeeList.as_view(), name='employee_list'),
    path('employee-detail/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),

    path('add-techtool/', views.AddTechTools.as_view(), name='add_techtool'),
    path('update-techtool/', views.UpdateTechTools.as_view(), name='update_techtool'),
    path('delete-techtool/', views.DeleteTechTools.as_view(), name='delete_techtool'),
    path('techtool-list/', views.TechToolList.as_view(), name='techtool_list'),

    path('assign-tool/', views.AssignTools.as_view(), name='assign_tool'),
    path('tool-issue/', views.ToolIssued.as_view(), name='tools_issued'),

    # urls for api
    path('toollist-api/', views_api.TechToolListApi.as_view(), name="techtoollist_api"),
    path('tooldetail-api/<int:pk>/', views_api.TechToolDetailApi.as_view(), name="tooldetail_api"),
    path('assign-list-api/', views_api.AssignToolListApi.as_view(), name="assign_list_api"),
    path('assign-create-api/', views_api.AssignToolCreateApi.as_view(), name="assign_create_api"),



]
