from django.contrib.auth.models import User
from django.test import TestCase

from ..forms.register_form import RegisterForm


class RegisterFormTest(TestCase):

    def setUp(self) -> None:
        self.data = {
            'username': 'Breno',
            'surname': 'Adm',
            'email': 'breninhoadm@gmail.com',
            'password': 'devbr123',
            'password2': 'devbr123',
        }

        return super().setUp()

    def create_user(
        self,
        username: str = 'Breno',
        surname: str = 'Adm', 
        email: str = 'breninhoadm@gmail.com', 
        password: str = 'devbr123'
        ):
        return User.objects.create_user(username=username, first_name=surname, email=email, password=password)


    def test_fields_label(self):
        labels_values = [
            ('username', 'Username'),
            ('surname', 'Surname'),
            ('email', 'E-mail'),
            ('password', 'Password'),
            ('password2', 'Repeat your password'),
        ]

        form = RegisterForm()
        for field, label in labels_values:
            with self.subTest(field=field, label=label):
                self.assertEqual(form[field].label, label)

    def test_field_username_is_longer_than_150_characteres(self):
        self.data['username'] = 'A' * 151
        form = RegisterForm(self.data)
        

        self.assertFalse(form.is_valid())
    
    def test_field_surname_is_longer_than_50_characteres(self):
        self.data['surname'] = 'A' * 51
        form = RegisterForm(self.data)

        self.assertFalse(form.is_valid())
    

    # Custom validation tests
    def test_field_username_already_exists_in_the_database_the_form_cannot_be_valid(self):
        # Created a new user
        self.create_user()

        self.data['email'] = 'breninhoplayhard@gmail.com'
        form = RegisterForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_field_email_already_exists_in_the_database_the_form_cannot_be_valid(self):
        # Created a new user
        self.create_user()

        self.data['username'] = 'Bruno'
        form = RegisterForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_field_email_is_not_valid(self):
        self.data['email'] = 'email'
        form = RegisterForm(self.data)

        self.assertFalse(form.is_valid())

        self.data['email'] = 'email@email.com'
        form = RegisterForm(self.data)

        self.assertTrue(form.is_valid())
    
    def test_field_surname_is_less_than_3_not_valid(self):
        # Remove spaces before validation
        self.data['surname'] = ' ' * 5
        form = RegisterForm(self.data)

        self.assertFalse(form.is_valid())

        self.data['surname'] = 'bu'
        form = RegisterForm(self.data)
        self.assertFalse(form.is_valid())

        self.data['surname'] = 'bruninhoclash'
        form = RegisterForm(self.data)
        self.assertTrue(form.is_valid())

    
    def test_field_password_is_less_than_5_characters_not_valid(self):
        self.data['password'] = '1234'
        self.data['password2'] = '1234'

        form = RegisterForm(self.data)
        self.assertFalse(form.is_valid())

        self.data['password'] = '12345'
        self.data['password2'] = '12345'
        form = RegisterForm(self.data)
        self.assertTrue(form.is_valid())
    
    def test_field_password2_is_less_than_5_characters_not_valid(self):
        self.data['password'] = '1234'
        self.data['password2'] = '1234'

        form = RegisterForm(self.data)
        self.assertFalse(form.is_valid())

        self.data['password2'] = '12345'
        self.data['password'] = '12345'
        form = RegisterForm(self.data)
        self.assertTrue(form.is_valid())

    def test_password_and_password2_not_be_equals_the_form_is_not_valid(self):
        self.data['password'] = '1' * 10
        self.data['password2'] = '2' * 10
        
        form = RegisterForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_form_is_valid(self):
        form = RegisterForm(self.data)
        self.assertTrue(form.is_valid())
