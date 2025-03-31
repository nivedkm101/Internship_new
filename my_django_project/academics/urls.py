from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar_view'),  
    path('emailContacts/', views.email_queries, name='email_queries'),
    path('convocation/', views.convocation, name='convocation'),
    path('exam/', views.exam, name='exam'),
    path('fee-structure/', views.fee, name='fee-structure'),
    path('scholarship/', views.scholarship, name='scholarship'),
    path("curriculum/", views.curriculum, name="curriculum"),
    path('results/', views.results, name='results'),
    path('nad/', views.nad, name='nad'),
]
