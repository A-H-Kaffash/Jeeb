from django.contrib import admin

from core.models import *

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "owner", "name"]
    list_filter = ["owner"]
    search_fields = ["card_number"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "user","name", "transaction_type"]
    list_filter = ["user","transaction_type"]
    search_fields = ["name"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["user", "category", "date", "description"]
    list_filter = ["user", "category__transaction_type", "date"]
    search_fields = ["description"]

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ["user"]