from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcements, name='announcements'),
    path('tenders/', views.tenders, name='tenders'),
    path('upcomingEvents/', views.upcomingEvents, name='upcomingEvents'),
    path('researchComponents/', views.researchComponents, name='researchComponents'),
]