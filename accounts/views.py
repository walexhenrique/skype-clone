from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms.register_form import RegisterForm


class RegisterView(CreateView):
    
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/admin/'
