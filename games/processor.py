# This file is for processing games from mongodb and formatting them for a model.
import datetime

from soccer.games.models import Game
from soccer.teams.models import Team



def check_game(d):
    """
    Make sure that the data you are trying to insert is consistent with other data.
    """

    # This should probably be the only way that a game gets inserted.
    # Need a pre-save hook for games?
    g = Game.objects.filter(date=d['date'], 
                            home_team=d['home_team'], 
                            away_team=d['away_team']
                            )

    gx = g[0]

    # Game already exists. Need to check that things match
    if g:
        if gx.location != '' and d.get('location') != gx.location:
            raise # ConsistencyError

        if gx.competition != '' and d.get('competition') != gx.competition:
            raise # ConsistencyError

        if gx.notes != '' and d.get('notes') != gx.notes:
            raise # ConsistencyError
            


def insert_game(d):
    """
    Insert data into extant game object if possible, otherwise create a new one.
    """
    g = Game.objects.filter(date=d['date'], 
                            home_team=d['home_team'], 
                            away_team=d['away_team']
                            )

    if not g:
        Game.objects.create(**d)

    else:
        gx = g[0]
        if d.get('location') and gx.location == '':
            gx.location = d.get('location')

        if d.get('competition') and gx.competition == '':
            gx.competition = d.get('competition')

        if d.get('notes') and gx.notes == '':
            gx.notes = d.get('notes')

        gx.save()


            

    

def process_mls_game(d):

    # We are not sure what the competition of any of these games is.

    home_team = Team.objects.get_team(d['home_team'])
    away_team = Team.objects.get_team(d['away_team'])

    dt = datetime.datetime.strptime(d['date'].strip(), '%A, %B %d, %Y')
                            d


    nd = {
        '
        
        

