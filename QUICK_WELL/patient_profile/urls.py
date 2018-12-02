from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #re_path('^form/$', views.profile, name="patient_profile.profile"),
    path('signup/', views.signup_view, name="patient_profile.signup"),
    path('create/', views.create, name="patient_profile.create"),
    path('login/', views.login, name="patient_profile.login"),
    path('logout/', auth_views.LogoutView.as_view(template_name=''), name="patient_profile.logout"),
    path('change-password/', views.change_password, name="change_password"),
    path('details/', views.view_profile, name="patient_profile.details"),
   # path('Appointment/', views.view_appointment, name="Appointment"),
    #path('userprofile/', views.userprofile,name="patient_profile.userprofile"),
    path('test/', views.test, name="patient_profile.test"),
]
