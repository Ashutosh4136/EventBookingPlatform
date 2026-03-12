from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from events.models import Event
from .forms import ReviewForm
from .models import Review


@login_required
def add_review(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)
            review.user = request.user
            review.event = event
            review.save()

            return redirect('event_detail', pk=event.id)

    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'event': event
    })