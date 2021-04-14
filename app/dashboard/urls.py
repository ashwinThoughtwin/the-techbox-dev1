from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-employee/', views.AddEmployees.as_view(), name='add_employee'),
    path('add-techtool/', views.AddTechTools, name='add_techtool'),

]
