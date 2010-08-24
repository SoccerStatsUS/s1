from django.db import models

from soccer.places.models import Country
from soccer.players.aliases import mapping


class PersonManager(models.Manager):
    def get_person(self, name):
        if name in mapping:
            name = mapping[name]
        return Person.objects.get(name=name)

    
class Person(models.Model):

    # Identity
    name = models.CharField(max_length=500)
    full_name = models.CharField(max_length=500)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    nickname = models.CharField(max_length=100, blank=True)

    # Stats
    height = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=250, null=True, blank=True)
    nationality = models.ForeignKey(Country)

    # Cruft
    mls_slug = models.CharField(max_length=250, blank=True)

    objects = PersonManager()

    class Meta:
        ordering = ('last_name',)

    @property
    def get_name(self):
        if self.nickname:
            return self.nickname
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        return self.name

    def __unicode__(self):
        return self.name
        

