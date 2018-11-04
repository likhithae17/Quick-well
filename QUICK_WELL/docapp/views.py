
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Specialization,Doctor
from django.db.models import Q

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
    return render(request, 'docapp/detail.html', {'doctor': doc})
    #return render(request,'docapp/index.html')


def detail(request,spec_id):
    spec = get_object_or_404(Specialization,pk=spec_id)
    query = request.GET.get('q')
    if query:
        spec = Specialization.objects.first(title__icontains=query)

    return render(request, 'docapp/detail.html', {'specialization':spec})


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
    template_name = 'docapp/detail.html'
    
    def get_queryset(self):
        self.spec = get_object_or_404(Specialization, pk=self.kwargs['pk'])
        return Specialization.objects.filter(spec_name__icontains='str(self.spec)')

"""


