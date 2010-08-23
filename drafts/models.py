from django.db import models

from soccer.players.models import Person
from soccer.teams.models import Team

def no_player():
    return Person.objects.get(name='No Player')


class Draft(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    year = models.IntegerField()

    def __unicode__(self):
        return self.name
    

class Pick(models.Model):
    draft = models.ForeignKey(Draft)
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Person, default=no_player)
    name = models.CharField(max_length='250')
    number = models.IntegerField()
