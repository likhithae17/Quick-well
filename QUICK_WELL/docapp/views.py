#API KEY for geolocation - AIzaSyBBDDHXhrCzm5a2cemyN2QtIb8B11hvHQE
#API Key for calendar  --  AIzaSyAMumSF2Rkulpco3sQ-LWvtfwFEzAn0j7o

#CLIENT ID -  798679894892-qa3o7qpo5l5g923qd6sdfvku2u0hi7fh.apps.googleusercontent.com
#CLIENT SECRET - Xedby0HI2bczZrVHt1-Bfs_3

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Specialization, Doctor, Office_Docavailability, Office, Appointment,LabTest, Tests_info

from django.core.mail import EmailMessage

from .forms import AppointmentForm
#from . import ref
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
    if query:
        doc = Doctor.objects.filter(firstname__icontains=query)
        if not doc:
            doc = Doctor.objects.filter(lastname__icontains=query)
            if not doc:
                doc = Doctor.objects.filter(spec__spec_name__icontains=query)
    else:
        doc = Doctor.objects.all()
    return render(request, 'docapp/index.html', {'doctor': doc})



def detail(request,spec_id):
    spec = get_object_or_404(Specialization,pk=spec_id)

    #query = request.GET.get('q')
    #if query:
     #   spec = Specialization.objects.first(title__icontains=query)

    return render(request, 'docapp/index.html', {'specialization':spec})

def maps(request):
    return render(request, 'docapp/maps.html')


# def appbooking(request,pk):
#     doc = get_object_or_404(Doctor, pk=pk)
#     app = get_object_or_404(Office_Docavailability, pk=pk)
#     return render(request, 'docapp/booking.html', {'doctor':doc, 'appbook':app})

def profile(request,pk):
    doc = get_object_or_404(Doctor, pk=pk)
    return render(request, 'profile/includes/basic.html', {'doc':doc})

def appbooking(request,pk):
    doc = get_object_or_404(Doctor, pk=pk)
    office = get_object_or_404(Office, pk=pk)
    app = get_object_or_404(Office_Docavailability, pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            user_name = form.cleaned_data['user_name']
            email_id = form.cleaned_data['email_id']
            #appoint_no = ref.generate_app_id()

            temp = Appointment.objects.create(date=date, time=time, user_name=user_name, email_id=email_id, office_id=office)

            subject = "Appointment booked"
            to_email = email_id
            print(to_email)
            context = {
                'name': user_name,
                #'Appointment_id':appoint_no,
                'time':time,
                'date': date,
                'doctor':doc,
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

    return render(request, 'docapp/booking.html', {'form': form,'doctor':doc, 'appbook':app})


def confirm(request,pk):
    doc = get_object_or_404(Doctor, pk=pk)
    #slot_selected = slot
    return render(request, 'docapp/confirm.html',{'doctor':doc})

def greet(request):
    return render(request, 'docapp/greet.html')
"""

from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Specialization
from django.views.generic.edit import CreateView, UpdateView,DeleteView
#from django.db.models import Q


class IndexView(generic.ListView):
    template_name = 'docapp/index.html'
    #context_object_name = 'all_specialization'

    def get_queryset(self):
        return Specialization.objects.all()

class DetailView(generic.DetailView):
    model = Specialization
    template_name = 'docapp/index.html'
    
    def get_queryset(self):
        self.spec = get_object_or_404(Specialization, pk=self.kwargs['pk'])
        return Specialization.objects.filter(spec_name__icontains='str(self.spec)')

"""


