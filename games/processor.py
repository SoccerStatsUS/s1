# This file is for processing games from mongodb and formatting them for a model.
import datetime

from soccer.games.models import Game
from soccer.teams.models import Team

import pymongo

class ConsistencyException(Exception):
    pass


def check_team_names(d):
    Team.objects.get_team_test(d['home_team'])
    Team.objects.get_team_test(d['away_team'])

def check_game(d):
    """
    Make sure that the data you are trying to insert is consistent with other data.
    """

    # This should probably be the only way that a game gets inserted.
    # Need a pre-save hook for games?
    d['date']
    g = Game.objects.filter(date=d['date'], 
                            home_team=d['home_team'], 
                            away_team=d['away_team']
                            )


    # Game already exists. Need to check that things match
    if g:
        gx = g[0]

        if gx.location != '' and d.get('location') != gx.location:
            raise ConsistencyException

        if gx.competition != '' and d.get('competition') != gx.competition:
            raise ConsistencyException

        if gx.notes != '' and d.get('notes') != gx.notes:
            raise ConsistencyException
            

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
    f = lambda d: datetime.datetime.strptime(d['date'].strip(), '%A, %B %d, %Y')
    return process_game(d, f)


def process_nasl_game(d):
    f = lambda d: datetime.datetime.strptime(d['date'].strip(), '%A, %B %d, %Y')
    month, day = re.search("(?P<date>\d{1,2}/\d{2})", date).groups()[0].split("/")
    dt = datetime.datetime(2011, int(month), int(day))

    return process_game(d, f)


def process_game(d, process_date_func):
    """
    Convert to the right types, parse text if necessary.
    """

    # We are not sure what the competition of any of these games is.
    home_team = Team.objects.get_team(d['home_team'])
    away_team = Team.objects.get_team(d['away_team'])
    dt = process_date_func(d)

    try:
        home_score = int(d['home_score'])
        away_score = int(d['away_score'])

    # Some score is bad.
    except ValueError:
        print d
        return {}

    return {
        'date': dt,
        'home_team': home_team,
        'home_score': home_score,
        'away_team': away_team,
        'away_score': away_score,
        'location': d['location'],
        'competition': d.get('competition', ''),
        'notes': d.get('notes', ''),
        }

def get_rows(collection):
    return [row for row in collection.find().sort('date', pymongo.ASCENDING)]


def load_rows(rows):

    for e in rows:
        check_team_names(e)

    # Get the necessary objects and coerce them to correct types.
    processed_rows = [process_game(e) for e in rows]
    processed_rows = [e for e in processed_rows if e]

    # make sure there is no conflicting data.
    for e in processed_rows:
        check_game(e)

    # insert games carefully.
    for e in processed_rows:
        insert_game(e)



def load_mlssoccer():
    """
    Load the mlssoccer scores.
    """
    connection = pymongo.Connection()
    soccer_db = connection.soccer

    # Make sure teams are working.
    rows = get_rows(soccer_db.mlssoccer_mls_games)
    load_rows(rows)

def load_nasl():
    """
    Load the mlssoccer scores.
    """
    connection = pymongo.Connection()
    soccer_db = connection.soccer

    # Make sure teams are working.
    rows = get_rows(soccer_db.mlssoccer_mls_games)
    load_rows(rows)

