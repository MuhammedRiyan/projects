from django.shortcuts import render
from .models import Department
from .models import AboutUs
def home(request):
    return render(request, 'main/home.html') 

def about(request):
    return render(request, 'main/about.html')

def registration(request):
    return render(request, 'main/registration.html')

def home(request):
    departments = Department.objects.all()
    return render(request, 'main/home.html', {'departments': departments})
def about(request):
    about_data = AboutUs.objects.first() 
    return render(request, 'main/about.html', {'about': about_data})
