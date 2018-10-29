from django.db import models
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone


# class UserProfile(models.Model):
#     user =  models.OneToOneField()
#     username_validator = ASCIIUsernameValidator()
#
#     class Meta:
#         proxy = True


class Account(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    balance = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    emergency_fund = models.DecimalField(max_digits=16, decimal_places=2, default=0)

    sign_up_date = models.DateTimeField(default=timezone.now)


    def get_balance(self):
        return self.balance

    def get_emergencyFund(self):
        return self.emergency_fund


class Activity(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=25, blank=True)
    widthdrawlorDeposit = models.CharField(max_length=25, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    transaction_date = models.DateTimeField(null=True)
    name = models.CharField(max_length=25, blank=True)

