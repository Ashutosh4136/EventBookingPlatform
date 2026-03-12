from django.urls import path
from .views import *

urlpatterns = [

    path('', notifications_list, name='notifications_list'),

]