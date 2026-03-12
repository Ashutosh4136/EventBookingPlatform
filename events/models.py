from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):

    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    image = models.ImageField(upload_to='events/')

    location = models.CharField(max_length=200)

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title