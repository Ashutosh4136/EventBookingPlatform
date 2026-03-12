from django.urls import path
from .views import *

urlpatterns = [

    path('book/<int:event_id>/', book_ticket, name='book_ticket'),

    path('my-bookings/', my_bookings, name='my_bookings'),

    path('success/', booking_success, name='booking_success'),

]