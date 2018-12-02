from django.shortcuts import render, redirect
from .models import user_profile, user_appointment
#from ..docapp.models import Appointment
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import Signup_form
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as out
from django.contrib.auth import update_session_auth_hash
import random

def signup_view(request):
    if request.method == 'POST':
        form = Signup_form(request.POST)
        if form.is_valid():
            form1 = form.save()
            otp = random.randint(100000, 999999)
            # Mail(request, form.email)
            send_mail("hello patient", str(otp), "quickwelldoctor@gmail.com", [form1.email])
            return redirect("home:home")
            #return HttpResponse("registered")
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    else:
        form = Signup_form()
    return render(request, 'patient_profile/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('working')
            user = form.get_user()
            auth_login(request, user)
            return HttpResponseRedirect("http://127.0.0.1:8000/patient_profile/create/")
    else:
        form = AuthenticationForm()
    return render(request, 'patient_profile/login.html', {'form': form})

def logout(request):
    if request.method == "POST":
        out(request)
    return HttpResponseRedirect("http://127.0.0.1:8000/patient_profile/create/")

def test(request):
    return render(request, 'patient_profile/test.html')

@login_required(login_url="http://127.0.0.1:8000/patient_profile/login/")
def view_profile(request):
    if request.method == "GET":
        uname = request.user
        profile = request.GET.get('profile')
        viewdetails = user_profile.objects.get(username=uname)
        context = {'details': viewdetails}
        if str(profile) == "profile":
            context['dask'] = 1
        return render(request, 'patient_profile/test.html', context)
    else:
        uname = request.user
        print('working', uname)
        viewdetails = user_profile.objects.get(username=uname)
        return render(request, 'patient_profile/test.html', {'details': viewdetails})


def create(request):
    if request.method == "POST":
        form = forms.profile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/patient_profile/details/")
    else:
        form = forms.profile()
    return render(request, 'patient_profile/profile.html', {'form': form})

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("/patient_profile/details/")
        else:
            return redirect('/patient_profile/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'patient_profile/change_password.html', args)








