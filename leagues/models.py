from django.db import models

from soccer.places import City

# Create your models here.

class Confederatoin(models.Model):
    full_name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=50)

class League(models.Model):
    name = models.CharField(max_length=50)
    confederation = models.ForeignKey(Confederation, related_name='leagues')


class Team(models.Model):
    name = models.CharField(max_length=50)
    league = models.ForeignKey(League, related_name='teams')
    city = modelsForeignKey(City, related_name='teams')
    founded = models.IntegerField()
    
