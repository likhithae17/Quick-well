from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import ListView, DetailView
#from .models import Post

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.login, name="login"),
<<<<<<< HEAD
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name=''), name="logout"),
=======
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name=""), name="logout"),
>>>>>>> 3dd6410621cc3d6328ae3b93af42a9ae108a22be
    url(r'^signup4/$', views.register, name="signup4"),
    url(r'^home/', views.index, name='index'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^test', views.test, name='test'),
    url(r'^temp/verify/$', views.mail_conf, name="verify"),
    #    url(r'^advt', views.advt, name='advt'),
#    url(r'^blog', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:10], template_name="profile/includes/blog.html")),
#    url(r'^blog/blog/(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='profile/includes/post.html'))
]