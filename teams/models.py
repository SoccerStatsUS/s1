from django.core.cache import cache
from django.db import models

from soccer.leagues.models import League

team_mapping = {
    u'CHI': "Chicago Fire",
    u'CHV':  'Chivas USA',
    u'CLB': 'Columbus Crew',
    u'COL': 'Colorado Rapids',
    u'DAL':'FC Dallas',
    u'DC': 'D.C. United',
    u'HOU': 'Houston Dynamo',
    u'KC': 'Kansas City Wizards',
    u'LA': 'Los Angeles Galaxy',
    u'NE': 'New England Revolution',
    u'NY': 'New York Red Bulls',
    u'PHI': 'Philadelphia Union',
    u'Pool': 'No Team',
    u'RSL': 'Real Salt Lake',
    u'SEA': 'Seattle Sounders',
    u'SJ': 'San Jose Earthquakes',
    u'TFC': 'Toronto FC',
    }


def seasons_with_stats_by_team():
    # Would like to make a lot more efficient.
    from soccer.stats.models import SeasonStat
    CACHE_KEY = "seasons_with_stats_by_team"
    d = cache.get(CACHE_KEY)
    if d is None:
        d = {}
        for s in SeasonStat.objects.all():
            team = s.team
            year = s.year
            if team not in d:
                d[team] = set()
            d[team].add(year)

        for k, v in d.items():
            d[k] = sorted(v)
        cache.set(CACHE_KEY, d, 24 * 60 * 60)
    return d


class TeamManager(models.Manager):
    def get_team(self, name):
        from soccer.teams.aliases import mapping
        if name in mapping:
            name = mapping[name]
        return Team.objects.get(name=name)


class Team(models.Model):
    name = models.CharField(max_length=200)

    # Let's get rid of short name! It's really just another alias.
    # No way, it's useful when you want to display a better name.
    # Let's just be clear that it's very optional.
    short_name = models.CharField(max_length=200)
    slug = models.SlugField()
    nickname = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    
    # League isn't really a property of a team...
    league = models.ForeignKey(League)
    founded = models.IntegerField(null=True, blank=True)
    defunct = models.BooleanField(default=False)

    objects = TeamManager()

    class Meta:
        ordering = ('short_name',)

    def fancy_name(self):
        return self.name

    @property
    def normal_name(self):
        if self.short_name:
            return self.short_name
        return self.name

    def years_with_stats(self):
        return seasons_with_stats_by_team().get(self, [])
        
    def __unicode__(self):
        return self.short_name


class Stadium(models.Model):
    name = models.CharField(max_length=200)
    opened = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name
    
