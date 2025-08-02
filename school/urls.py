"""
URL configuration for books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views
from .views import contact_page


urlpatterns = [
    path('contact/', contact_page, name='contact'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),

    path('terms_of_service/', views.terms_of_service,name='terms_of_service'),
    path('students_life/', views.students_life, name='students_life'),
   path('starter_page/', views.starter_page, name='starter_page'),
    path('privacy/', views.privacy, name='privacy'),
    path('news_details/', views.news_details, name='news_details'),
    path('news/', views.news, name='news'),
    path('home/', views.home, name='home') ,

    path('faculty_staff/', views.faculty_staff, name='faculty_staff'),
    path('events/', views.events, name='events'),
    path('event_details/' , views.event_details, name='event_details'),
    path('contact/', views.contact, name='contact'),
    path('campus_facilities/', views.campus_facilities, name='campus_facilities'),
    path('alumni/', views.alumni, name='alumni'),
    path('admissions/', views.admissions, name='admissions'),
    path('academics/', views.academics, name='academics'),


]
