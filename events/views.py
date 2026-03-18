from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def event_list(request):

    events = Event.objects.all().order_by('-created_at')

    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, pk):

    event = get_object_or_404(Event, pk=pk)

    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def create_event(request):

    if request.method == 'POST':

        form = EventForm(request.POST, request.FILES)

        if form.is_valid():

            event = form.save(commit=False)
            event.organizer = request.user
            event.save()

            return redirect('add_ticket', event_id=event.id)

    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})


@login_required
def my_events(request):

    events = Event.objects.filter(organizer=request.user)

    return render(request, 'events/my_event.html', {'events': events})