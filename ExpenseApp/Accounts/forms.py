from django import forms

CHOICES = [
    ('Checking', 'Checking'),
    ('Savings', 'Savings')
]


class DepositForm(forms.Form):
    account_type = forms.CharField(label='Account:',
                                   widget=forms.RadioSelect(choices=CHOICES))
    name = forms.CharField(label='Description:')
    deposit_amount = forms.IntegerField(min_value=1)


class WidthdrawForm(forms.Form):
    account_type = forms.CharField(label='Account:',
                                   widget=forms.RadioSelect(choices=CHOICES))
    name = forms.CharField(label='Description:')
    widthdraw_amount = forms.IntegerField(min_value=1)


class RegisterForm(forms.Form):
    checking_balance = forms.IntegerField()
    savings_balance = forms.IntegerField()
