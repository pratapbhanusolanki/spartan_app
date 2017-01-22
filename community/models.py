from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Major(models.Model):
    acronym = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s (%s)" % (self.acronym, self.name)
class Type(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    major = models.ForeignKey(Major)
    created_date = models.DateTimeField(
            default=timezone.now)
    class_type = models.ForeignKey(Type)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    categories = models.ManyToManyField(Category)
  
    def __str__(self):
        return self.name

class Event(models.Model):
	name = models.CharField(max_length=200)
	creator = models.ForeignKey(User)
	club = models.ForeignKey(Club)
	description = models.TextField()
	location = models.CharField(max_length=400)
	start_time = models.DateTimeField()
	#Many to many relationship
	categories = models.ManyToManyField(Category)
	majors = models.ManyToManyField(Major)
	class_types = models.ManyToManyField(Type)

	end_time = models.DateTimeField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name







