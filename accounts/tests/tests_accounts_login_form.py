from django.test import SimpleTestCase

from ..forms.login_form import LoginForm


class LoginFormTest(SimpleTestCase):
    def test_fields_label(self):
        labels_values = [
            ('username', 'Username'),
            ('password', 'Password'),
        ]

        form = LoginForm()
        for field, label in labels_values:
            with self.subTest(field=field, label=label):
                self.assertEqual(form[field].label, label)
    
    def test_fields_placeholder(self):
        placeholders_values = [
            ('username', 'Ex.: John'),
            ('password', 'Password...'),
        ]

        form = LoginForm()
        for field, placeholder in placeholders_values:
            with self.subTest(field = field, placeholder = placeholder):
                self.assertEqual(placeholder, form[field].field.widget.attrs['placeholder'])

    def test_form_is_valid(self):
        data = {
            'username': 'Breno',
            'password': '123456'
        }

        form = LoginForm(data)
        self.assertTrue(form.is_valid())
