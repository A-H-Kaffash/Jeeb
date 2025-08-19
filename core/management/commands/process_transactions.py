from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from core.models import Transaction, Category

class Command(BaseCommand):
    help = "Process pending transactions whose date has arrived"

    def handle(self, *args, **options):
        today = timezone.now().date()
        transactions_to_process = Transaction.objects.filter(
            date__gte=today,
            is_processed=False,
        )

        for trans in transactions_to_process:
            with transaction.atomic():
                account = trans.account

                if trans.category.transaction_type == Category.TransactionType.INCOME:
                    account.balance += trans.amount
                elif trans.category.transaction_type == Category.TransactionType.EXPENSE:
                    account.balance -= trans.amount

                account.save()
                trans.is_processed = True
                trans.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully processed transaction ID: {trans.id}'))

# Run command below in terminal:
# python manage.py process_transactions
