from django.shortcuts import render
from .models import Cemetery, Burial
from .forms import CemeteryForm, BurialForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.views import login
from django.contrib.auth.models import User


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


def cemetery_add(request):
    if request.method=='POST':
        form=CemeteryForm(request.POST)
        if form.is_valid():
            cemetery=form.save(commit=False)
            cemetery.name=request.POST.get('name')
            cemetery.city=request.POST.get('city')
            cemetery.zipcode=request.POST.get('zipcode')
            cemetery.date_created=timezone.now()
            if request.user.is_authenticated:
                cemetery.created_by=request.user
            else:
                return login(request)
            #cemetery_obj=Cemetery(name=name, city=city,zipcode=zipcode,created_by=created_by)
            cemetery.save()
            return redirect('cemetery_list')
    else:
        form=CemeteryForm
    return render(request,'heaven/edit_cemetery.html',{'form':form})

def burial_add(request):
    if request.method=="POST":
        form=BurialForm(request.POST)
        if form.is_valid():
            #create an instance of Cemetery

            burial=form.save(commit=False)
            burial.cemetery_id=Cemetery.objects.get(id=request.POST.get('cemetery_id'))
            burial.first_name=request.POST.get('first_name')
            burial.DoB=form.cleaned_data.get('DoB')
            burial.DoD=form.cleaned_data.get    ('DoD')
            burial.sex=request.POST.get('sex')
            burial.date_created=request.POST.get('date_created')
            if request.user.is_authenticated:
                burial.created_by=request.user
            else:
                return login(request)
            burial.save()
            return redirect('burial_list')
    else:
        form=BurialForm
    return render(request,'heaven/edit_burial.html',{'form':form})
