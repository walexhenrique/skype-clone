from collections import defaultdict

from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._errors = defaultdict(list)

    username = forms.CharField(
        label = 'Username',
        error_messages = {
            'required': 'Error, username is required',
            'max_length': 'Error, username is longer than 150 characters',
            'min_length': 'Error, username is too short',
        },
        max_length = 150,
        min_length = 4,
    )

    first_name = forms.CharField(
        label = 'Your surname',
        error_messages = {
            'required': 'Error, surname is required',
            'max_length': 'Error, surname is longer than 150 characters',
            'min_length': 'Error, surname is too short',
        },
        max_length = 150,
        min_length = 4,
    )

    email = forms.EmailField(
        label = 'E-mail',
        error_messages = {
            'required': 'Error, email is required',
        },
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Your password'
            }
        ),
        error_messages = {
            'required': 'Error, password is required',
        }
    )
    password2 = forms.CharField(
        label = 'Repeat your password',
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Repeat your password',
            },
        ),
        error_messages = {
            'required': 'Error, please repeat your password'
        }
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email', '')

        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            self._errors['email'].append('E-mail already registered')
        
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        username_exists = User.objects.filter(username=username).exists()

        if username_exists:
            self._errors['username'].append('Username alredy registered')
        
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password', '')

        if len(password) < 5:
            self._errors['password'].append('Password is too short')
        
        return password
    
    def clean_password2(self):
        password2 = self.cleaned_data.get('password2', '')

        if len(password2) < 5:
            self._errors['password2'].append('Password is too short')
        
        return password2
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password', '')
        password2 = cleaned_data.get('password2', '')

        if password != password2:
            self._errors['password'].append('the passwords do not match')
            self._errors['password2'].append('the passwords do not match')
        
        if self._errors:
            raise ValidationError(self._errors)
        
