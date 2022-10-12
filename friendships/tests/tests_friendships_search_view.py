from django.urls import reverse

from .tests_friendships_base import FriendshipsBaseTest


class SearchViewTest(FriendshipsBaseTest):
    def setUp(self) -> None:
        self.url = reverse('friendships:search')
        return super().setUp()

    def test_search_view_returns_status_code_200_OK(self):
        # you must be logged in
        self.client.login(username='Breno', password='123456')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_search_view_redirect_for_login_if_is_not_logged(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
    
    def test_search_view_shows_the_profiles_with_the_correctly_fetched_nickname(self):
        self.client.login(username='Breno', password='123456')

        # Create profile to be found
        random_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        random_profile = self.create_profile(user=random_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # Page shows profile with successfully
        response = self.client.get(self.url+'?surname=maga')
        self.assertContains(response, 'magali CS GO')
    
    def test_search_view_shows_correct_text_if_no_profile_is_found(self):
        self.client.login(username='Breno', password='123456')

        # Create profile to be found
        random_user = self.create_user(username='magali', email='magali@gmail.com', password='12121212')
        random_profile = self.create_profile(user=random_user, slug='magali', surname='magali CS GO', bio='Chama chama')

        # does not shows any profile
        response = self.client.get(self.url+'?surname=mub')
        self.assertContains(response, "We didn't find anything for your search.")

        # does not show its own profile
        response = self.client.get(self.url+'?surname=Breno')
        self.assertContains(response, "We didn't find anything for your search.")

        
