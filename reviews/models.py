from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from events.models import Event

User = settings.AUTH_USER_MODEL


class Review(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f"{self.user} - {self.event}"