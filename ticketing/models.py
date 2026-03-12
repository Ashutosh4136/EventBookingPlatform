from django.db import models

# Create your models here.
from django.db import models
from events.models import Event


class Ticket(models.Model):

    TICKET_TYPES = (
        ('free', 'Free'),
        ('paid', 'Paid'),
        ('vip', 'VIP'),
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')

    name = models.CharField(max_length=100)

    ticket_type = models.CharField(max_length=20, choices=TICKET_TYPES)

    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    quantity = models.IntegerField()

    sales_start = models.DateTimeField()

    sales_end = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"