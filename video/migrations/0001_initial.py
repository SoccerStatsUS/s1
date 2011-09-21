# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Video'
        db.create_table('video_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1023)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('video', ['Video'])


    def backwards(self, orm):
        
        # Deleting model 'Video'
        db.delete_table('video_video')


    models = {
        'video.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1023'})
        }
    }

    complete_apps = ['video']
