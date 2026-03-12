from django.contrib import admin

# Register your models 
from django.contrib import admin
from .models import Ticket

admin.site.register(Ticket)