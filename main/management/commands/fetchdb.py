import os
import sys

from django.core.management.base import BaseCommand, CommandError
from django import settings

db_path = settings.DATABASES['default']['NAME']

class Command(BaseCommand):
    
    args = ''
    help = "Downloads the production database."
    
    def handle(self, *args, **options):

        if not sys.argv[2:]:
            command = "scp reyna:%s %s" % (db_path, db_path)
        else:
            command = "scp reyna:%s %s" % (db_path, sys.argv[2])
        os.system(command)

        
