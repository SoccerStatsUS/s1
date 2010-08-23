from django.db import models

from soccer.places.models import Country

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=500)
    full_name = models.CharField(max_length=500)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    nickname = models.CharField(max_length=100, blank=True)
    mls_slug = models.CharField(max_length=250, blank=True)
    height = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=250, null=True, blank=True)
    nationality = models.ForeignKey(Country)

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
        return self.get_name
        

