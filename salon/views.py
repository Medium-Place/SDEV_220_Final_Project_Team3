
from django.shortcuts import render, redirect
from .models import Service, Stylist, Customer, Appointment
import datetime




def home_view(request):
    return render(request, 'VVStylesHome.html')

def services_view(request):
    services = Service.objects.all()  # Get all services from database
    return render(request, 'VVStylesServices.html', {'services': services})  # Send them to the template

def booking_view(request):
    services = Service.objects.all()
    stylists = Stylist.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        stylist_id = request.POST.get('stylist')
        service_id = request.POST.get('service')

        if not stylist_id or not service_id:
            return render(request, 'VVStylesBooking.html', {
                'services': services,
                'stylists': stylists,
                'error_message': "You must select both a stylist and a service."
            })

        stylist = Stylist.objects.get(stylist_id=int(stylist_id))
        service = Service.objects.get(service_id=int(service_id))

        appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

        customer, created = Customer.objects.get_or_create(
            email=email,
            defaults={
                'name': email,
                'phone_number': '000-000-0000'
            }
        )

        Appointment.objects.create(
            service=service,
            appointment_datetime=appointment_datetime,
            stylist=stylist,
            customer=customer,
            booking_confirmation='pending'
        )

        return redirect('booking_confirmed')  # <-- Redirect to confirmation page

    return render(request, 'VVStylesBooking.html', {'services': services, 'stylists': stylists})

def booking_confirmed_view(request):
    return render(request, 'VVStylesBookingConfirmed.html')



