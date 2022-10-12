from django.urls import reverse

from .tests_friendships_base import FriendshipsBaseTest


class ProfileEditTest(FriendshipsBaseTest):
    def setUp(self) -> None:
        self.url = reverse('friendships:profile-edit', kwargs={'slug': 'breno'})
        return super().setUp()

    def test_profile_edit_view_returns_status_code_200_OK(self):
        # you must be logged in
        self.client.login(username='Breno', password='123456')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_profile_edit_view_redirect_for_login_if_is_not_logged(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_profile_edit_view_returns_status_code_404_if_no_profile_is_found_with_the_slug(self):
        self.client.login(username='Breno', password='123456')

        url_slug_not_exists = reverse('friendships:profile-edit', kwargs={'slug': 'user-random'})
        response = self.client.get(url_slug_not_exists)
        self.assertEqual(response.status_code, 404)
    
    def test_profile_edit_view_returns_successfully_redirect_to_detail_profile_if_not_profile_owner(self):
        self.client.login(username='Breno', password='123456')

        url_magali = reverse('friendships:profile-edit', kwargs={'slug': 'magali'})

        # Create profile friend
        user_magali = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        profile_magali = self.create_profile(user=user_magali, slug='magali', surname='magali CS GO', bio='Chama chama')

        response = self.client.get(url_magali)
        self.assertRedirects(response, reverse('friendships:profile-detail', kwargs={'slug': profile_magali.slug}), 302)
    
