from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

from .forms.login_form import LoginForm
from .forms.register_form import RegisterForm


class RegisterView(View):
    
    def get(self, *args, **kwargs):
        form = RegisterForm()
        return render(self.request, 'accounts/register.html', {'form': form})
    
    def post(self, *args, **kwargs):
        form = RegisterForm(self.request.POST)

        if form.is_valid():
            return redirect('accounts:teste')
        
        return render(self.request, 'accounts/register.html', {'form': form})


class LoginView(View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        return render(self.request, 'accounts/login.html', {'form': form})
    
    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = authenticate(self.request, username=username, password=password)

            if user:
                login(self.request, user)
                return redirect('accounts:teste')
        
        return redirect('accounts:login_view')
            


def teste(request):
    return render(request, 'accounts/teste.html')
