from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

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


def teste(request):
    return render(request, 'accounts/teste.html')
