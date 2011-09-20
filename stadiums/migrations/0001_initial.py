# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Stadium'
        db.create_table('stadiums_stadium', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('opened', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal('stadiums', ['Stadium'])


    def backwards(self, orm):
        
        # Deleting model 'Stadium'
        db.delete_table('stadiums_stadium')


    models = {
        'stadiums.stadium': {
            'Meta': {'object_name': 'Stadium'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opened': ('django.db.models.fields.DateField', [], {'null': 'True'})
        }
    }

    complete_apps = ['stadiums']
