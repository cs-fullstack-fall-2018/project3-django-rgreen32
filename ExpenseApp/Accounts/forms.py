from django import forms

CHOICES = [
    ('Checking', 'Checking'),
    ('Savings', 'Savings')
]


class DepositForm(forms.Form):
    account_type = forms.CharField(label='Account:',
                                   widget=forms.RadioSelect(choices=CHOICES))
    name = forms.CharField(label='Description:')
    deposit_amount = forms.DecimalField(min_value=1)


class WidthdrawForm(forms.Form):
    account_type = forms.CharField(label='Account:',
                                   widget=forms.RadioSelect(choices=CHOICES))
    name = forms.CharField(label='Description:')
    widthdraw_amount = forms.DecimalField(min_value=1)


class RegisterForm(forms.Form):
    checking_balance = forms.DecimalField()
    savings_balance = forms.DecimalField()
