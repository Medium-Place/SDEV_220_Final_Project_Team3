from django.db import models # type: ignore

class Stylist(models.Model): #Defines Stylist Class to store information about stylist
    
    stylist_id = models.AutoField(primary_key=True) # Unique ID automatically generated for each stylist record.
    name = models.CharField(max_length=100)  # Stylist's name
    phone_number = models.CharField(max_length=20) # Stylist's contact number
    social_media = models.CharField(max_length=100, blank=True) # Optional social media link
    portfolio = models.ImageField(blank=True, null=True) #Optional portfolio image
    
    #Methods
    def confirm_appointment(self, appointment): #method to confirm an appointment
        appointment.confirmation = 'confirmed'
        appointment.save()
        return True
    
    def __str__(self): #string representaiton of stylist object
        return self.name
    

class Customer(models.Model):#Defines Customer Class model to store information about clients
    
    customer_id = models.AutoField(primary_key=True) # Unique ID automatically generated for each customer record
    name = models.CharField(max_length=100) #Customer's name
    email= models.EmailField(unique=True) #Customer's email
    phone_number = models.CharField(max_length=20) #Customer's contact number

    #Methods
    def book_appointment(self, stylist, service, datetime): #Customer books an appointment
        return Appointment.objects.create(
            customer=self,
            stylist=stylist,
            service=service,
            appointment_datetime=datetime,
            booking_confirmation='pending'
        )
    
    def view_appointment(self, stylist, datetime):# View all appointments associated with customer
        return self.appointment_set.all()
    
    def cancel_appointment(self, appointment): #Cancel a specific appointment
        appointment.booking_confirmation = 'canceled'
        appointment.save()

    def reschedule_appointment(self, appointment, new_datetime): #Reschedules a specific appointment
        appointment.reschedule(new_datetime)
        appointment.booking_confirmation = 'pending'
        appointment.save()

    def __str__(self): #String representation of customer object
        return self.name
    


class Appointment(models.Model):#Defines Appointment class to store data between customers and stylist
    
    #Tuples that store status options for booking confirmation
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    service = models.ForeignKey('Service', on_delete=models.CASCADE) #services that are linked
    appointment_datetime = models.DateTimeField() #date and time of the appointment
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)# linked stylist
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)# linked customer
    booking_confirmation = models.CharField(max_length=10, choices=STATUS_CHOICES) #status of the appointment 

    #Methods
    def reschedule(self, new_datetime): #reschedules an appointment
        self.appointment_datetime = new_datetime
        self.save()

    def modify_service(self, new_service):# changes the service for the appointment
        self.service = new_service
        self.save()

    def __str__(self): #string representation of the appointment object
        return f"{self.appointment_datetime} - {self.customer.name} with {self.stylist.name}"
    


class Service(models.Model):#Defines Service Class to store the types of services offered by the salon
    
    service_id = models.AutoField(primary_key=True) # Unique ID automatically generated for each 
    service_type = models.CharField(max_length=100) # Type of service (ex. freestyle, intermediate, simple braids etc.)
    style_description = models.TextField() #Description of the style/service
    duration = models.DurationField()  #Time required for the service
    price = models.DecimalField(max_digits=6, decimal_places=2) #Price of the service

    #Methods
    def get_service_price(self): #Returns the price of the service
        return self.price

    
    def list_services(): #Returns all the services available
        return Service.objects.all()

    def __str__(self): #String representation of the service object
        return self.service_type
    





