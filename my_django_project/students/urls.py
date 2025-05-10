from django.urls import path
from . import views

urlpatterns = [

    
    path('', views.welfare, name='welfare'),
    path('studentrules/', views.studentrules, name='studentrules'),
    path('antiragging/', views.anti_ragging, name='anti_ragging'),
    path('annualfest/',views.annualfest, name='annualfest'),
    path('orientation/',views.orientation, name='orientation'),
    path('clubs/',views.clubs, name='clubs'),
    path('student_association/',views.student_association, name='student_association'),
    path('councelling/',views.counselling_service, name='counselling_service'),
    path('Grievance Redressal/',views.grievance_redressal, name='grievance_redressal'),
    path('sw-announcements/',views.sw_announcements, name='sw_announcements'),
    path('medical_insurance/',views.medical_insurance, name='medical_insurance'),
    path('studentActivities/',views.studentActivities, name='studentActivities'),
    path('aluminiRelations/', views.aluminiRelations, name='aluminiRelations'),
    path('internship/', views.internship, name='internship'),
    path('council/',views.council, name='council'),
    path('ncc/',views.ncc, name='ncc'),
    path('nss/',views.nss, name='nss'),

]

