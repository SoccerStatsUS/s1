from soccer.drafts.models import Draft
from soccer.players.models import Player
from soccer.teams.models import Team


def process_draft(draft, text):
    text = text.replace("*", "")
    lines = [e.split("\t") for e in text.split('\n')]
    for pick, team, name in lines:
        p = int(pick)
        t = Team.objects.get(name=team)
        pick = Pick(number=p, team=t, name=name)
        try:
            player = Player.objects.get(name=name)
            pick.player = player
        except:
            print team
        #pick.save()
    
    
