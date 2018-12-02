from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Doctor(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    experience = models.IntegerField(null=True)
    doc_photo = models.FileField(null=True)
    email_id = models.CharField(max_length=150,null=True,blank=True)
    phone_num = models.BigIntegerField(null=True,blank=True)
    #previous_hospitals = models.CharField(max_length=300,null=True)
    specialization = models.CharField(max_length=150)

    def __str__(self):
        return self.firstname+' '+self.lastname+' - '+str(self.specialization)

class Tests_info(models.Model):
    test_name = models.CharField(max_length=150)
    preparation = models.TextField()
    procedure = models.TextField()
    cost = models.FloatField()


class LabTest(models.Model):
    lab_name = models.CharField(max_length=150)
    lab_photo = models.FileField(null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    phone_num = models.BigIntegerField(null=True, blank=True)
    tests_available = models.ManyToManyField(Tests_info)


class Qualification(models.Model):
    doc_name = models.ManyToManyField(Doctor)
    qual_name = models.CharField(max_length=500)
    institute_name = models.CharField(max_length=500,null=True)
    procurement_year = models.DateField()


class Hospital_Affiliation(models.Model):
    doc_name = models.ManyToManyField(Doctor,default='')
    hosp_name = models.CharField(max_length=200)
    hosp_photo = models.CharField(max_length=500, null=True,blank=True)
    city = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=300,blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.hosp_name

class Office(models.Model):
    doc_id = models.ForeignKey(Doctor, on_delete=models.PROTECT,null=True,blank = True)
    hosp_affiliation_id = models.ForeignKey(Hospital_Affiliation, on_delete=models.PROTECT,null=True,blank=True)
    first_fee = models.FloatField(null=False)
    followup_fee = models.FloatField(null=False)
    street_address = models.CharField(max_length=500,blank=True)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    zip = models.BigIntegerField(blank=True)

    def __str__(self):
        return str(self.doc_id)


class Office_Docavailability(models.Model):
    office_id = models.ForeignKey(Office, on_delete=models.PROTECT)
    time_slot_per_patient = models.FloatField(null=True, blank=True)


    day = models.CharField(max_length=20)
    reason_unavailability = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return str(self.office_id)

"""
class insurance(models.Model):
    insurance_name = models.CharField(max_length=100)
    office_id = models.ForeignKey(doctor, on_delete=models.PROTECT)
"""

class user_profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
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


class User_Review(models.Model):
    client_accountid = models.ForeignKey(user_profile, on_delete=models.PROTECT)
    doc_id = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    is_anonymous = models.BooleanField(default=False)
    wait_time_rating = models.FloatField(null=True)
    manner_rating = models.FloatField(null=True)
    rating = models.FloatField(null=True)
    review = models.CharField(max_length=500,null=True)
    is_doc_recommended = models.BooleanField(default=True)
    review_date = models.DateField()


class Appointment_Status(models.Model):
    status = models.CharField(max_length=20)


class Appointment(models.Model):
    #client_accountid = models.ForeignKey(User, on_delete=models.PROTECT)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    #start_time =  models.DateTimeField()
    #end_time =  models.DateTimeField()
    user_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    #appointment_id = models.CharField(blank=False, null=False, max_length=200)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    #appoint_status_id = models.ForeignKey(Appointment_Status, on_delete=models.PROTECT)



class labAppointment(models.Model):
    test_id = models.ForeignKey(Tests_info, on_delete=models.PROTECT)
    user_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    #appointment_id = models.CharField(blank=False, null=False, max_length=200)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    #appoint_status_id = models.ForeignKey(Appointment_Status, on_delete=models.PROTECT)

