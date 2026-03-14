from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from ticketing.models import Ticket
from events.models import Event

User = settings.AUTH_USER_MODEL


class Booking(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    date = models.DateField(null=True, blank=True)

    persons = models.IntegerField(null=True, blank=True)

    food = models.BooleanField(default=False)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} - {self.ticket.event.title}"