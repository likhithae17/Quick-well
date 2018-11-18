from django.urls import path
from . import views
from django.contrib.auth.views import auth_login
urlpatterns = [
    #path('', views.home, name='video-request'),
    path('mail', views.Mail),
    #path('login',login)
]