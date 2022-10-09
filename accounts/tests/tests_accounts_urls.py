from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .. import views


class AccountsURLsTest(SimpleTestCase):
    def test_view_register_has_the_correct_path(self):
        url = reverse('accounts:register_view')
        self.assertEqual(url, '/register/')
    
    def test_view_logout_has_the_correct_path(self):
        url = reverse('accounts:logout_view')
        self.assertEqual(url, '/logout/')
    
    def test_view_login_has_the_correct_path(self):
        url = reverse('accounts:login_view')
        self.assertEqual(url, '/login/')
    
