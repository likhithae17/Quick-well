
from django.shortcuts import render, redirect, get_object_or_404
from home.models import user_profile
from home.models import user_reports
#from ..docapp.models import Appointment
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import Signup_form, profile_update

from django.shortcuts import render, redirect
from home.models import *
from django.db.models import Avg, IntegerField
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import Signup_form, Patient_Update_Form, passwordchange, ReviewForm

from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as out
from django.template.loader import render_to_string
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
        form = AuthenticationForm
    return render(request, 'patient_profile/login.html', {'form': form})

def logout(request):
    if request.method == "POST":
        out(request)
    return HttpResponseRedirect("http://127.0.0.1:8000/patient_profile/create/")

def forgot_pass(request):
    return render(request, 'registration/password_reset_form.html')

def test(request):
    return render(request, 'patient_profile/test.html')

@login_required(login_url="http://127.0.0.1:8000/patient_profile/login/")
def view_profile(request):
    if request.method == "GET":
        uname = request.user
        profile = request.GET.get('profile')
        viewdetails = user_profile.objects.get(username=uname)
        context = {'details': viewdetails}
        viewreports = user_reports.objects.filter(username=uname)
        context['reports'] = viewreports
        if str(profile) == "profile":
            context['dask'] = 1
        elif str(request.GET.get('reports')) == "reports":
            context['dask1'] = 1
        elif str(request.GET.get('appointment')) == "appointment":
            context['dask2'] = 1
        return render(request, 'patient_profile/test.html', context)
    else:
        uname = request.user
        print('working', uname)
        viewdetails = user_profile.objects.get(username=uname)
        return render(request, 'patient_profile/test.html', {'details': viewdetails})

@login_required(login_url="http://127.0.0.1:8000/patient_profile/login/")
def reports(request):
    if request.method== "GET":
        uname = request.user
        print("hello", uname)
        viewreports = user_reports.objects.filter(username=uname)
        context = {'reports': viewreports}
        context['dask1'] = 1
        print('hello', context)
        return render(request, 'patient_profile/test.html', context)
    else:
        uname = request.user.username
        print('working', uname)
        viewreports = user_reports.objects.get(username=uname)
        return render(request, 'patient_profile/test.html', {'reports': viewreports})

def appointment1(request):
    uname = request.user
    viewappointment = Appointment.objects.filter(user_name=uname)
    profile = user_profile.objects.get(username=uname)
    #return HttpResponse("app")
    return render(request, 'patient_profile/app.html', {'appointment': viewappointment, 'details': profile})

def labtest(request):
    uname = request.user
    viewlab_test = LabTest.objects.filter(user_name=uname)
    profile = user_profile.objects.get(username=uname)
    # return HttpResponse("app")
    return render(request, 'patient_profile/lab_test.html', {'lab_test': viewlab_test, 'details': profile})



@login_required(login_url="http://127.0.0.1:8000/patient_profile/login/")
def create(request):
    if request.method == "POST":
        form = forms.profile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/patient_profile/details/")
        else:
            print(form.errors)
    else:
        form = forms.profile()
    return render(request, 'patient_profile/profile.html', {'form': form})

@login_required(login_url="http://127.0.0.1:8000/patient_profile/login/")
def upload(request):
    if request.user.username == "lab_admin":
        if request.method == "POST":
            form = forms.upload(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("uploaded")
                #return HttpResponseRedirect("/patient_profile/details/")
        else:
            form = forms.upload()
        return render(request, 'patient_profile/upl_lab.html', {'form1': form})
    return HttpResponse("you have no privilage")

def patient_update(request):
    temp = 1
    pat = get_object_or_404(user_profile, username=request.user)
    if request.method == 'POST':
        prof_form = profile_update(request.POST, instance=request.user or None)
        if prof_form.is_valid():
            prof_form.save()
            return HttpResponse("done")
    else:
        prof_form = profile_update(instance=request.user)
    return render(request, 'patient_profile/profile_update.html', {'prof_form': prof_form, 'temp': temp, 'pat': pat})





def change_password(request):
    if request.method == 'POST':
        change_form = passwordchange(data=request.POST, user=request.user)
        if change_form.is_valid():
            change_form.save()
            update_session_auth_hash(request, change_form.user)
            return HttpResponse('Done')
    else:
        change_form = passwordchange(user=request.user)
    return render(request, 'accounts/changepassword.html', {'change_form': change_form})


@login_required(login_url="http://127.0.0.1:8000/patient_profile/login/")
def reviews(request):
    rate = User_Review.objects.all()
    if request.method == 'POST':
        f = ReviewForm(request.POST)
        review_details = User_Review.objects.order_by('review_date')
        if f.is_valid():
            F= f.save(commit=False)
            try:
                obj1 = User_Review.objects.get( client_accountid=F.patient_id,  doctorid=F.doc_id)
                obj1.rating = F.rating
                obj1.review_date = F.review_date
                obj1.comment = F.comment
                obj1.save()
            except:
                F.save()
        a = []
        doctor = Doctor.objects.all()
        count = Doctor.objects.all().count()
        for i in range(0, count):
            b = User_Review.objects.filter(doc_id=doctor[i]).aggregate(Avg('rating', output_field=IntegerField()))
            a.append(b)
        print(a)

        return render(request, 'patient_profile/doctor_rating.html', {'doc_id': doctor, 'rating': a, 'comment': rate})
    else:
        f = ReviewForm()
        return render(request, 'patient_profile/review.html', {'form': f})

'''
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
        return render(request, 'patient_profile/change_password.html', args)'''








