from django.urls import path
from django.contrib import admin
from . import views
from .views import Login_Page, register

urlpatterns = [
    path("", views.profile, name="profile"),
    path('upload/', views.resume, name='resume'),
    path('welcome/',views.Login_Page, name='Login_Page'),
    path('register/', views.register, name='register'),
    path("testPath/", views.testPath, name="testPath"),
  
] 