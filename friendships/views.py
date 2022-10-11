from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from .models import Friend


@method_decorator(login_required, 'dispatch')
class IndexView(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        friends_1 = Friend.objects.filter(status='A', id_requester__user=user).order_by('-id')
        friends_2 = Friend.objects.filter(status='A', id_receiver__user=user).order_by('-id')

        
        return render(self.request, 'friendships/index.html', {'friends_add': friends_1, 'friends_received': friends_2})
