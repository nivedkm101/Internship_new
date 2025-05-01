from django.urls import path
from . import views

urlpatterns = [

    path('', views.netandsys, name='netandsys'),
    path('aiserver/', views.aiserver, name='aiserver'),
    path('hardware/', views.hardware, name='hardware'),
    path('software/', views.software, name='software'),
    path('emailkb/', views.emailkb, name='emailkb'),
    
]

