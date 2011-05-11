import os
import sys

from django.core.management.base import BaseCommand, CommandError
from django import settings

remote_path = "/home/chris/www/soccer/soccer.db"

class Command(BaseCommand):
    
    args = ''
    help = "Downloads the production database."
    
    def handle(self, *args, **options):
        if not sys.argv[2:]:
            db = settings.DATABASES['default']['NAME']
            command = "scp reyna:%s %s" % (remote_path, db)
        else:
            command = "scp reyna:%s %s" % (remote_path, sys.argv[2])
        os.system(command)

        
