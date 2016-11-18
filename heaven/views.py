from django.shortcuts import render

def cemetery_list(request):
    return render(request, 'heaven/cemetery_list.html', {})
