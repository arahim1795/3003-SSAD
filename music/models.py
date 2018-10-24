from django.db import models
from django.core.validators import MaxValueValidator
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + " - " + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

class Operator(models.Model):
    operator_name = models.CharField(max_length = 50)
    operator_id = models.IntegerField(validators=MaxValueValidator(99999999999))
    operator_phone = models.IntegerField(max_length=8)

    def __Operator__(self):
        return self.operator_id + " - " + self.operator_name + " - " + self.operator_phone


class Taskforce(models.Model):
    taskforce_name = models.CharField(max_length = 50)
    taskforce_id = models.IntegerField(max_length=10)
    taskforce_phone = models.IntegerField(max_length=8)

    def __Taskforce__(self):
        return self.taskforce_id + " - " + self.taskforce_name + " - " + self.taskforce_phone

class PMOffice(models.Model):
    prime_minister_office_name = models.CharField(max_length=50)
    prime_minister_office_id = models.IntegerField(max_length=10)
    prime_minister_office_phone = models.IntegerField(max_length=8)
    prime_minister_office_email = models.CharField(max_length=70)

    def __PMOffice__(self):
        return self.prime_minister_office_id + " - " + self.prime_minister_office_name + " - " + self.prime_minister_office_phone + " - " + self.prime_minister_office_email

class Shelter(models.Model):
    shelter_name = models.CharField(max_length=50)
    shelter_description = models.CharField(max_length=250)
    shelter_address = models.CharField(max_length=70)
    shelter_postal_code = models.IntegerField(max_length=6)
    shelter_id = models.IntegerField(max_length=10)

    def __Shelter__(self):
        return self.shelter_id + " - " + self.shelter_name + " - " + self.shelter_address + " - " + self.shelter_postal_code + " - " + self.shelter_description

class Incident(models.Model):
    incident_type = models.CharField(max_length=10)
    incident_time = models.DateTimeField(auto_now_add=True, blank=True)
    incident_postal_code = models.IntegerField(max_length=6)
    incident_id = models.IntegerField(max_length=10)
    incident_response = models.BooleanField(default=False)
    incident_reported_by = models.CharField(max_length=50)

    def __Incident__(self):
        return self.incident_id + " - " + self.incident_postal_code + " - " + self.incident_time + " - " + self.incident_type + " - " + self.incident_reported_by + " - " + self.incident_response