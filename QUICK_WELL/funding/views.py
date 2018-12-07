from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import EmailMessage
from .forms import fundraiserForm
from home.models import fundraiser,user_profile


def index(request):
    return render(request, 'funding/index.html')


@login_required(login_url='/login/')
def startproject(request):
    #user = get_object_or_404(user_profile, id=int(request.user))

    if request.method == 'POST':
        form = fundraiserForm(request.POST)

        if form.is_valid():

            category = form.cleaned_data['category']
            Title = form.cleaned_data['Title']
            goal_amount = form.cleaned_data['goal_amount']
            beneficiary_name = form.cleaned_data['beneficiary_name']
            beneficary_relation = form.cleaned_data['beneficiary_relation']
            Fundraiser_story = form.cleaned_data['Fundraiser_story']
            End_date = form.cleaned_data['End_date']

            #temp = fundraiser.objects.create(user_name=user, category=category, Title=Title, goal_amount=goal_amount, beneficiary_name=beneficiary_name, beneficiary_relation=beneficary_relation, Fundraiser_story=Fundraiser_story, End_date=End_date  )

            return HttpResponse('<h2>Thank you for creating a fundraiser</h2>')

    else:
        form = fundraiserForm()

    return render(request, 'funding/startproject.html', {'form': form})

