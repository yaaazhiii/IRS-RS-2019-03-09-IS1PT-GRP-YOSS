from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

debug = True

def welcome(request):
    # This is the first html page
    return render(request, 'Scheduler/welcome.html')

def calendar(request):
    # This is the first html page    

    return render(request, 'Scheduler/calendar.html')

def file(request):
    # This is the first html page
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)


    return render(request, 'Scheduler/file.html')