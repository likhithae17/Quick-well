from django.contrib import admin
from .models import video_con_request,video_con_pass
#from video_conference.models import video_con_request
 #Register your models here.
admin.site.register(video_con_request)
admin.site.register(video_con_pass)
