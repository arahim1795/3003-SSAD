from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

#create database for taskforce and PMO

class Operator(models.Model):
    operator_id = models.IntegerField("Operator ID", primary_key=True)
    operator_name = models.CharField(max_length = 50)
    operator_phone = models.IntegerField("Operator phone", validators=[MaxLengthValidator(8),
                                                                       MinLengthValidator(8)])

    def __str__(self):
        return "Operator " + str(self.operator_id)


class Taskforce(models.Model):
    taskforce_id = models.IntegerField("Taskforce ID", primary_key=True)
    taskforce_name = models.CharField(max_length = 50)
    taskforce_phone = models.IntegerField("Taskforce phone", validators=[MaxLengthValidator(8),
                                                                         MinLengthValidator(8)])

    def __str__(self):
        return "Taskforce " + str(self.taskforce_id)

class PMOffice(models.Model):
    prime_minister_office_id = models.IntegerField("Prime minister office ID", primary_key=True)
    prime_minister_office_name = models.CharField(max_length=50)
    prime_minister_office_phone = models.IntegerField("Prime minister office Phone", validators=[MaxLengthValidator(8),
                                                                                                 MinLengthValidator(8)])
    prime_minister_office_email = models.CharField(max_length=70)

    def __str__(self):
        return "PMO office " + str(self.prime_minister_office_id)

class Shelter(models.Model):
    shelter_id = models.IntegerField("Shelter ID", primary_key=True)
    shelter_name = models.CharField(max_length=50)
    shelter_description = models.CharField(max_length=250)
    shelter_address = models.CharField(max_length=70)
    shelter_postal_code = models.IntegerField("Shelter postal code", validators=[MaxLengthValidator(6),
                                                                                 MinLengthValidator(6)])

    def __str__(self):
        return "Shelter " + str(self.shelter_id)

class Incident(models.Model):
    incident_id = models.IntegerField("Incident ID", primary_key=True)
    incident_type = models.CharField(max_length=10)
    incident_time = models.DateTimeField(blank=True)
    incident_postal_code = models.IntegerField("Incident postal code", validators=[MaxLengthValidator(6),
                                                                                   MinLengthValidator(6)])
    incident_response = models.BooleanField(default=False)
    incident_reported_by = models.CharField(max_length=50)

    def __str__(self):
        return "Incident " + str(self.incident_id)