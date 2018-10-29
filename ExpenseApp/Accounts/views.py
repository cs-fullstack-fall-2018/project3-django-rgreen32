from django.shortcuts import render, redirect
from .models import Account, Activity
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .forms import DepositForm, WidthdrawForm, RegisterForm
from django.utils import timezone
# Create your views here.


def index(request):
    if request.user.id:
        print(request.user.id)
        account = get_object_or_404(Account, User_id=request.user.id)
        print(account.activity_set.all())
        print(account.balance)
        history = account.activity_set.all()
        context = {
            'account': account,
            'history': history
        }
        return render(request, 'accounts/index.html', context)
    else:
        return render(request, 'accounts/welcome.html')

def register(request):
    print("here")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("here in if")
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            print('here')
            # user.account_set.create(balance='1111')
            print("it worked now")
            #account = get_object_or_404(Account, User_id=user.id)
            user.account_set.create(balance=request.POST["checking_balance"], emergency_fund=request.POST["savings_balance"])
            return redirect('index')

    else:
        form = UserCreationForm()
        form2 = RegisterForm()
        context = {'form': form, 'form2': form2}
        return render(request, 'registration/register.html', context)


def deposit(request):
    if request.method == "POST":
        name = request.POST['name']
        account = get_object_or_404(Account, User_id=request.user.id)
        depositAmount = int(request.POST["deposit_amount"])
        account_type = request.POST["account_type"]
        if account_type == 'Checking':
            Account.objects.select_for_update().filter(User_id=request.user.id).update(balance=int(account.balance) + depositAmount)
        elif account_type == 'Savings':
            Account.objects.select_for_update().filter(User_id=request.user.id).update(emergency_fund=int(account.emergency_fund) + depositAmount)

        account.activity_set.create(widthdrawlorDeposit='Deposit', account_type=account_type, transaction_date=timezone.now(), amount=depositAmount, name=name)

        return redirect('index')
    else:
        form = DepositForm()
        # context = {'form', form}
        return render(request, 'accounts/deposit.html', {'form': form})


def widthdraw(request):
    if request.method == "POST":
        name = request.POST['name']
        account = get_object_or_404(Account, User_id=request.user.id)
        account_type = request.POST["account_type"]
        widthdrawAmount = int(request.POST["widthdraw_amount"])
        if account_type == 'Checking':
            Account.objects.select_for_update().filter(User_id=request.user.id).update(balance=int(account.balance) - widthdrawAmount)
        elif account_type == 'Savings':
            Account.objects.select_for_update().filter(User_id=request.user.id).update(emergency_fund=int(account.emergency_fund) - widthdrawAmount)

        account.activity_set.create(widthdrawlorDeposit='Widthdraw', account_type=account_type, transaction_date=timezone.now(), amount=widthdrawAmount, name=name)
        return redirect('index')
    else:
        form = WidthdrawForm()
        # context = {'form', form}
        return render(request, 'accounts/widthdraw.html', {'form': form})


def logout(request):
    print(request.user.is_authenticated)
    auth_logout(request)
    return render(request, 'accounts/welcome.html')




# def login(request):
#     m = Account.objects.get(user_name=request.POST['username'])
#     if m.user_pass == request.POST('password'):
#         request.session["member_id"] = m.id
#
#
# def logout(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out.")