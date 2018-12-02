from django.urls import re_path, include, path
from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('<int:pk>', views.detail, name='details'),
    path('book/<int:pk>', views.labbook, name='labbook'),
    #path('<int:pk>/', views.labbooking, name='labbooking'),
    #path('greet/', views.greet, name='greet'),

]