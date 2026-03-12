from django.urls import path
from .views import *

urlpatterns = [

    path('add/<int:event_id>/', add_review, name='add_review'),

]