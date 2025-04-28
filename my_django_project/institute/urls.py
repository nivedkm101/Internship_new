from django.urls import path
from . import views

urlpatterns = [
    path('', views.institute, name='institute'),
    path('campus/', views.campus, name='campus'),
    path('rules/', views.rules, name='rules'),
    path('forms/', views.forms, name='forms'),
    path('icc/', views.icc, name='icc'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('campusconnect/', views.campusconnect, name='campusconnect'),
    path('bulletin/',views.bulletin,name='bulletin'),
    path('rti/',views.rti,name='rti'),
    path('nirf/',views.nirf,name='nirf'),
]
