from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket

        fields = [
            # 'name',
            'ticket_type',
            'price',
            'quantity',
            # 'total_quantity'
        ]
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control'}),
                'total_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            }