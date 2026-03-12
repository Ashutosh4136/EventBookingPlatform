from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = [
            'title',
            'description',
            'category',
            'image',
            'location',
            'start_date',
            'end_date',
            'capacity'
        ]