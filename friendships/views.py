from accounts.forms.profile_form import ProfileForm
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView

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

@method_decorator(login_required, 'dispatch')
class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'friendships/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get profile user logged
        profile_user = Profile.objects.get(user=self.request.user)
        
        # Slug profil detail
        slug = self.kwargs.get('slug')

        # Get profile from slug
        profile_detail = Profile.objects.get(slug=slug)

        # Checks if slug is equal slug from profile_user
        is_owner = True if slug == profile_user.slug else False
        context['is_owner'] = is_owner
        
        # Check if are friends
        are_friends = Friend.objects.filter(
            Q(id_requester=profile_user,
            id_receiver=profile_detail) |
            Q(id_requester=profile_detail,
            id_receiver=profile_user)
        ).exists()

        context['are_friends'] = are_friends
        return context

@method_decorator(login_required, 'dispatch')
class ProfileEditUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'friendships/profile-edit.html'
    success_url = reverse_lazy('friendships:index')

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        profile = Profile.objects.filter(slug=slug)

        if not profile:
            raise Http404()

        if profile.first().user != self.request.user:
            return redirect(reverse('friendships:profile-detail', kwargs={'slug': slug}))
        
        return super().get(request, *args, **kwargs)

@method_decorator(login_required, 'dispatch')
class ProfileFriendRequest(View):
    def get(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        
        profile_request = Profile.objects.filter(slug=slug).first()

        if not profile_request:
            raise Http404()
            
        profile_owner = Profile.objects.get(user=self.request.user)
        
        if profile_request.slug == profile_owner.slug:
            return redirect(reverse_lazy('friendships:index'))

        search_friendships = Friend.objects.filter(
            Q(
                Q(id_requester = profile_request,
                id_receiver = profile_owner),
                ~Q(status = 'D')
            ) | Q(
                Q(id_requester = profile_owner,
                id_receiver = profile_request),
                ~Q(status = 'D')
            )
        ).exists()

        if search_friendships:
            return redirect(reverse_lazy('friendships:index'))
        
        Friend.objects.create(id_requester=profile_owner, id_receiver=profile_request)
        return redirect(reverse_lazy('friendships:index'))



