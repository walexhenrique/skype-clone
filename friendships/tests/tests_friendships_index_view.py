from django.urls import reverse

from .tests_friendships_base import FriendshipsBaseTest


class IndexViewTest(FriendshipsBaseTest):

    def test_view_returns_status_code_200_OK(self):
        self.client.login(username='Breno', password='123456')
        
        url = reverse('friendships:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
