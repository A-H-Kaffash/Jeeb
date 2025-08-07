from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Category

@receiver(post_save, sender=User)
def create_default_category(sender, instance, created, **kwargs):
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
