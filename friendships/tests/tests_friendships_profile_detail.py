from django.urls import reverse

from .tests_friendships_base import FriendshipsBaseTest


class SearchViewTest(FriendshipsBaseTest):
    def setUp(self) -> None:
        self.url = reverse('friendships:profile-detail', kwargs={'slug': 'breno'})
        return super().setUp()

    def test_profile_detail_view_returns_status_code_200_OK(self):
        # you must be logged in
        self.client.login(username='Breno', password='123456')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_profile_detail_view_redirect_for_login_if_is_not_logged(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_profile_detail_view_returns_status_code_404_if_no_profile_is_found_with_the_slug(self):
        self.client.login(username='Breno', password='123456')

        url_slug_not_exists = reverse('friendships:profile-detail', kwargs={'slug': 'user-random'})
        response = self.client.get(url_slug_not_exists)
        self.assertEqual(response.status_code, 404)
    
    def test_profile_detail_view_the_profile_owner_has_accessed_and_is_owner_must_be_true(self):
        self.client.login(username='Breno', password='123456')

        response = self.client.get(self.url)
        self.assertTrue(response.context['is_owner'])

        self.assertFalse(response.context['are_friends'])

    def test_profile_detail_view_if_access_by_profile_that_already_has_a_friend_request_are_friends_in_context_equals_true(self):
        self.client.login(username='Breno', password='123456')
        url_magali = reverse('friendships:profile-detail', kwargs={'slug': 'magali'})

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # Create friendship
        self.create_friendship(profile_1=self.profile, profile_2=friend_profile)

        response = self.client.get(url_magali)
        self.assertTrue(response.context['are_friends'])

        self.assertFalse(response.context['is_owner'])
    
    def test_profile_detail_view_if_the_profile_you_access_is_not_a_friend_context_are_friends_is_false(self):
        self.client.login(username='Breno', password='123456')

        url_magali = reverse('friendships:profile-detail', kwargs={'slug': 'magali'})

        # Create outher profile 
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        response = self.client.get(url_magali)
        self.assertFalse(response.context['are_friends'])

        self.assertFalse(response.context['is_owner'])




