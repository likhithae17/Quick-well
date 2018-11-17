from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form/$', views.form, name='form'),
    url(r'^consult/$', views.consult, name='consult'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),


]
