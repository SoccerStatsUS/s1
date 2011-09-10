from django.db import models 

class Country(models.Model):
    "A country in the world."""

    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=250) # unused
    population = models.IntegerField()
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class State(models.Model):
    """A state (or other territory) somewhere in the world."""

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    population = models.IntegerField()

    def __unicode__(self):
        return "%s, %s" % (self.name, self.country)

class City(models.Model):
    """A city somewhere in the world."""

    slug = models.CharField(max_length=50, unique=True, null=False)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, default='U.S.A.')
    #location = models.PointField(null=True, blank=True)

    
