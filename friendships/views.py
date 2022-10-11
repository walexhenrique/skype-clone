from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from .models import Friend


@method_decorator(login_required, 'dispatch')
class IndexView(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        # friends_1 = Friend.objects.filter(status='A', id_requester__user=user).order_by('-id')
        # friends_2 = Friend.objects.filter(status='A', id_receiver__user=user).order_by('-id')
        friends = Friend.objects.filter(Q(Q(id_requester__user=user) | Q(id_receiver__user=user)), status='A').order_by('-id')

        
        return render(self.request, 'friendships/index.html', {'friends': friends})


class SearchListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'friendships/search.html'
    paginate_by = 5
    ordering = ['-id']
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        surname_search = self.request.GET.get('surname', '')
        profile_user = Profile.objects.get(user=self.request.user)
        qs = qs.filter(
            surname__icontains=surname_search
        ).exclude(surname=profile_user.surname)

        return qs
