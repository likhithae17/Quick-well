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
    experience = models.IntegerField(null=True)
    doc_photo = models.CharField(max_length=500, null=True,blank=True)
    email_id = models.CharField(max_length=150,null=True,blank=True)
    phone_num = models.BigIntegerField(null=True,blank=True)
    #previous_hospitals = models.CharField(max_length=300,null=True)
    spec = models.ForeignKey(Specialization, on_delete=models.PROTECT)

    def __str__(self):
        return self.firstname+' '+self.lastname+' - '+str(self.spec)

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
    slot1 = models.TimeField(default='9:00')
    slot1_available = models.BooleanField(default=True)
    slot2 = models.TimeField(default='9:15')
    slot2_available = models.BooleanField(default=True)
    slot3 = models.TimeField(default='9:30')
    slot3_available = models.BooleanField(default=True)
    slot4 = models.TimeField(default='9:45')
    slot4_available = models.BooleanField(default=True)
    slot5 = models.TimeField(default='10:00')
    slot5_available = models.BooleanField(default=True)
    slot6 = models.TimeField(default='10:15')
    slot6_available = models.BooleanField(default=True)
    slot7 = models.TimeField(default='10:30')
    slot7_available = models.BooleanField(default=True)
    slot8 = models.TimeField(default='10:45')
    slot8_available = models.BooleanField(default=True)
    slot9 = models.TimeField(default='11:00')
    slot9_available = models.BooleanField(default=True)
    slot10 = models.TimeField(default='11:15')
    slot10_available = models.BooleanField(default=True)
    slot11 = models.TimeField(default='11:30')
    slot11_available = models.BooleanField(default=True)
    slot12 = models.TimeField(default='11:45')
    slot12_available = models.BooleanField(default=True)
    slot13 = models.TimeField(default='12:00')
    slot13_available = models.BooleanField(default=True)
    slot14 = models.TimeField(default='12:15')
    slot14_available = models.BooleanField(default=True)
    slot15 = models.TimeField(default='12:30')
    slot15_available = models.BooleanField(default=True)
    slot16 = models.TimeField(default='12:45')
    slot16_available = models.BooleanField(default=True)
    slot17 = models.TimeField(default='13:00')
    slot17_available = models.BooleanField(default=True)
    slot18 = models.TimeField(default='13:15')
    slot18_available = models.BooleanField(default=True)
    slot19 = models.TimeField(default='13:30')
    slot19_available = models.BooleanField(default=True)
    slot20 = models.TimeField(default='13:45')
    slot20_available = models.BooleanField(default=True)
    slot21 = models.TimeField(default='14:00')
    slot21_available = models.BooleanField(default=True)
    slot22 = models.TimeField(default='14:15')
    slot22_available = models.BooleanField(default=True)
    slot23 = models.TimeField(default='14:30')
    slot23_available = models.BooleanField(default=True)
    slot24 = models.TimeField(default='14:45')
    slot24_available = models.BooleanField(default=True)
    slot25 = models.TimeField(default='15:00')
    slot25_available = models.BooleanField(default=True)
    slot26 = models.TimeField(default='15:15')
    slot26_available = models.BooleanField(default=True)
    slot27 = models.TimeField(default='15:30')
    slot27_available = models.BooleanField(default=True)
    slot28 = models.TimeField(default='15:45')
    slot28_available = models.BooleanField(default=True)
    slot29 = models.TimeField(default='16:00')
    slot29_available = models.BooleanField(default=True)
    slot30 = models.TimeField(default='16:15')
    slot30_available = models.BooleanField(default=True)
    slot31 = models.TimeField(default='16:30')
    slot31_available = models.BooleanField(default=True)
    slot32 = models.TimeField(default='16:45')
    slot32_available = models.BooleanField(default=True)
    slot33 = models.TimeField(default='17:00')
    slot33_available = models.BooleanField(default=True)
    slot34 = models.TimeField(default='17:15')
    slot34_available = models.BooleanField(default=True)
    slot35 = models.TimeField(default='17:30')
    slot35_available = models.BooleanField(default=True)
    slot36 = models.TimeField(default='17:45')
    slot36_available = models.BooleanField(default=True)
    slot37 = models.TimeField(default='18:00')
    slot37_available = models.BooleanField(default=True)
    slot38 = models.TimeField(default='18:15')
    slot38_available = models.BooleanField(default=True)
    slot39 = models.TimeField(default='18:30')
    slot39_available = models.BooleanField(default=True)
    slot40 = models.TimeField(default='18:45')
    slot40_available = models.BooleanField(default=True)
    slot41 = models.TimeField(default='19:00')
    slot41_available = models.BooleanField(default=True)
    slot42 = models.TimeField(default='19:15')
    slot42_available = models.BooleanField(default=True)
    slot43 = models.TimeField(default='19:30')
    slot43_available = models.BooleanField(default=True)
    slot44 = models.TimeField(default='19:45')
    slot44_available = models.BooleanField(default=True)
    slot45 = models.TimeField(default='20:00')
    slot45_available = models.BooleanField(default=True)
    slot46 = models.TimeField(default='20:15')
    slot46_available = models.BooleanField(default=True)
    slot47 = models.TimeField(default='20:30')
    slot47_available = models.BooleanField(default=True)
    slot48 = models.TimeField(default='20:45')
    slot48_available = models.BooleanField(default=True)
    slot49 = models.TimeField(default='21:00')
    slot49_available = models.BooleanField(default=True)
    slot50 = models.TimeField(default='21:15')
    slot50_available = models.BooleanField(default=True)
    slot51 = models.TimeField(default='21:30')
    slot51_available = models.BooleanField(default=True)
    slot52 = models.TimeField(default='21:45')
    slot53_available = models.BooleanField(default=True)
    slot54 = models.TimeField(default='22:00')
    slot54_available = models.BooleanField(default=True)
    day = models.CharField(max_length=20)
    reason_unavailability = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return str(self.office_id)

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
    #client_accountid = models.ForeignKey(User, on_delete=models.PROTECT)
    office_id = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    #start_time =  models.DateTimeField()
    #end_time =  models.DateTimeField()
    user_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    appointment_id = models.CharField(blank=False, null=False, max_length=200)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    #appoint_status_id = models.ForeignKey(Appointment_Status, on_delete=models.PROTECT)

    def __str__(self):
        return self.appointment_id