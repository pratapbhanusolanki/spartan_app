from __future__ import unicode_literals

# from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib import admin
from location_field.models.spatial import LocationField
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    #location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    #objects = models.GeoManager()
    food_pref = models.CharField(max_length=20)
    occupation = models.CharField(max_length=30)
    organisation = models.CharField(max_length=50)
    about_me = models.TextField()
    nationality = models.CharField(max_length=30)
    languages = models.CharField(max_length=100)
    roommate_gender_pref = models.CharField(max_length=20)
    interests = models.CharField(max_length=100)
    photo = models.ImageField(width_field=32, height_field=32,blank=True)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ['age', 'gender', 'food_pref', 'occupation', 'organisation', 'about_me','nationality', 'languages','roommate_gender_pref',
        'interests', 'photo']


class Feature(models.Model):
    name = models.CharField(max_length=100)

class FeatureMap(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)
    acc_score = models.FloatField()

class Question(models.Model):
    name = models.CharField(max_length=500)
    feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)
    is_self = models.BooleanField()

class Option(models.Model):
    name = models.CharField(max_length=500)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

class Answer(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.FloatField()
    is_self = models.BooleanField()
    feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)

class PeerReview(models.Model):
    scorer_id = models.ForeignKey(Profile, related_name='by',on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, related_name='of',on_delete=models.CASCADE)
    is_roommate = models.BooleanField()
    date_time = models.DateTimeField(auto_now=True)

class SelfReview(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)