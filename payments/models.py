from django.db import models
from bookings.models import Booking


class Payment(models.Model):

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(max_length=50)

    transaction_id = models.CharField(max_length=200, blank=True, null=True)

    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')

    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking}"