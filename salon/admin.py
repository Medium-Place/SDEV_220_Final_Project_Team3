from django.contrib import admin
from .models import Stylist
from .models import Customer
from .models import Appointment
from .models import Service

admin.site.register(Stylist)
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(Service)

# Register your models here.
