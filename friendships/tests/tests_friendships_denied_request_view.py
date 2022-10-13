from django.urls import reverse

from ..models import Friend
from .tests_friendships_base import FriendshipsBaseTest


class DeniedRequestViewTest(FriendshipsBaseTest):
    def setUp(self) -> None:
        self.url = reverse('friendships:profile-denied', kwargs={'id': 1})
        return super().setUp()
    
    def test_denied_request_view_redirect_for_login_if_is_not_logged(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
    
    def test_denied_request_the_profile_owner_denies_the_request_and_modifies_the_status_correctly(self):
        # you must be logged in
        self.client.login(username='Breno', password='123456')

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # Create request friendship status Pending
        self.create_friendship(profile_1=self.profile, profile_2=friend_profile, status='P')

        self.client.get(self.url)

        friend_request_denied = Friend.objects.filter(
            pk=1,
            id_requester = self.profile,
            id_receiver = friend_profile,
            status='D'
        ).exists()

        self.assertTrue(friend_request_denied)

    def test_denied_request_the_profile_the_owner_tries_to_deny_a_request_that_does_not_exist_or_does_not_belong_to_him(self):
        # you must be logged in
        self.client.login(username='Breno', password='123456')

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        friend_user_2 = self.create_user(username='magali2', email='magali2@gmail.com', password='12121212')
        friend_profile_2 = self.create_profile(user=friend_user_2, slug='magali2', surname='magali2 CS GO', bio='Chama chama2')

        # Create request friendship status Pending
        self.create_friendship(profile_1=friend_profile, profile_2=friend_profile_2, status='P')

        self.client.get(self.url)

        friend_request_denied = Friend.objects.filter(
            pk=1,
            id_requester = friend_profile,
            id_receiver = friend_profile_2,
            status='D'
        ).exists()

        self.assertFalse(friend_request_denied)
