
from django.db import models
from django.utils import timezone
from django.contrin.auth.models import User

class User(models.Model):
    User_Name = models.CharField(max_length=150),
    User_Email = models.CharField(max_length=150),
 

 class video_con_request(models.Model):
     requester = models.ForeignKey(User),
     date_requested = models.DateTimeField(default=timezone.now),
     requester = models.ForeignKey(User,on_delete=models.CASCADE()),
