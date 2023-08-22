from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def photo_list(request):
    return render(request, 'photo_list.html', {})