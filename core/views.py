from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import transaction
from django.utils import timezone
from datetime import datetime
from decimal import Decimal
from .models import Token, Transaction, Account, Category


# Create your views here.

@csrf_exempt
@transaction.atomic
def submit_transaction(request):

    if request.method != "POST":
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

    token_str = request.POST.get('token')
    amount_str = request.POST.get('amount')
    category_id = request.POST.get('category_id')
    account_id = request.POST.get('account_id')
    description = request.POST.get('description')
    date_str = request.POST.get('date',None)

    if date_str:
        transaction_date = datetime.strptime(date_str, '%Y-%m-%d').date() #date format: YYYY-MM-DD ( like 2025-08-19 )
    else:
        transaction_date = timezone.now()
    process_now = (transaction_date <= timezone.now().date())

    if not all([token_str, amount_str, category_id,account_id]):
        return JsonResponse({'status': 'error', 'message': 'Missing required fields'}, status=400)

    try:

        user = Token.objects.get(string=token_str).user
        account = Account.objects.get(id=account_id,owner=user)
        category = Category.objects.get(id=category_id)
        amount = Decimal(amount_str)

        new_transaction = Transaction.objects.create(
            user=user,
            account=account,
            category=category,
            amount=amount,
            description=description,
            is_processed=process_now,
        )

        if process_now:
            if category.transaction_type == Category.TransactionType.INCOME:
                account.balance += amount
            elif category.transaction_type == Category.TransactionType.EXPENSE:
                account.balance -= amount

            account.save()

        transaction_data = {
            'id': new_transaction.id,
            'account_name': new_transaction.account.name,
            'category_name': new_transaction.category.name,
            'amount': str(new_transaction.amount),
            'date': new_transaction.date.isoformat(),
            'description': new_transaction.description,
        }

        return JsonResponse({'status': 'success', 'transaction': transaction_data})

    except Token.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Invalid token'}, status=401)

    except (Account.DoesNotExist, Category.DoesNotExist):
        return JsonResponse({'status': 'error', 'message': 'Invalid account or category'}, status=404)

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
