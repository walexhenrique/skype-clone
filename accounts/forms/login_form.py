from attr import attr
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Username', 
        max_length=150,
        widget=forms.PasswordInput(attrs={'placeholder': 'Ex.: John'})
    )
    password = forms.CharField(
        label = 'Password', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password...'})
    )
