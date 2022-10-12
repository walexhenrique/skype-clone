from django.urls import reverse

from .tests_friendships_base import FriendshipsBaseTest


class IndexViewTest(FriendshipsBaseTest):
    def setUp(self) -> None:
        self.url = reverse('friendships:index')
        return super().setUp()

    def test_index_view_returns_status_code_200_OK(self):
        # you must be logged in
        self.client.login(username='Breno', password='123456')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_index_view_redirect_for_login_if_is_not_logged(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
    
    def test_index_view_correctly_displays_all_my_added_friends(self):
        # you must be logged in
        self.client.login(username='Breno', password='123456')

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # Create friendship
        self.create_friendship(profile_1=self.profile, profile_2=friend_profile)

        response = self.client.get(self.url)
        self.assertContains(response, 'magali CS GO')
    
    def test_index_view_shows_correct_text_if_no_friends_added(self):
        # you must be logged in
        self.client.login(username='Breno', password='123456')

        response = self.client.get(self.url)
        self.assertContains(response, "You don't have friends.")

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')
        
        # friend request denied not be shown
        self.create_friendship(profile_1=self.profile, profile_2=friend_profile, status='D')

        response = self.client.get(self.url)
        self.assertContains(response, "You don't have friends.")
