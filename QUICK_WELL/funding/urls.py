from django.urls import include, path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('startproject', views.startproject, name='startproject'),

]