from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Category,Token
import secrets

@receiver(post_save, sender=User)
def create_user_defaults(sender, instance, created, **kwargs):
    if created:
        Category.objects.create(
            user=instance,
            name="Default Expense",
            transaction_type=Category.TransactionType.EXPENSE
        )
        Category.objects.create(
            user=instance,
            name="Default Income",
            transaction_type= Category.TransactionType.INCOME
        )
        Token.objects.create(user=instance, string=secrets.token_hex(32))