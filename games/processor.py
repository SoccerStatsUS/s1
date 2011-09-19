# This file is for processing games from mongodb and formatting them for a model.
import datetime

from soccer.teams.models import Team



def insert_game(d):
    # This should probably be the only way that a game gets inserted.
    # Need a pre-save hook for games?
    g = Game.objects.filter(date=d['date'], 
                            home_team=d['home_team'], 
                            away_team=d['away_team']
                            )


def merge_games(collections):
    # Not sure how to do this?
    # First we want to get games as processed as possible.
    # This means having real datetimes and unique teams. That should be enough for identification.
    # Each team should only have one game on the same day. 
    # We should probably be 
    pass
    

def process_mls_game(d):

    # We are not sure what the competition of any of these games is.

    home_team = Team.objects.get_team(d['home_team'])
    away_team = Team.objects.get_team(d['away_team'])

    dt = datetime.datetime.strptime(d['date'].strip(), '%A, %B %d, %Y')
                            d


    nd = {
        '
        
        

