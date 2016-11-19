from django.shortcuts import render
from .models import Cemetery
from django.utils import timezone


def cemetery_list(request):
    cemeteries=Cemetery.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    dates_only=Cemetery.objects.filter(date_created__lte=timezone.now())
    return render(request, 'heaven/cemetery_list.html', {'cemeteries':cemeteries})
