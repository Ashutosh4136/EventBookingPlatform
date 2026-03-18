from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from events.models import Event
from .models import Ticket
from .forms import TicketForm
from django.contrib import messages

@login_required
def add_ticket(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    form = TicketForm(request.POST or None)
    print("POST DATA:", request.POST)  
    if request.method == 'POST' and form.is_valid():
        print("POST DATA:", request.POST)  

        ticket = form.save(commit=False)
        ticket.event = event
        ticket.save()

        messages.success(request, "Ticket added successfully!")

        return redirect('add_ticket', event_id=event.id)
    else:
        print("FORM ERRORS:", form.errors) 

    tickets = Ticket.objects.filter(event=event)

    return render(request, 'ticketing/add_ticket.html', {
        'form': form,
        'event': event,
        'tickets': tickets
    })


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