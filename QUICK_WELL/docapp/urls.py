from django.urls import re_path, include, path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:pk>/', views.appbooking, name='appbooking'),
    path('hospitalnearme/', views.maps, name='maps'),
    path('greet/', views.greet, name='greet'),

    #path('book/<int:pk>/', views.confirm, name='confirm'),
    # re_path('appbooking/?P<pk>[0-9]/',views.appbooking,name='appbooking'),
    # path('spec/add/',views.SpecializationCreate.as_view(), name='spec-add'),

    # /music/<album_id>/favorite/
    # re_path('(?P<album_id>[0-9])/favorite/$', views.favorite, name='favorite'),
]