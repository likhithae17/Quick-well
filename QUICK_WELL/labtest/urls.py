from django.urls import re_path, include, path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    #path('<int:pk>/', views.labbooking, name='labbooking'),
    #path('greet/', views.greet, name='greet'),

]