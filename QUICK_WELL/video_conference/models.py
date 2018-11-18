
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class video_con_request(models.Model):
    requester = models.ForeignKey(User,on_delete=models.CASCADE)
   # doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add= True)
    requeste_id = models.CharField(max_length=120)

class video_con_pass(models.Model):
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    date_conference = models.DateTimeField(default=timezone.now)
    #doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    conference_link = models.CharField(max_length=120)

