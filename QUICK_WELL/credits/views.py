from django.shortcuts import render
from django.http import HttpResponse
from .models import Balance,Pay
from django.core.mail import send_mail
from django.conf import settings
import random
import string

def index(request):
    balances = Balance.objects.filter(userid=1)
    print(balances)
    balance = {'bal': balances}
    return render(request, 'credits/index.html', context=balance)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def pay(request):
    amount = request.POST['amount']
    key = id_generator()
    Pay.objects.create(userid=1,key=key,amount=amount)
    subject = 'Payment'
    message = ('This key for confirmation {}'.format(key))
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['Recipient email',]
    send_mail( subject, message, email_from, recipient_list)
    

def key(request):
    pay_key = request.POST['pay_key']
    temp1 = Pay.objects.get(userid=1)
    amount = temp1.amount
    if pay_key == temp1.key:
        temp = AccountBalance.objects.get(userid=1)
        y1 = float(temp.balance) + float(amount)
        user_bal_update = Balance.objects.filter(name=admin).update(balance=y1)
        return HttpResponse("Success")
    else:
        return HttpResponse("Incorrect key")
