from django.shortcuts import render, redirect
from .models import user_profile, user_appointment
from . import forms
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login as auth_login, logout as out

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
    else:
        form = AuthenticationForm()
    return render(request, 'force/login.html', {'form': form})
def logout(request):
    if request.method == "POST":
        out(request)
    return HttpResponse("logged out")

def test(request):
    return render(request, 'force/test.html')
'''
def index(request):
    return render(request,'force/profile.html')'''
'''
def result(request):
    print("Request Object:{}".format(request.POST))
    name = request.POST['name']
    age= request.POST['age']
    dob = request.POST['dob']
    email = request.POST['email']
    contact_number = request.POST['contact_number']
    Street = request.POST['address']
    City = request.POST['city']
    District = request.POST['district']
    State = request.POST['state']
    Country = request.POST['country']
    Zipcode = request.POST['code']
    photo = request.FILES['Photo']
    user_profile.objects.create(name=name,age=age,dob=dob,email=email,contact_number=contact_number,street_address=Street,city=City,district=District,state=State,country=Country,zipcode=Zipcode,Photo=photo)
    return HttpResponse("saved")
'''
def view_profile(request):
    if request.method == "GET":

        # uname = request.user
        profile = request.GET.get('profile')
        viewdetails = user_profile.objects.get(name='rohit')
        context = {'details': viewdetails}
        if str(profile) == "profile":
            context['dask'] = 1
        return render(request, 'force/test.html', context)

    else:
        #uname = request.user
        viewdetails = user_profile.objects.get(name='rohit')
        return render(request, 'force/test.html', {'details': viewdetails})

def view_appointment(request):
    if request.method == "GET":
        #uname = request.user
        appointment = request.GET.get('appointment')
        viewappointment = user_appointment.objects.get(name='rohit')
        context = {'details': viewappointment}
        if str(appointment) == "appointment":
            context['dask2'] = 1
        return render(request, 'force/test.html', context)
    else:
        #uname = request.user
        viewappointment = user_profile.objects.get(name='rohit')
        return render(request, 'force/test.html', {'details': viewappointment})

'''
def userprofile(request):
    profile_details = user_profile.objects.get(name='sivakrishna
    ')
    return render(request, 'force/profile.html',{'details':profile_details})'''


def create(request):
    if request.method == "POST":
        form = forms.profile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
    else:
        form = forms.profile()
    return render(request, 'force/profile.html', {'form': form})

