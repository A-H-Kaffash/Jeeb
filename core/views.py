from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Token, Transaction, Account, Category


# Create your views here.

@csrf_exempt
def submit_transaction(request):

    if request.method != "POST":
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

    token_str = request.POST.get('token')
    amount = request.POST.get('amount')
    category_id = request.POST.get('category_id')
    account_id = request.POST.get('account_id')
    description = request.POST.get('description')

    if not all([token_str,amount,category_id,account_id]):
        return JsonResponse({'status': 'error', 'message': 'Missing required fields'}, status=400)

    try:
        user = Token.objects.get(string=token_str).user
        account = Account.objects.get(id=account_id,owner=user)
        category = Category.objects.get(id=category_id)

        new_transaction = Transaction.objects.create(
            user=user,
            account=account,
            category=category,
            amount=amount,
            description=description,
        )

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
