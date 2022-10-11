from accounts.models import Profile
from django.contrib.auth.models import User
from django.test import TestCase


class FriendshipsBaseTest(TestCase):
    def setUp(self) -> None:
        self.profile = self.create_profile(self.create_user())
        return super().setUp()
    
    def create_user(
        self,
        username:str = 'Breno',
        email:str = 'breno@gmail.com',
        password:str = '123456'
    ):
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return user
    
    def create_profile(
        self,
        user,
        slug:str = 'breno',
        surname:str = 'Breninho free fire',
        bio:str = 'Breno está aberto para novas amizades',
        image:str = None,
    ):
        profile = Profile.objects.create(
            user=user,
            slug=slug,
            surname=surname,
            bio=bio,
            image=image,
        )
        return profile

    
        