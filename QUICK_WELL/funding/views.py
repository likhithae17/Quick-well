from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect


def index(request):
    return render(request, 'funding/index.html')

@login_required(login_url='/login/')
def startproject(request):

    return render(request, 'funding/startproject.html')