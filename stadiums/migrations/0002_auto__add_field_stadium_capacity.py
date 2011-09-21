# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Stadium.capacity'
        db.add_column('stadiums_stadium', 'capacity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Stadium.capacity'
        db.delete_column('stadiums_stadium', 'capacity')


    models = {
        'stadiums.stadium': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Stadium'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opened': ('django.db.models.fields.DateField', [], {'null': 'True'})
        }
    }

    complete_apps = ['stadiums']
