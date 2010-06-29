from django.db import models

from soccer.places.models import City

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    height = models.IntegerField(null=True, blank=True)
    birthplace = models.ForeignKey(City, related_name='players', null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
