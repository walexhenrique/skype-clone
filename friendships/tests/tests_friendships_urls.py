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
    
    def test_view_profile_detail_edit_has_the_correct_path(self):
        url = reverse('friendships:profile-edit', kwargs={'slug':'breno'})

        self.assertEqual(url, '/friendships/profile-detail/breno/edit/')

    def test_view_friend_request_has_the_correct_path(self):
        url = reverse('friendships:friend-request', kwargs={'slug': 'breno'})

        self.assertEqual(url, '/friendships/friend-request/breno/')
    
    def test_view_peding_has_the_correct_path(self):
        url = reverse('friendships:pending')
        
        self.assertEqual(url, '/friendships/pending/')
    
    def test_view_denied_request_has_the_correct_path(self):
        url = reverse('friendships:profile-denied', kwargs={'id': 1})

        self.assertEqual(url, '/friendships/profile-denied/1/')

    def test_view_accepted_request_has_the_correct_path(self):
        url = reverse('friendships:profile-accepted', kwargs={'id': 1})

        self.assertEqual(url, '/friendships/profile-accepted/1/')
