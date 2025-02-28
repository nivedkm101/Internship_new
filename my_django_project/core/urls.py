from django.urls import path
from .views import home, about,reach_us,contact,announcement_banner,gallery_view,newsletter,tendernews
from .views import upcommingEvents,research_component

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    
    path('reach_us/',reach_us, name='reach_us'),

    path('contact/', contact, name='contact'),
    
    path('announcement_banner/', announcement_banner, name='announcement_banner'),

    path('gallery/', gallery_view, name='gallery'),


    path('institute/administration/newsletter/', newsletter, name='newsletter'),

    path('tendernews/', tendernews, name='tendernews'),

    path('upcommingEvents/', upcommingEvents, name='upcommingEvents'),
    
    path('research_component/', research_component, name='research_component'),
    
]
