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
        print("Form POST received")

        try:
            email = request.POST.get('email')
            date = request.POST.get('date')
            time = request.POST.get('time')
            stylist_id = request.POST.get('stylist')
            service_id = request.POST.get('service')
        
            print(f"Email: {email}, Date: {date}, Time: {time}, Stylist ID: {stylist_id}, Service ID: {service_id}")

            if not stylist_id or not service_id:
                print("Stylist or Service missing!")
                return render(request, 'VVStylesBooking.html', {
                    'services': services,
                    'stylists': stylists,
                    'error_message': "You must select both a stylist and a service."
                })

            stylist = Stylist.objects.get(stylist_id=int(stylist_id))
            print(f"Stylist found: {stylist.name}")

            service = Service.objects.get(service_id=int(service_id))
            print(f"Service found: {service.service_type}")

            appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            print(f"Parsed datetime: {appointment_datetime}")

            customer, created = Customer.objects.get_or_create(email=email, defaults={
                'name': email,
                'phone_number': '000-000-0000'
            })
            print(f"Customer found or created: {customer.name}")

            Appointment.objects.create(
                service=service,
                appointment_datetime=appointment_datetime,
                stylist=stylist,
                customer=customer,
                booking_confirmation='pending'
            )

            print("Appointment created successfully!")

            return redirect('home')

        except Exception as e:
            print(f"Something went wrong: {e}")

            return render(request, 'VVStylesBooking.html', {
                'services': services,
                'stylists': stylists,
                'error_message': f"Error: {e}"
            })

    return render(request, 'VVStylesBooking.html', {'services': services, 'stylists': stylists})



