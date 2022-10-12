from django.test import SimpleTestCase
from django.urls import reverse


class FriendshipsURLsTest(SimpleTestCase):
    def test_view_index_has_the_correct_path(self):
        url = reverse('friendships:index')

        self.assertEqual(url, '/friendships/')
    
    def test_view_search_has_the_correct_path(self):
        url = reverse('friendships:search')

        self.assertEqual(url, '/friendships/search/')

    def test_view_profile_detail_has_the_correct_path(self):
        url = reverse('friendships:profile-detail', kwargs={'slug': 'breno'})
        
        self.assertEqual(url, '/friendships/profile-detail/breno/')
