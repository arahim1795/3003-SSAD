from datetime import datetime
from django.test import TestCase

from .models import Event


# Models Testing
class EventModelTestCase(TestCase):
    def setUp(self):
        Event.objects.create(
            reporter_first="Test1First", reporter_last="Test1Last",
            phone_number="61234567", postal_code="499614",
            add_desc="Test1Desc", assist_type="A",
        )

    def test_contents(self):
        event1 = Event.objects.get(id=1)
        self.assertEqual(event1.reporter_first, 'Test1First')
        self.assertEqual(event1.reporter_last, 'Test1Last')
        self.assertEqual(event1.phone_number, '61234567')
        self.assertEqual(event1.postal_code, '499614')
        self.assertEqual(event1.add_desc, 'Test1Desc')
        self.assertEqual(event1.assist_type, 'A')

        self.assertNotEqual(len(event1.title), 0)
        self.assertEqual(event1.date_time.year, datetime.today().year)
        self.assertEqual(event1.date_time.month, datetime.today().month)
        self.assertNotEqual(len(event1.lat), 0)
        self.assertNotEqual(len(event1.long), 0)
