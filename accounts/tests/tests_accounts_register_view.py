from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..forms.register_form import RegisterForm
from ..models import Profile


class RegisterViewTest(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'username': 'Breno',
            'surname': 'Breninho free fire',
            'email': 'breno@email.com',
            'password': '123456',
            'password2': '123456',
        }
        return super().setUp()
    
    def test_register_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('accounts:register_view'))
        self.assertEqual(response.status_code, 200)
    
    def test_register_view_create_user_and_profile_successfully(self):
        url = reverse('accounts:register_view')
        response = self.client.post(url, self.form_data)

        user = User.objects.filter(username=self.form_data['username']).exists()
        profile = Profile.objects.filter(pk=1).exists()

        self.assertTrue(user)
        self.assertTrue(profile)
        self.assertEqual(response.status_code, 302)
    
    def test_register_view_display_form_errors_when_it_is_not_valid(self):
        url = reverse('accounts:register_view')
        self.form_data['email'] = 'email.com'
        response = self.client.post(url, self.form_data, follow=True)

        self.assertContains(response, 'Enter a valid email address.')
        self.assertContains(response, 'There are errors in the form, please fix them and send again.')

    def test_register_view_the_data_entered_is_not_valid_profile_and_user_must_not_be_created(self):
        url = reverse('accounts:register_view')
        self.form_data['password'] = '123456789'
        self.form_data['password2'] = '123456'

        response = self.client.post(url, self.form_data)
        user_created = User.objects.filter(username=self.form_data['username']).exists()
        profile_created = Profile.objects.filter(surname=self.form_data['surname']).exists()

        self.assertFalse(user_created)
        self.assertFalse(profile_created)
    
    def test_register_view_form_used_is_correct(self):
        url = reverse('accounts:register_view')
        response = self.client.get(url)
        self.assertIsInstance(response.context.get('form'), RegisterForm)




    
