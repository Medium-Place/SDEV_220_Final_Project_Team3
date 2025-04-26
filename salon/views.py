from django.shortcuts import render
from .models import Service

def home_view(request):
    return render(request, 'VVStylesHome.html')

def services_view(request):
    return render(request, 'VVStylesServices.html')

def booking_view(request):
    return render(request, 'VVStylesBooking.html')
