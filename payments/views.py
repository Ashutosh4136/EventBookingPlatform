from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from bookings.models import Booking
from .models import Payment


def make_payment(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        'booking': booking,
        'event': booking.ticket
    }

    return render(request, 'payments/make_payment.html', context)


def payment_success(request):

    return render(request, 'payments/payment_success.html')