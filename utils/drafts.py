from soccer.drafts.models import Draft, Pick
from soccer.players.models import Person
from soccer.teams.models import Team

from soccer.utils.players import scrape_person


def remove_pairs(text, start, end):
    s = ""
    include = True
    for char in text:
        if char == start:
            include = False

        if include:
            s += char
        
        if char == end:
            include = True

    return s



def process_draft(draft, text, commit=False):
    text = text.replace("*", "")
    text = remove_pairs(text, "(", ")")
    text = remove_pairs(text, "[", "]")
    lines = [e for e in text.split("\n") if e]
    items = [e.split('\t') for e in lines]

    t = Team.objects.all()[0]

    for number, name, team in items:
        number = int(number)
        name = name.strip()
        team = team.strip()

        if commit:
            t = Team.objects.get_team(team)
        else:
            try:
                t = Team.objects.get_team(team)
            except:
                print "BROKEN TEAM: %s" % team

        pick = Pick(number=number, team=t, name=name, draft=draft)
        try:
            player = Person.objects.get(name=name)
            pick.player = player
        except:
            if commit:
                pass
            else:
                print name

        if commit:
            pick.save()
    
    
