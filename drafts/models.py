from django.db import models

from soccer.players.models import Person

# Create your models here.


class Draft(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    year = models.IntegerField()
    

class Pick(models.Model):
    draft = models.ForeignKey(Draft)
    team = modles.ForeignKey(Team)
    player = models.ForeignKey(Person)
    number = models.IntegerField()
