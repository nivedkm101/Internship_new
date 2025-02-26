from django.urls import path
from . import views
urlpatterns = [


    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('procedure/', views.procedure, name='procedure'),
    path('program/', views.program, name='program'),
    path('recruitments/', views.recruitments, name='recruitments'),
    path('testimonial/', views.testimonial, name='testimonial'),
    
]