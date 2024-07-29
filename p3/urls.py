from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='homePage'),
    path('index--header-slider-classic/', views.headerSliderClassicPage, name='headerSliderClassic'),
    path('index--header-slider/', views.headerSliderPage, name='headerSlider'),
    path('index--home-classic/', views.homeClassicPage, name='homeClassic'),
    path('index--selfhosted-classic/', views.selfhostedClassicPage, name='selfhostedClassic'),
    path('index--selfhosted/', views.selfhostedPage, name='selfhosted'),
    path('index--youtube-classic/', views.youtubeClassicPage, name='youtubeClassic'),
    path('index--youtube/', views.youtubePage, name='youtube'),
    path('cloudcomputing/', views.cloudPage, name='cloudcomputing'),
    path('courses/', views.courses, name='courses'),
    path('course2/', views.course2, name='course2'),
    path('course3/', views.course3, name='course3'),
    path('course4/', views.course4, name='course4'),
    path('course5/', views.course5, name='course5'),
    path('course6/', views.course6, name='course6'),
    path('course7/', views.course7, name='course7'),
    path('pastevents/', views.pasteventsPage, name='pastevents'),
    path('registration/', views.registration_view, name='registration_view'),
    path('success/', views.success_page, name='success'),
   
]