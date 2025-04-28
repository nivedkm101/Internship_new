from django.urls import path
from . import views

urlpatterns = [
    path('Opportunities/', views.career, name='career'),
]
