from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcements, name='announcements'),
    path('tenders/', views.tenders, name='tenders'),
]