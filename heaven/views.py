from django.shortcuts import render
from .models import Cemetery, Burial
from django.utils import timezone

def home(request):
    return render(request,'heaven/home.html')

def cemetery(request):
    return render(request, 'heaven/base_cemetery.html', {})

def cemetery_list(request):
    cemeteries=Cemetery.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, 'heaven/cemetery_list.html', {'cemeteries':cemeteries})

def burial(request):
    return render(request, 'heaven/base_burial.html', {})

def burial_list(request):
    burials=Burial.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, 'heaven/burial_list.html', {'burials':burials})


