from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Event

class NewEventFormTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form_new_num6(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 302)

        event = Event.objects.get(id=1)
        self.assertEqual(event.reporter_first, 'Test1First')

    def test_form_new_num8(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '81234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 302)

        event = Event.objects.get(id=1)
        self.assertEqual(event.reporter_first, 'Test1First')

    def test_form_new_num9(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '91234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 302)

        event = Event.objects.get(id=1)
        self.assertEqual(event.reporter_first, 'Test1First')

    def test_form_new_no_add_desc(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': '', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 302)

        event = Event.objects.get(id=1)
        self.assertEqual(event.reporter_first, 'Test1First')

    def test_form_new_inv_reporter_first(self):
        form_data = {
            'reporter_first': '', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_reporter_last(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': '',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_phone_number_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '6123456', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_phone_number_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '51234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_phone_number_3(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '612345678', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_postal_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_postal_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '12345',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_postal_3(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '1234567',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_assist_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'E',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_assist_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': '',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

class NewEventFormTestLoggedIn(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='test')
        user.set_password('1973qwER')
        user.save()
        self.client.login(username="test", password="1973qwER")

    def test_form_new_num6(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 302)

        event = Event.objects.get(id=1)
        self.assertEqual(event.reporter_first, 'Test1First')

    def test_form_new_num8(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '81234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 302)

        event = Event.objects.get(id=1)
        self.assertEqual(event.reporter_first, 'Test1First')

    def test_form_new_num9(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '91234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 302)

        event = Event.objects.get(id=1)
        self.assertEqual(event.reporter_first, 'Test1First')

    def test_form_new_no_add_desc(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': '', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 302)

        event = Event.objects.get(id=1)
        self.assertEqual(event.reporter_first, 'Test1First')

    def test_form_new_inv_reporter_first(self):
        form_data = {
            'reporter_first': '', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_reporter_last(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': '',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_phone_number_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '6123456', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_phone_number_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '51234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_phone_number_3(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '612345678', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_postal_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_postal_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '12345',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_postal_3(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '1234567',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_assist_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'E',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_form_new_inv_assist_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': '',
        }
        response = self.client.post(reverse('event:new'), form_data)
        self.assertEqual(response.status_code, 200)


class UpdateEventFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='test')
        user.set_password('1973qwER')
        user.save()
        self.client.login(username="test", password="1973qwER")
        Event.objects.create(
            reporter_first="Update1First", reporter_last="Test1Last",
            phone_number="61234567", postal_code="499614",
            add_desc="Test1Desc", assist_type="A",
        )

    def test_form_update_reporter_first(self):
        form_data = {
            'reporter_first': 'Test1FirstChange', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Event.objects.get(id=1).reporter_first, 'Test1FirstChange'
        )

    def test_form_update_reporter_last(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1LastChange',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Event.objects.get(id=1).reporter_last, 'Test1LastChange'
        )

    def test_form_update_phone_number(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '91234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Event.objects.get(id=1).phone_number, '91234567'
        )

    def test_form_update_postal_code(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '760646',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Event.objects.get(id=1).postal_code, '760646'
        )

    def test_form_update_add_desc(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': '', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Event.objects.get(id=1).add_desc, ''
        )

    def test_form_update_assist_type(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'B',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Event.objects.get(id=1).assist_type, 'B'
        )

    def test_form_update_inv_reporter_first(self):
        form_data = {
            'reporter_first': '', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_reporter_last(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': '',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_phone_number_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_phone_number_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '5123456', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_phone_number_3(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '612345678', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_postal_code_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_postal_code_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '49961',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_postal_code_3(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '4996145',
            'add_desc': 'Test1Desc', 'assist_type': 'A',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_assist_type_1(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': '',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)

    def test_form_update_inv_assist_type_2(self):
        form_data = {
            'reporter_first': 'Test1First', 'reporter_last': 'Test1Last',
            'phone_number': '61234567', 'postal_code': '499614',
            'add_desc': 'Test1Desc', 'assist_type': 'E',
        }
        response = self.client.post(
            reverse('event:edit', kwargs={'pk': 1}), form_data
        )
        self.assertEqual(response.status_code, 200)


class DeleteEventFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='test')
        user.set_password('1973qwER')
        user.save()
        self.client.login(username="test", password="1973qwER")
        Event.objects.create(
            reporter_first="Update1First", reporter_last="Test1Last",
            phone_number="61234567", postal_code="499614",
            add_desc="Test1Desc", assist_type="A",
        )

    def test_form_update_inv_assist_type_2(self):
        response = self.client.post(
            reverse('event:delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
