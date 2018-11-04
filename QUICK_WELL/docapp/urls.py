from django.urls import re_path, include, path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    #/music/<album_id>/
    re_path('(?P<spec_id>[0-9])/', views.detail, name='detail'),

    #path('spec/add/',views.SpecializationCreate.as_view(), name='spec-add'),

    #/music/<album_id>/favorite/
    #re_path('(?P<album_id>[0-9])/favorite/$', views.favorite, name='favorite'),
]