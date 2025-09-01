from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.about, name='about'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    ]