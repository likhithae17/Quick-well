from django.conf.urls import url
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    re_path('^$', views.index, name="credits.index"),
    path('pay/', views.pay, name="credits.pay"),
    path('key/', views.key, name="credits.key"),
]
