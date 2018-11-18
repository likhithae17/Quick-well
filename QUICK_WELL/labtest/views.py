from django.shortcuts import render,get_object_or_404,redirect
from docapp.models import LabTest,Tests_info

# Create your views here.


def index(request):
    #lab = LabTest.objects.all()
    test = Tests_info.objects.all()
    query = request.GET.get('q')
    if query:
        test = Tests_info.objects.filter(test_name__icontains=query)
        if not test:
            test = Tests_info.objects.filter(cost__icontains=query)
    else:
        test = Tests_info.objects.all()

    return render(request, 'labtest/index.html', {'test':test})


def detail(request,pk):
    test = get_object_or_404(Tests_info, pk=pk)
    lab = LabTest.objects.filter(tests_available__test_name__icontains=test)
    return render(request, 'labtest/details.html', {'lab':lab,'test':test})

