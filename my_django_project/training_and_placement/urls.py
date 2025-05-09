from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.training_and_placement, name='training_and_placement'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('procedure/', views.procedure, name='procedure'),
    path('program/', views.program, name='program'),
    path('recruitments/', views.recruitments, name='recruitments'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.tnp_contact, name='tnp_contact'),
    
]