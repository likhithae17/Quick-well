from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #re_path('^form/$', views.profile, name="force.profile"),
    path('signup/', views.signup_view, name="force.signup"),
    path('create/', views.create, name="force.create"),
    path('login/', views.login, name="force.login"),
    path('logout/', auth_views.LogoutView.as_view(template_name=''), name="force.logout"),
    path('details/', views.view_profile, name="force.details"),
    #path('appointment/', views.view_appointment, name="force.appointment"),
    #path('userprofile/', views.userprofile,name="force.userprofile"),
    path('test/', views.test, name="force.test"),
]
