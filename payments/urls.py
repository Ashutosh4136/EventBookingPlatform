from django.urls import path
from .views import *

urlpatterns = [

    path('pay/<int:booking_id>/', make_payment, name='make_payment'),

    path('success/', payment_success, name='payment_success'),

]