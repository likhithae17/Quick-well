from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def home(request):
    return HttpResponse('<h1>this is video conference page</h1>')


def Mail(request):
   res = send_mail("hello karthik", "hi  ra", "b.jaswanth6@gmail.com", ['jaswanth.b17@iiits.in'])
   return HttpResponse('%s'%res)

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

    return HttpResponse('email_one')