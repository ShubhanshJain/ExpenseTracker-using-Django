from tracker.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('delete-transactions/<uuid>', delete_transactions, name = 'delete_transactions'),
]