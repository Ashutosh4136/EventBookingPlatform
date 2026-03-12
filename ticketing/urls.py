from django.urls import path
from .views import *

urlpatterns = [

    path('create/<int:event_id>/', create_ticket, name='create_ticket'),

    path('event/<int:event_id>/', ticket_list, name='ticket_list'),

]