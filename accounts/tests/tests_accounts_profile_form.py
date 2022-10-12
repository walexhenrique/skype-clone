from accounts.forms.profile_form import ProfileForm
from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Profile


class ProfileFormTest(TestCase):
    def setUp(self) -> None:
        self.data = {
            'surname': 'Breno zap zap',
            'bio': 'new Bio',
        }

        return super().setUp()
    
    def create_user(
        self,
        username: str = 'Breno',
        email: str = 'breninhoadm@gmail.com', 
        password: str = 'devbr123'
        ):
        return User.objects.create_user(username=username, email=email, password=password)

    def create_profile(
        self,
        user: User,
        surname: str = 'breninho free fire',
        bio: str = 'I play minecraft',
        image: str = 'suco.png'
    ):
        return Profile.objects.create(user=user, surname=surname, bio=bio, image=image)
    
    def test_bio_field_is_greater_than_150_characters_the_form_is_invalid(self):
        # Create user and profile for test
        user = self.create_user()
        profile = self.create_profile(user)
        
        self.data['bio'] = 'A'*121
        form = ProfileForm(self.data,instance=profile)

        self.assertFalse(form.is_valid())

    