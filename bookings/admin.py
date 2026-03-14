from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):

    list_display = ['id',
        'user',
        'ticket',
        'date',
        'persons',
        'total_price',
        'status',
        'created_at']

    def get_event(self, obj):
        return obj.ticket.event.title

    get_event.short_description = "Event"


admin.site.register(Booking, BookingAdmin)