from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Friend


@method_decorator(login_required, 'dispatch')
class IndexView(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        # friends_1 = Friend.objects.filter(status='A', id_requester__user=user).order_by('-id')
        # friends_2 = Friend.objects.filter(status='A', id_receiver__user=user).order_by('-id')
        friends = Friend.objects.filter(Q(Q(id_requester__user=user) | Q(id_receiver__user=user)), status='A').order_by('-id')

        
        return render(self.request, 'friendships/index.html', {'friends': friends})

@method_decorator(login_required, 'dispatch')
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


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'friendships/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = Profile.objects.get(user=self.request.user)
        slug = self.kwargs.get('slug')
        profile_detail = Profile.objects.get(slug=slug)

        is_owner = True if slug == profile_user.slug else False
        context['is_owner'] = is_owner
        
        are_friends = Friend.objects.filter(
            Q(id_requester=profile_user,
            id_receiver=profile_detail) |
            Q(id_requester=profile_detail,
            id_receiver=profile_user)
        ).exists()
        context['are_friends'] = are_friends
        return context
