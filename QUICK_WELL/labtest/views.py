from django.shortcuts import render,get_object_or_404,redirect
from home.models import LabTest,Tests_info,labAppointment
from django.core.mail import EmailMessage
from .forms import labAppointmentForm
#from . import ref
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    #lab = LabTest.objects.all()
    test = Tests_info.objects.all()
    query = request.GET.get('q')
    query1 = request.GET.get('q1')
    if query:
        test = Tests_info.objects.filter(test_name__icontains=query)
        if not test:
            test = Tests_info.objects.filter(cost__icontains=query)
    else:
        test = Tests_info.objects.all()

    return render(request, 'labtest/index.html', {'test':test, 'query': query1})


def detail(request,pk):
    test = get_object_or_404(Tests_info, pk=pk)
    lab = LabTest.objects.filter(tests_available__test_name__icontains=test)
    return render(request, 'labtest/details.html', {'lab':lab,'test':test})

def labbook(request,pk):
    test = get_object_or_404(Tests_info, pk=pk)
    lab = LabTest.objects.filter(tests_available__test_name__icontains=test)

    if request.method == 'POST':
        form = labAppointmentForm(request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            user_name = form.cleaned_data['user_name']
            email_id = form.cleaned_data['email_id']
            #appoint_no = ref.generate_app_id()

            sametest = labAppointment.objects.filter(test_id__id__icontains=test)
            flag = 1

            for slot in sametest:
                 if slot.date == date and slot.time == time:
                     error_msg='Sorry, this slot is not available please select a different slot!'
                     flag=0
                     #form = AppointmentForm()
                     print(date)
                     break;

            if flag==1:
                temp = labAppointment.objects.create(date=date, time=time, user_name=user_name, email_id=email_id, test_id=test)

                subject = "Appointment booked"
                to_email = email_id
                print(to_email)
                context = {
                    'name': user_name,
                    'time':time,
                    'date': date,
                    'test':test,
                    'appid': temp.id,
                }
                message = render_to_string('labtest/emailtxt.html', context)
                msg = EmailMessage(subject, message, to=[to_email])
                msg.content_subtype = 'html'

                try:
                    msg.send()
                    print('Successful')
                except:
                    print('Unsuccessful')

                return render(request, 'labtest/greet.html', context)

    else:
        form = labAppointmentForm()

    return render(request, 'labtest/booking.html', {'form': form,'test':test,})


def delete(request,appid):
    appointment = get_object_or_404(labAppointment, pk=appid)
    appointment.delete()
    msg = 'Your appointment is cancelled'
    return render(request, 'docapp/greet.html',{'msg':msg})