from django.test import TestCase
from django.urls import reverse


class RegisterViewTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_register_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('accounts:register_view'))
        self.assertEqual(response.status_code, 200)
    
    

    
