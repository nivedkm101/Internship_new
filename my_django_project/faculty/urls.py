from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
    path('', views.FacultyListView.as_view(), name='faculty_list'),
    path('adminDirectory/', views.admin_directory, name='admin_directory'),
    path('hodDirectory/', views.hod_directory, name='hod_directory'),
    path('deanDirectory/', views.dean_directory, name='dean_directory'),
    path('facultyDirectory/', views.faculty_directory, name='faculty_directory'),
    path('focDirectory/', views.foc_directory, name='foc_directory'),
    path('officerDirectory/', views.officer_directory, name='officer_directory'),
    path('pdDirectory/', views.pd_directory, name='pd_directory'),
    path('staffDirectory/', views.staff_directory, name='staff_directory'),
    path('faculty-welfare/', views.faculty_welfare, name='faculty_welfare'),

]