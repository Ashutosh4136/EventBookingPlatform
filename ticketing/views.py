from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from events.models import Event
from .models import Ticket
from .forms import TicketForm


@login_required
def create_ticket(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(commit=False)
            ticket.event = event
            ticket.save()

            return redirect('ticket_list', event_id=event.id)

    else:
        form = TicketForm()

    return render(request, 'ticketing/create_ticket.html', {'form': form, 'event': event})


def ticket_list(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    tickets = Ticket.objects.filter(event=event)

    return render(request, 'ticketing/ticket_list.html', {
        'event': event,
        'tickets': tickets
    })