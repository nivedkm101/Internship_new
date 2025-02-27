from django.urls import path
from . import views

urlpatterns = [
    path('', views.hostel, name='hostel'),
    path('circular_hostel/', views.circular_hostel, name='circular_hostel'),
]
