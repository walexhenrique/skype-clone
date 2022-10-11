from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, 'dispatch')
class IndexView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'friendships/index.html')
