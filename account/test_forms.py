from django.test import TestCase

from .forms import SignUpForm


class SignUpFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'responder0',
            'password1': '1973qwER',
            'password2': '1973qwER',
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertTrue(form.is_valid())

    def test_username_inv_character(self):
        form_data = {
            'username': '/*&#0',
            'password1': '1973qwER',
            'password2': '1973qwER',
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())

    def test_password_inv_password2(self):
        form_data = {
            'username': 'responder0',
            'password1': '1973qwER',
            'password2': '1973qwRE',  # RE, instead of ER
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())

    def test_password_inv_lesschar(self):
        form_data = {
            'username': 'responder0',
            'password1': '1973qwE',
            'password2': '1973qwE',
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())

    def test_password_inv_alldigit(self):
        form_data = {
            'username': 'responder0',
            'password1': '12345678',
            'password2': '12345678',
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())

    def test_password_inv_common(self):
        form_data = {
            'username': 'responder0',
            'password1': '1234qwER',
            'password2': '1234qwER',
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())

    def test_password_inv_missingDigit(self):
        form_data = {
            'username': 'responder0',
            'password1': 'qwERqwER',
            'password2': 'qwERqwER',
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())

    def test_password_inv_missingLower(self):
        form_data = {
            'username': 'responder0',
            'password1': '1973QWER',
            'password2': '1973QWER',
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())

    def test_password_inv_missingUpper(self):
        form_data = {
            'username': 'responder0',
            'password1': '1973qwer',
            'password2': '1973qwer',
            'code': 'ssad3003_signup',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())

    def test_password_inv_code(self):
        form_data = {
            'username': 'responder0',
            'password1': '1973qwer',
            'password2': '1973qwer',
            'code': 'codenotcorrect3003',
        }
        form = SignUpForm(data=form_data)
        self. assertFalse(form.is_valid())
