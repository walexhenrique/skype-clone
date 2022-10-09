from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

from .forms.login_form import LoginForm
from .forms.register_form import RegisterForm
from .models import Profile


class RegisterView(View):
    
    def get(self, *args, **kwargs):
        register_data = self.request.session.get('form_register')
        form = RegisterForm(register_data)
        return render(self.request, 'accounts/register.html', {'form': form})
    
    def post(self, *args, **kwargs):
        form = RegisterForm(self.request.POST)
        self.request.session['form_register'] = self.request.POST

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            surname = form.cleaned_data.get('surname')
            user = User.objects.create_user(username=username, email=email, password=password)

            Profile.objects.create(surname=surname, user=user, slug=username)
            del(self.request.session['form_register'])
            return redirect('accounts:teste')
        
        return redirect('accounts:register_view')


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
    return render(request, 'accounts/teste.html', {'saco': 'cimento'})
