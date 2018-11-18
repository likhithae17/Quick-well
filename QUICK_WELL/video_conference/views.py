from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import random
import webbrowser
import os
from .forms import *
from .models import *


def requester(request):

    if request.method == 'POST':
        form = video_requestForm(request.POST)
        if form.is_valid():
            t = video_request(requester = form.cleaned_data['username'])
            t.save()
            return render(request, 'video_conference/conference.html' , {'form':form})

    else:
        form = video_requestForm()
    return render(request,'video_conference/request.html',{'form':form})

def login(request):
    cd = random.randint(100000, 9999999)
    os.system("start \"\" http://appr.tc/r/"+str(cd))

def Mail(request):
    x = User.objects.all()
    lis=[]
    for a in x:
        lis.append(a.email)
    for i in range(0,len(lis)):
        res = send_mail("Health Tips", "Today's health tip : drink 8 cups of water minimum a day.", "qucikwelldoctor@gmail.com", [lis[i]])
    return HttpResponse('tip sent')
'''
def email_one(request):
    subject = "I am a text email"
    to = ['jaswanth.b17@iiits.in']
    from_email = 'b.jaswanth6@gmail.in'

    ctx = {
        'user': 'buddy',
        'purchase': 'Books'
    }

    message = render_to_string('blog/email.txt', ctx)

    EmailMessage(subject, message, to=to, from_email=from_email).send()

    return HttpResponse('email_one')'''