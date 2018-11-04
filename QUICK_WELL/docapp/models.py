from django.db import models
from django.urls import reverse

class Specialization(models.Model):
    spec_name = models.CharField(max_length=150)

    def __str__(self):
        return self.spec_name

    #def get_absolute_url(self):
    #    return reverse('docapp:detail',kwargs={'pk':self.pk})

class Doctor(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    experience = models.FloatField(null=True)
    doc_photo = models.CharField(max_length=500, null=True,blank=True)
    email_id = models.CharField(max_length=150,null=True,blank=True)
    phone_num = models.BigIntegerField(null=True,blank=True)
    #previous_hospitals = models.CharField(max_length=300,null=True)
    spec = models.ForeignKey(Specialization, on_delete=models.PROTECT)

    def __str__(self):
        return self.firstname+' '+self.lastname+' - '+str(self.spec)

class Qualification(models.Model):
    doc_name = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    qual_name = models.CharField(max_length=500)
    institute_name = models.CharField(max_length=500,null=True)
    procurement_year = models.DateField()


class Hospital_Affiliation(models.Model):
    doc_name = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    hosp_name = models.CharField(max_length=200)
    hosp_photo = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class Office(models.Model):
    doc_id = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    hosp_affiliation_id = models.ForeignKey(Hospital_Affiliation, on_delete=models.PROTECT,null=True)
    time_slot_per_patient = models.FloatField(null=False)
    first_fee = models.FloatField(null=False)
    followup_fee = models.FloatField(null=False)
    street_address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.BigIntegerField()


class Office_Docavailability(models.Model):
    office_id = models.ForeignKey(Office, on_delete=models.PROTECT)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    day = models.CharField(max_length=20)
    is_available = models.BooleanField(default=False)
    reason_unavailability = models.CharField(max_length=500,null=True)

"""
class insurance(models.Model):
    insurance_name = models.CharField(max_length=100)
    office_id = models.ForeignKey(doctor, on_delete=models.PROTECT)
"""

class User(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    age = models.FloatField()
    dob = models.DateField(null=True)
    email = models.CharField(max_length=150)
    contact_number = models.BigIntegerField(null=False)
    street_address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.BigIntegerField()


class User_Review(models.Model):
    client_accountid = models.ForeignKey(User, on_delete=models.PROTECT)
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
    client_accountid = models.ForeignKey(User, on_delete=models.PROTECT)
    office_id = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    start_time =  models.DateTimeField()
    end_time =  models.DateTimeField()
    appoint_status_id = models.ForeignKey(Appointment_Status, on_delete=models.PROTECT)
    appoint_date = models.DateField(null=False)
