from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ticketing.models import Ticket
from .models import Booking
from .forms import BookingForm
from events.models import Event



@login_required
def book_ticket(request, event_id):

    ticket = get_object_or_404(Ticket, event_id=event_id)

    # ✅ check availability
    if ticket.remaining_quantity <= 0:
        return render(request, 'events/sold_out.html')

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user
            booking.ticket = ticket

            booking.date = form.cleaned_data['date']
            booking.persons = form.cleaned_data['persons']
            booking.food = form.cleaned_data['food']

            # ✅ calculate price
            booking.total_price = ticket.price * booking.persons

            booking.status = 'confirmed'

            booking.save()

            return redirect('make_payment', booking_id=booking.id)

    else:
        form = BookingForm()

    return render(request, 'bookings/book_ticket.html', {
        'form': form,
        'ticket': ticket
    })
@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'bookings/my_bookings.html', {
        'bookings': bookings
    })


def booking_success(request):

    return render(request, 'bookings/booking_success.html')