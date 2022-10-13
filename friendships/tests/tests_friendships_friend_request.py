from django.urls import reverse

from ..models import Friend
from .tests_friendships_base import FriendshipsBaseTest


class FriendRequestTest(FriendshipsBaseTest):
    def setUp(self) -> None:
        self.url = reverse('friendships:friend-request', kwargs={'slug': 'breno'})
        return super().setUp()
    
    def test_friend_request_view_redirect_for_login_if_is_not_logged(self):
        response = self.client.get(self.url, follow=True)

        # Redirect with successfully for login.html
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_friend_request_view_returns_status_code_404_if_no_profile_is_found_with_the_slug(self):
        self.client.login(username='Breno', password='123456')

        url_slug_not_exists = reverse('friendships:friend-request', kwargs={'slug': 'user-random'})
        response = self.client.get(url_slug_not_exists)
        self.assertEqual(response.status_code, 404)
    
    def test_friend_request_view_the_profile_owner_cannot_create_a_friend_request_for_himself(self):
        self.client.login(username='Breno', password='123456')

        self.client.get(self.url)
        request_friend_exists = Friend.objects.filter(pk=1).exists()

        self.assertFalse(request_friend_exists)
    
    def test_friend_request_view_the_profile_owner_is_already_a_friend_and_cannot_create_another_friend_request(self):
        self.client.login(username='Breno', password='123456')

        url_friend = reverse('friendships:friend-request', kwargs={'slug': 'magali'})

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # Create friendship
        self.create_friendship(profile_1=self.profile, profile_2=friend_profile, status='A')
        
        self.client.get(url_friend)
        new_friend_requests = Friend.objects.filter(id_requester=self.profile, id_receiver=friend_profile, status='P').exists()

        self.assertFalse(new_friend_requests)
    
    def test_friend_request_view_the_profile_owner_already_has_a_request_as_pending_cannot_create_another_friend_request(self):
        self.client.login(username='Breno', password='123456')

        url_friend = reverse('friendships:friend-request', kwargs={'slug': 'magali'})

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # Create friendship like status Pending
        self.create_friendship(profile_1=self.profile, profile_2=friend_profile, status='P')

        self.client.get(url_friend)
        friend_requests = Friend.objects.filter(id_requester=self.profile, id_receiver=friend_profile, status='P')
        self.assertEqual(len(friend_requests), 1)
    
    def test_friend_request_view_the_profile_owner_has_no_friend_request_with_the_other_profile_can_create_a_new_one(self):
        self.client.login(username='Breno', password='123456')

        url_friend = reverse('friendships:friend-request', kwargs={'slug': 'magali'})

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # Create a new friend request
        self.client.get(url_friend)

        friend_requests = Friend.objects.filter(id_requester=self.profile, id_receiver=friend_profile, status='P').exists()

        self.assertTrue(friend_requests)

    def test_friend_request_view_the_profile_owner_has_a_friend_request_but_it_was_previously_denied_can_create_a_new_request(self):
        self.client.login(username='Breno', password='123456')

        url_friend = reverse('friendships:friend-request', kwargs={'slug': 'magali'})

        # Create profile friend
        friend_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        friend_profile = self.create_profile(user=friend_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # Create friendship like status Denied
        self.create_friendship(profile_1=self.profile, profile_2=friend_profile, status='D')
        
        self.client.get(url_friend)

        friend_requests = Friend.objects.filter(id_requester=self.profile, id_receiver=friend_profile, status='P').exists()

        self.assertTrue(friend_requests)


