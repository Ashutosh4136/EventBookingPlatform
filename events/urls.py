from django.urls import path
from .views import *

urlpatterns = [

    path('', event_list, name='event_list'),

    path('event/<int:pk>/', event_detail, name='event_detail'),

    path('create/', create_event, name='create_event'),

    path('my-events/', my_events, name='my_events'),

]