from django.contrib import admin
from django.urls import path , include

from profil import views
urlpatterns = [
    path('land/',views.landing_page,name='landing_page'),
    
    path('education/',views.edu_page,name='edu_page'),
    path('skills/',views.skills_page,name='skills_page'),
    path('projects/',views.projects_page,name='projects_page'),
    path('experience/',views.experience_page,name='experience_page'),
    path('contact/',views.contact_page,name='contact_page'),
    
    path('base/',views.base_nav,name='base_nav'),
]