from django.urls import path
from . import views

urlpatterns = [
    path('api/submit-transaction/',views.submit_transaction,name='api_submit_transaction'),
    path('api/register',views.register_user,name='api_register'),
    path('api/login',views.login_user,name='api_login'),
]