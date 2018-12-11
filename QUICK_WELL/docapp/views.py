#API KEY for geolocation - AIzaSyBBDDHXhrCzm5a2cemyN2QtIb8B11hvHQE
#API Key for calendar  --  AIzaSyAMumSF2Rkulpco3sQ-LWvtfwFEzAn0j7o

#CLIENT ID -  798679894892-qa3o7qpo5l5g923qd6sdfvku2u0hi7fh.apps.googleusercontent.com
#CLIENT SECRET - Xedby0HI2bczZrVHt1-Bfs_3


from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from home.models import Doctor, Appointment
from django.core.mail import EmailMessage
from .forms import AppointmentForm
from django.template.loader import render_to_string



#from googleapiclient import discovery
#from oauth2client import tools
#from oauth2client.client import OAuth2WebServerFlow
#from oauth2client.file import Storage
#import httplib


#from django.db.models import Q

def index(request):
    doc = Doctor.objects.all()
    query = request.GET.get('q')
    query1 = request.GET.get('q1')
    if query:
        doc = Doctor.objects.filter(firstname__icontains=query)
        if not doc:
            doc = Doctor.objects.filter(lastname__icontains=query)
            if not doc:
                doc = Doctor.objects.filter(specialization__icontains=query)
    else:
        doc = Doctor.objects.all()

    return render(request, 'docapp/index.html', {'doctor': doc, 'query': query1})


def maps(request):
    return render(request, 'docapp/maps.html')


def profile(request,pk):
    doc = get_object_or_404(Doctor, pk=pk)
    return render(request, 'docprof/includes/basic.html', {'doc':doc})

def index1(request):
    doc = Doctor.objects.all()
    query = request.GET.get('q')
    return render(request, 'docprof/includes/index.html' )

def contact(request):
    return render(request, 'docprof/includes/basic.html', {'content': ['contact me at', 'sandeshjatla@gmail.com']})

def test(request):
    return render(request, 'docprof/includes/test.html')


def appbooking(request,pk):
    doc = get_object_or_404(Doctor, pk=pk)
    docid = doc.id
    error_msg=''
    #office = get_object_or_404(Office, pk=pk)
    #app = get_object_or_404(Office_Docavailability, pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            user_name = form.cleaned_data['user_name']
            email_id = form.cleaned_data['email_id']

            #bookedslots = Appointment.objects.all()
            #for slot in  bookedslots:
            samedoc = Appointment.objects.filter(doctor_id__id__icontains=docid)
            flag=1

            for slot in samedoc:
                 if slot.date == date and slot.time == time:
                     error_msg='Sorry, this slot is not available please select a different slot!'
                     flag=0
                     #form = AppointmentForm()
                     print(date)
                     break;


            if flag==1:
                temp = Appointment.objects.create(date=date, time=time, user_name=user_name, email_id=email_id,doctor_id=doc)
                subject = "Appointment booked"
                to_email = email_id
                print(to_email)
                context = {
                    'name': user_name,
                    #'Appointment_id':appoint_no,
                    'time':time,
                    'date': date,
                    'doctor':doc,
                    'appid':temp.id,
                }
                message = render_to_string('docapp/emailtext.html', context)
                msg = EmailMessage(subject, message, to=[to_email])
                msg.content_subtype = 'html'

                try:
                    msg.send()
                    print('Successful')
                except:
                    print('Unsuccessful')

                return render(request, 'docapp/greet.html', context)

    else:
        form = AppointmentForm()

    return render(request, 'docapp/booking.html', {'form': form,'doctor':doc,'error':error_msg})


def confirm(request,pk):
    doc = get_object_or_404(Doctor, pk=pk)
    #slot_selected = slot
    return render(request, 'docapp/confirm.html',{'doctor':doc})


def greet(request):
    return render(request, 'docapp/greet.html')


def delete(request,pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    msg = 'Your appointment is cancelled'
    #return render(request, 'docapp/greet.html',{'msg':msg})
    return HttpResponse('<h2>Appointment cancelled</h2>')

