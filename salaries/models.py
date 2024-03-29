from django.core.cache import cache
from django.db import models


from soccer.players.models import Person
from soccer.teams.models import Team

# Create your models here.


def median_salary(qs, type="base"):
    c = qs.count()
    mid = count / 2
    if count % 2:
        return getattr(qs[mid], type)
    else:
        mids = qs[mid:mid+2]
        attrs = [getattr(e, type) for e in mids]
        return sum(attrs) / 2
    

class SalaryManager(models.Manager):
    
    def median(self, type):
        qs = self.get_query_set()
        count = qs.count()
        mid = count / 2
        if count % 2:
            q = qs[mid]
            return getattr(q, type)
        else:
            q = qs[mid:mid+2] # Gets the item and the next one up.
            attrs = [getattr(e, type) for e in q]
            return sum(attrs) / 2

    def average(self, type):
        qs = self.get_query_set()
        return qs.aggregate(models.Avg(type))
        

    

class Salary(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    player = models.ForeignKey(Person, related_name='salaries')
    year = models.IntegerField(null=False, blank=False)
    team = models.CharField(max_length=50)
    team2 = models.ForeignKey(Team, related_name="salaries")
    position = models.CharField(max_length=50)
    base = models.DecimalField(max_digits=20, decimal_places=2)
    guaranteed = models.DecimalField(max_digits=20, decimal_places=2)

    objects = SalaryManager()

    class Meta:
        ordering = ('-year', 'last_name', 'first_name')
        verbose_name_plural = 'salaries'

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def base_pretty(self):
        return "$%s" % self.base

    @property
    def guaranteed_pretty(self):
        return "$%s" % self.guaranteed

        
    def __unicode__(self):
        return "%s (%s): %s" % (self.full_name, self.year, self.base)

    @staticmethod
    def get_years_for_team(team):
        # This should really be under team.
        # Will move once team has been ported.
        CACHE_KEY = "years:%s" % team
        sorted_years = cache.get(CACHE_KEY)
        if sorted_years is None:
            years = [e[0] for e in Salary.objects.filter(team=team).values_list("year")]
            sorted_years = sorted(set(years))
            cache.set(CACHE_KEY, sorted_years, 60*60*24*7)
        return sorted_years
