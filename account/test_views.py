from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


# Testing Here
class AccountViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup(self):
        response = self.client.get('/account/')
        self.assertEquals(response.status_code, 200)

    def test_signup_2(self):
        response = self.client.get('/account/signup/')
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/account/login/')
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        user = User.objects.create(username='test')
        user.set_password('1973qwER')
        user.save()
        self.client.login(username="test", password="1973qwER")
        self.assertRedirects(
            self.client.get('/account/logout/'),
            '/event/',
            302
        )


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='test')
        user.set_password('1973qwER')
        user.save()

    def login_form_test(self):
        form_data = {
            'username': 'test', 'password': '1973qwER'
        }
        response = self.client.post(
            reverse('account:login', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 302)
