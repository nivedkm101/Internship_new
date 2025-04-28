from django.urls import path
from . import views

urlpatterns = [
    path('', views.hostel, name='hostel'),
    path('circular_hostel/', views.circular_hostel, name='circular_hostel'),
    path('hostelRules/', views.hostelRules, name='hostelRules'),
    path('hostel_facilities/',views.hostel_facilities,name='hostel_facilities'),
]
