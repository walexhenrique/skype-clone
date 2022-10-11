from django.test import SimpleTestCase
from django.urls import reverse


class FriendshipsURLsTest(SimpleTestCase):
    def test_view_index_has_the_correct_path(self):
        url = reverse('friendships:index')

        self.assertEqual(url, '/friendships/')
