from django.shortcuts import render
from events.models import Event


def home(request):

    events = Event.objects.all().order_by("-created_at")[:6]

    return render(request, "home/home.html", {
        "events": events
    })