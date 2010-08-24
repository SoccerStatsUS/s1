from soccer.players.models import Person


# Used for model defaults.
# Is this the best way?
no_player = lambda: Person.objects.get(name='No Player') 
