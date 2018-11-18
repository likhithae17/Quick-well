from django.shortcuts import render,get_object_or_404,redirect
from docapp.models import LabTest,Tests_info

# Create your views here.

def index(request):
    lab = LabTest.objects.all()
    return render(request, 'labtest/index.html', {'labs':lab})