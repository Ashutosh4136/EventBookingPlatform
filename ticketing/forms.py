from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket

        fields = [
            'name',
            'ticket_type',
            'price',
            'quantity',
            'sales_start',
            'sales_end'
        ]