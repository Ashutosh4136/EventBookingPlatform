from django.urls import path
from .views import *

urlpatterns = [
    path('add/<int:event_id>/', add_ticket, name='add_ticket'),
    path('create/<int:event_id>/', create_ticket, name='create_ticket'),

    path('event/<int:event_id>/', ticket_list, name='ticket_list'),

]