from piston.handler import BaseHandler
from soccer.players.models import Person

class PersonHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = Person

   def read(self, request):
       return Person.objects.all()[:10]

