import re

from django.db import models

from soccer.players.models import Person
from soccer.teams.models import Team


class Game(models.Model):
    date = models.DateField()
    neutral = models.BooleanField(default=False)
    
    home_team = models.ForeignKey(Team, related_name="home_games")
    home_score = models.IntegerField()

    away_team = models.ForeignKey(Team, related_name="away_games")
    away_score = models.IntegerField()

    competition = models.CharField(max_length=255)

    class Meta:
        ordering = ('date',)
        unique_together = [('home_team', 'date'), ('away_team', 'date')]


    def score(self):
        return "%s - %s" % (self.home_score, self.away_score)

    @property
    def home_players(self):
        return self.gameappearance_set.all()
    

    def __unicode__(self):
        return u"%s: %s v %s" % (self.date, self.home_team, self.away_team)



class GameGoal(models.Model):

    game = models.ForeignKey(Game)

    scorer = models.CharField(max_length=255)
    assist_1 = models.CharField(max_length=255)
    assist_2 = models.CharField(max_length=255)
    minute = models.IntegerField()

    penalty = models.BooleanField()

    def __unicode__(self):
        return "%s: %s" % (self.game, self.minute)

class GamePlayed(models.Model):
    
    game = models.ForeignKey(Game)

    player = models.CharField(max_length=255)
    
    on = models.IntegerField()
    off = models.IntegerField()

    def __unicode__(self):
        return "%s: %s" % (self.game, self.player)


class GoalRecord(models.Model):
    game = models.ForeignKey(Game, related_name="goals")
    team = models.ForeignKey(Team)
    
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.description

    def parse_assist(self, text):
        penalty = False
        p = re.match("(\d+)\s*pen")
        t = re.match("(\d_)")
        if r:
            minute = int(r.groups()[0])
            penalty = True
        elif t:
            minute = int(t.groups()[0])
        else:
            pass



        


    def parse(self):
        """A method for getting the corrrect description of GoalRecords."""
        goal_strings = [e.strip() for e in self.description.split(";")]
        for s in goal_strings:
            a_match = re.search(".*?\((?P<assists>.*?)\).*", self.description)
            if not a_match:
                g_match = re.search("(\S+) (\d+)", self.description)
                player = g_match.groups()[0]
                minute = int(g_match.groups()[1])
                #print player, minute
            
            else:
                assist_text = a_match.groups()[0].strip()
                if assist_text == "pk":
                    g_match = re.search("^(.*?)\(pk\) (\d+)", self.description)
                    if g_match:
                        player = g_match.groups()[0]
                        minute = int(g_match.groups()[1])

                elif assist_text == "unassisted":
                    g_match = re.search("^(.*?)\(unassisted ?\) (\d+)", self.description)
                    if g_match:
                        player = g_match.groups()[0]
                        minute = int(g_match.groups()[1])


                elif "," in assist_text:
                    players = assist_text.split(",")
                    g_match = re.search("^(.*?)\(.*?\) (\d+)", self.description)
                    if g_match:
                        player = g_match.groups()[0]
                        minute = int(g_match.groups()[1])
                    else:
                        print self.description
                    #print players
                else:
                    pass
            
        

        

    def can_parse(self):
        try:
            self.parse()
            return True
        except:
            return False
        
     

class GameAppearance(models.Model):
    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)

    player = models.ForeignKey(Person)

    on = models.IntegerField()
    off = models.IntegerField()
    
    def __unicode__(self):
        return "%s: %s" % (self.game, self.player)



    


    
