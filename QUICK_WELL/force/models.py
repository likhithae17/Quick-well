from django.db import models
# Create your models here.
'''class userlog(models.Model):
    userlogid = models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class equationlog(models.Model):
    mass = models.FloatField(null=False)
    acceleration = models.FloatField(null=False)
    force = models.FloatField(null=False)
    userlogid = models.ForeignKey(userlog, on_delete=models.PROTECT)'''

class user_profile(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    email = models.CharField(max_length=150)
    contact_number = models.BigIntegerField(null=False)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.BigIntegerField()
    photo = models.ImageField(upload_to='media', blank=True)

class user_appointment(models.Model):
    name = models.CharField(max_length=150)
    doctor = models.CharField(max_length=150,null=True)
    age = models.IntegerField()
    email = models.CharField(max_length=150)
    contact_number = models.BigIntegerField(null=False)
    specialisations = models.CharField(max_length=500)