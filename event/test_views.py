from django.contrib.auth.models import User
from django.test import Client, TestCase

from .models import Event

class EventViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        Event.objects.create(
            reporter_first="Test1First", reporter_last="Test1Last",
            phone_number="61234567", postal_code="499614",
            add_desc="Test1Desc", assist_type="A",
        )
        user = User.objects.create(username='test')
        user.set_password('1973qwER')
        user.save()

    # Not Logged In Test
    def test_view_index(self):
        response = self.client.get('/event/')
        self.assertEquals(response.status_code, 200)

    def test_view_new(self):
        response = self.client.get('/event/new')
        self.assertEquals(response.status_code, 200)

    def test_event_view(self):
        response = self.client.get('/event/1/')
        self.assertEquals(response.status_code, 200)

    # Logged In Test
    def test_view_index_li(self):
        self.client.login(username="test", password="1973qwER")
        response = self.client.get('/event/')
        self.assertEquals(response.status_code, 200)

    def test_view_new_li(self):
        self.client.login(username="test", password="1973qwER")
        response = self.client.get('/event/new')
        self.assertEquals(response.status_code, 200)

    def test_event_view_li(self):
        self.client.login(username="test", password="1973qwER")
        response = self.client.get('/event/1/')
        self.assertEquals(response.status_code, 200)

    def test_event_edit(self):
        self.client.login(username="test", password="1973qwER")
        response = self.client.get('/event/1/edit')
        self.assertEquals(response.status_code, 200)

    def test_event_resolve(self):
        self.client.login(username="test", password="1973qwER")
        response = self.client.get('/event/1/resolve')
        self.assertEquals(response.status_code, 200)
