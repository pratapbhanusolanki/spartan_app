from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    description = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    major = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=100)
    subsciptions = models.CommaSeparatedIntegerField()

class Category(models.Model):
    name = models.CharField(max_length=30)

class Events(models.Model):
    name = models.CharField(max_length=100)
    club_id = models.IntegerField()
    rsvps = models.CommaSeparatedIntegerField()