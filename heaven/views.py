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

# -------- Cemetery ----------
def add_cemetery(request):
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
            return redirect('view_cemetery')
    else:
        form=CemeteryForm
    return render(request,'heaven/add_cemetery.html',{'form':form})

def view_cemetery(request):
    cemeteries=Cemetery.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, 'heaven/view_cemetery.html', {'cemeteries':cemeteries})

def edit_cemetery(request):
    return render(request, 'heaven/edit_cemetery.html', {})

def delete_cemetery(request):
    return render(request, 'heaven/delete_cemetery.html', {})

# -------- Burial ----------

def burial(request):
    return render(request, 'heaven/base_burial.html', {})

def add_burial(request):
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
            return redirect('view_burial')
    else:
        form=BurialForm
    return render(request,'heaven/add_burial.html',{'form':form})


def view_burial(request):
    burials=Burial.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, 'heaven/view_burial.html', {'burials':burials})

def edit_burial(request):
    return render(request, 'heaven/edit_burial.html', {})

def delete_burial(request):
    return render(request, 'heaven/delete_burial.html', {})

#---------- Photo ------------

def photo(request):
    return render(request, 'heaven/base_photo.html', {})

def add_photo(request):
    return render(request,'heaven/add_photo.html')

def view_photo(request):
    return render(request, 'heaven/view_photo.html')

def edit_photo(request):
    return render(request, 'heaven/edit_photo.html', {})

def delete_photo(request):
    return render(request, 'heaven/delete_photo.html', {})

