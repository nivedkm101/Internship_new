from django.urls import path
from . import views

urlpatterns = [
    path('', views.institute, name='institute'),
    path('campus/', views.campus, name='campus'),
    path('rules/', views.rules, name='rules'),
    path('forms/', views.forms, name='forms'),
]
