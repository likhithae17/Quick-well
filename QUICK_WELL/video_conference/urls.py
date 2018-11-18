from django.urls import path
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path('', views.requester, name='video-request'),
    path('mail', views.Mail),
    path('call',views.login,name='call'),
    #path('login',login)
]