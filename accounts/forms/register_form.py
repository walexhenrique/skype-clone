
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(
        label = 'Username',
        error_messages = {
            'required': 'Error, username cannot be empty',
            'max_length': 'Error, username is too big',
        },
        max_length = 150,
    )

    surname = forms.CharField(
        label = 'Surname',
        error_messages = {
            'required': 'Error, surname cannot be empty',
            'max_length': 'Error, surname is too big'
        },
        max_length=50,
        help_text = 'This will be the public and prominent name'
    )

    email = forms.EmailField(
        label = 'E-mail',
        error_messages = {
            'required': 'Error, email cannot be empty'
        },
    )

    password = forms.CharField(
        label = 'Password',
        error_messages = {
            'required': 'Error, password cannot be empty'
        },
        widget = forms.PasswordInput
    )

    password2 = forms.CharField(
        label = 'Repeat your password',
        error_messages = {
            'required': 'Error, this field cannot be empty'
        },
        widget = forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        username_alredy_exists = User.objects.filter(username=username).exists()

        if username_alredy_exists:
            raise ValidationError('Error, username already exists in the database')

        return username
    
    def clean_surname(self):
        surname = self.cleaned_data.get('surname', '')

        if len(surname) < 3:
            raise ValidationError('Error, surname is too short')
        
        return surname

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_alredy_exists = User.objects.filter(email=email).exists()

        if email_alredy_exists:
            raise ValidationError('Error, email already exists in the database')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password', '')

        if len(password) < 5:
            raise ValidationError('Error, password is too short')
        
        return password
    
    def clean_password2(self):
        password2 = self.cleaned_data.get('password2', '')

        if len(password2) < 5:
            raise ValidationError('Error, password is too short')
        
        return password2
    
    def clean(self):
        super().clean()

        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise ValidationError('Error, passwords not be equals')
        
    
