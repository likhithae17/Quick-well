from django.urls import include, path
from . import views

#app_name = 'funding'

urlpatterns = [

    path('', views.index, name='index'),
    path('startproject', views.startproject, name='startproject'),

]