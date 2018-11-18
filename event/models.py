from datetime import datetime
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.urls import reverse  # generate URL by reversing the patterns
# from geopy import geocoders
# from geopy.geocoders import GoogleV3
from uuid import uuid4

import json
import requests


# Functions Here
def create_title():
    date = datetime.now().strftime("%Y%m%d-%H%M-")
    return date+str(uuid4().int)[:4]


def get_address(postal):
    url = (
        "https://developers.onemap.sg/commonapi/search?searchVal="
        + postal + "&returnGeom=N&getAddrDetails=Y"
    )
    response = requests.get(url)
    content = response.content.decode("utf8")
    js = json.loads(content)
    return (
        js["results"][0]["BLK_NO"]
        + ' ' + js["results"][0]["ROAD_NAME"]
        + ' ' + js["results"][0]["POSTAL"]
    ).title()


def get_lat(postal):
    url = (
        "https://developers.onemap.sg/commonapi/search?searchVal="
        + postal + "&returnGeom=Y&getAddrDetails=N"
    )
    response = requests.get(url)
    content = response.content.decode("utf8")
    js = json.loads(content)
    return (
        js["results"][0]["LATITUDE"]
    )


def get_long(postal):
    url = (
        "https://developers.onemap.sg/commonapi/search?searchVal="
        + postal + "&returnGeom=Y&getAddrDetails=N"
    )
    response = requests.get(url)
    content = response.content.decode("utf8")
    js = json.loads(content)
    return (
        js["results"][0]["LONGITUDE"]
    )


# Models Here
class Event(models.Model):
    title = models.CharField(
        max_length=30, default=create_title,
        blank=True, editable=False
    )
    # auto_now_add renders field un-editable
    date_time = models.DateTimeField(auto_now_add=True)
    reporter_first = models.CharField(max_length=30)
    reporter_last = models.CharField(max_length=30)
    phone_number = models.CharField(
        max_length=8, default='',
        validators=[
            MinLengthValidator(8),
            RegexValidator(r'\b[6,8,9]\d{7}\b$')
        ]
    )
    postal_code = models.CharField(
        max_length=6, default='',
        validators=[
            MinLengthValidator(6),
            RegexValidator(r'\b\d{6}\b$')
        ]
    )
    address = models.CharField(
        max_length=100, default='', editable=False
    )
    add_desc = models.CharField(
        max_length=200, default='',
        blank=True,
    )
    lat = models.CharField(
        max_length=100, default='0', editable=False
    )
    long = models.CharField(
        max_length=100, default='0', editable=False
    )
    ASSIST = (
        ('A', 'Emergency Ambulance'),
        ('B', 'Rescue and Evacuation'),
        ('C', 'Fire-Fighting'),
        ('D', 'Gas Leak Control'),
    )
    assist_type = models.CharField(max_length=1, choices=ASSIST)

    def save(self, *args, **kwargs):
        # geolocator = geocoders.GoogleV3(
        #     api_key='AIzaSyCwoGSZg_KbqCiv9Ujk72bl8XYn7hdsnI0',
        #     format_string="%s, Singapore SG"
        # )
        # location = geolocator.geocode(self.postal_code)
        self.address = get_address(self.postal_code)
        self.lat = get_lat(self.postal_code)
        self.long = get_long(self.postal_code)
        super(Event, self).save(*args, **kwargs)

    # String for representing Event model
    def __str__(self):
        return self.title

    # Returns the url to access a particular Event instance
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])
