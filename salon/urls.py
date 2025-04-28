from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),           # Homepage
    path('services/', views.services_view, name='services'),  # Services page
    path('booking/', views.booking_view, name='booking'),     # Booking page
    path('booking/confirmed/', views.booking_confirmed_view, name='booking_confirmed'),  # Booking Confirmation
]
