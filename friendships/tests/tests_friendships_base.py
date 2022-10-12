from accounts.models import Profile
from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Friend


class FriendshipsBaseTest(TestCase):
    def setUp(self) -> None:
        self.profile = self.create_profile(self.create_user())
        return super().setUp()
    
    def create_user(
        self,
        username:str = 'Breno',
        email:str = 'breno@gmail.com',
        password:str = '123456'
    ) -> User:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return user
    
    def create_profile(
        self,
        user: User,
        slug:str = 'breno',
        surname:str = 'Breninho free fire',
        bio:str = 'Breno está aberto para novas amizades',
        image:str = None,
    ) -> Profile:
        profile = Profile.objects.create(
            user=user,
            slug=slug,
            surname=surname,
            bio=bio,
            image=image,
        )
        return profile

    def create_friendship(self, profile_1, profile_2, status='A') -> Friend:
        friend = Friend.objects.create(id_requester=profile_1, id_receiver=profile_2, status=status)
        return friend
    
        