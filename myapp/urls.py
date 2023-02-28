
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('contact1/',views.contact1,name='contact1'),
    path('header/',views.header,name='header'),
    path('about/',views.about,name='about'),
    path('services',views.services,name='services'),
    path('services/quality-assurance-services',views.Quality_Assurance_Services,name='Quality_Assurance_Services'),
    path('services/cloud-computing',views.Cloud_Computing,name='Cloud_Computing'),
    path('services/android-application-development',views.Android_Application_Development,name='Android_Application_Development'),
    path('services/mobile-app-development',views.React_Native_Development,name='React_Native_Development'),
    path('services/web-development',views.Web_Development,name='Web_Development'),
    path('services/game-development',views.Game_development,name='Game_development'),
    path('career/',views.career,name='career'),
    path('job-apply',views.job_apply,name='job_apply'),
    path('career/job/<int:pk>/',views.Job_Post,name='Job_Post'),
    path('sitemap',views.sitemap,name='sitemap'),
    path('privacy-policy',views.privacy_policy,name='privacy_policy'),
    # path('Job/Job_Post/<slug:slug>/', views.Job_Post, name='Job_Post'),
   
    
]

