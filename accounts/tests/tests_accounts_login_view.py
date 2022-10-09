from urllib import response

from django.test import TestCase
from django.urls import reverse


class LoginViewTest(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'username': 'Breno',
            'surname': 'Breninho free fire',
            'email': 'breno@email.com',
            'password': '123456',
            'password2': '123456',
        }

        self.form_login = {
            'username': 'Breno',
            'password': '123456'
        }
        return super().setUp()
    
    def test_login_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('accounts:login_view'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_view_correctly_logged_in_an_existing_user(self):
        # Register a new user with register_view
        url_register = reverse('accounts:register_view')
        self.client.post(url_register, self.form_data)

        # Test start here
        url_login = reverse('accounts:login_view')
        response = self.client.post(url_login, data=self.form_login)
        self.assertRedirects(response, reverse('accounts:teste'))

    def test_login_view_user_exists_but_entered_the_data_wrong(self):
        # Register a new user with register_view
        url_register = reverse('accounts:register_view')
        self.client.post(url_register, self.form_data)

        # Test start here
        url_login = reverse('accounts:login_view')
        self.form_login['password'] = '12345'  # Correct password = '123456'
        response = self.client.post(url_login, data=self.form_login)
        self.assertRedirects(response, url_login)

            