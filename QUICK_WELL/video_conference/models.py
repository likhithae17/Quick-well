
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class video_con_request(models.Model):
    requester = models.ForeignKey(User,on_delete=models.CASCADE)
    date_requested = models.DateTimeField(default=timezone.now)
  #  video_con_id =
   # requester = models.ForeignKey(User,on_delete=models.CASCADE)

class video_con_pass(models.Model):
    patient = models.ForeignKey(User.username,on_delete=models.CASCADE)
    date_conference = models.DateTimeField(default=timezone.now)

