from django.urls import path
from . import views

urlpatterns = [
    path('api/submit-transaction/',views.submit_transaction,name='api_submit_transaction'),
]