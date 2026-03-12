from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):

    FOOD_CHOICES = [
        (True, "Yes, Include Food"),
        (False, "No Food"),
    ]

    food = forms.ChoiceField(
        choices=FOOD_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Booking
        fields = ['date', 'persons', 'food']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }