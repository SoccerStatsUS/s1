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




class Team(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    slug = models.SlugField()
    nickname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    league = models.ForeignKey(League)
    founded = models.IntegerField(null=True, blank=True)
    defunct = models.BooleanField()

    class Meta:
        ordering = ('short_name',)
        
        

    def __unicode__(self):
        return self.name


class Stadium(models.Model):
    name = models.CharField(max_length=200)
    opened = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name
    
