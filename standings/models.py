from django.db import models


class Place(models.Model):

    """
    Represents a standings line.

    team   w l t gf ga
    Dallas 5 3 2 12  9

    """
    # This doesn't necessarily apply just to a team.
    # A player could just easily have one of these,
    # or a group of players.
    # How does Manchester United perform with Giggs and Beckham on the field between 2008 and 2010?
    # Could be anything that you can get a mongo collection for.
    # As such, should probably have a name, and no required foreign keys.

    team = models.ForeignKey(Team)

    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()

    points_system = models.CharField(max_length=255)


    @property
    def games(self):
        return self.wins + self.losses + self.ties

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against
        
    @property
    def points(self):
        # Should customize this significantly.
        return self.wins * 3 + self.ties

    def points_per_game(self):
        return float(self.points) / self.games

    def goal_difference_per_game(self):
        return float(self.goal_difference) / self.games
