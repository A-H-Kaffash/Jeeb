from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Account(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False, verbose_name=_("Account Name"))
    owner = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name=_("Account Owner"))
    card_number = models.CharField(max_length=20, blank=False, null=False, verbose_name=_("Card Number"))
    balance = models.DecimalField(decimal_places=2, max_digits=20, default=0.0, verbose_name=_("Balance"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")


class Category(models.Model):

    class TransactionType(models.TextChoices):
        INCOME = "INCOME", _("Income")
        EXPENSE = "EXPENSE", _("Expense")

    name = models.CharField(max_length=100,blank=False, null=False, verbose_name=_("Name of Category"))
    transaction_type = models.CharField(choices=TransactionType, max_length=10, blank=False, null=False, verbose_name=_("Transaction Type"))
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name=_("Category User"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Category Description"))

    def __str__(self):
        return f"{self.name} ({self.transaction_type})"

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Transaction(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name=_("Transaction User"))
    account = models.ForeignKey(Account,on_delete=models.CASCADE, blank=False, null=False, verbose_name=_("Transaction Account"))
    amount = models.DecimalField(decimal_places=2, max_digits=20, blank=False, null=False, verbose_name=_("Amount"))
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name=_("Category"))
    date = models.DateField(default=timezone.now, verbose_name="Transaction Date")
    description = models.TextField(max_length=500,blank=True, null=True, verbose_name=_("Description"))

    def __str__(self):
        return f"{self.user} ({self.account})"

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")


