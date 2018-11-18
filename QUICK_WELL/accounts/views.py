from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from .forms import *
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth import get_user_model, login as auth_login, logout as out, logout
from django.conf import settings
from .models import *
from django.contrib.auth import authenticate
import random

# def home(request):
#     return render(request, 'accounts/home.html')

def Mail(request,emailto):
   otp = random.randint(100000, 999999)
   res = send_mail("hello doctor", "Thanks for registering "+ str(otp) + " is your verification otp", "quickwelldoctor@gmail.com", [emailto], fail_silently=True)
   return HttpResponse('%s'%res)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
        else:
            return HttpResponse("invalid details!")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    # if request.method == "POST":
    #     out(request)
    # return HttpResponse("logged out")
    logout(request)
    return redirect('home:home')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = Signup_user_form(request.POST)
        profile_form = Signup_profile_form(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            UserForm = user_form.save()
            UserForm.set_password(UserForm.password)
            UserForm.save()
            ProfileForm = profile_form.save(commit=False)
            ProfileForm.user = UserForm
            ProfileForm.save()
            Mail(request, UserForm.email)
            registered = True
        else:
            return HttpResponse(form.errors)
    else:
        user_form = Signup_user_form()
        profile_form = Signup_profile_form()
    if registered:
        return HttpResponse("Successfully created your account")
    else:
        return render(request, 'accounts/signup4.html', {'user_form': user_form, 'profile_form': profile_form})

def index(request):
    doc = Profile.objects.all()
    query = request.GET.get('q')
    return render(request, 'profile/includes/index.html')

def contact(request):
    return render(request, 'profile/includes/basic.html', {'content': ['contact me at', 'sandeshjatla@gmail.com']})

def test(request):
    return render(request, 'profile/includes/test.html')

# def advt