from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


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


class user_profile(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
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


class fundraiser(models.Model):
    user_name = models.ForeignKey(user_profile,on_delete=models.PROTECT)
    category = models.CharField(max_length=50)
    Title = models.CharField(max_length=60)
    goal_amount = models.FloatField()
    beneficiary_name = models.CharField(max_length=50)
    beneficiary_relation = models.CharField(max_length=25)
    Fundraiser_story = models.TextField()
    End_date = models.DateField()

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    pharmacy = models.CharField(max_length=100)
    about = models.CharField(max_length=1000, default='0000000')
    description = models.CharField(max_length=1000)
    mfg_date = models.DateField(null=True)
    exp_date = models.DateField(null=True)
    pres_req = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name + ' - ' + self.pharmacy


class PurchaseItem(models.Model):
    ref_code = models.CharField(max_length=15, default='0000000')
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True, unique=None)
    quantity = models.IntegerField(null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(null=True)
    date_ordered = models.DateTimeField(null=True)




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine, blank=True)
    first_name = models.CharField(max_length=100, default='0000000')
    last_name = models.CharField(max_length=100, default='0000000')
    bio = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=200, blank=False, default='')
    interests = models.CharField(max_length=255, blank=True)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(PurchaseItem)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        sum = 0 ;
        for item in self.items.all():
            sum = sum + ((item.medicine.price)*(item.quantity))
        return sum

