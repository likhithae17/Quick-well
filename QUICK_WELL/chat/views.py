from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
import json
#from .forms import PatientdetailsForm
from django.db import models
from .models import Patientdetails
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/')
def index(request):
    return render(request, 'chat/form.html', {})

@login_required(login_url='http://127.0.0.1:8000/')
def form(request):
    return render(request, 'chat/form.html')

@login_required
def consult(request):
    print("Request objects: {}".format(request.POST))
    #patient=request.POST['patient']
    patientname=request.POST['patientname']
    email=request.POST['email']
    symptoms = request.POST['symptoms']
    Department = request.POST['Department']

    patientdetails = Patientdetails.objects.create(patientname=patientname,email=email,symptoms=symptoms,Department=Department)
    patientdetails.save()
    return render(request, 'chat/Students_list.html')


@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })