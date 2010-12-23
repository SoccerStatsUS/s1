# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'SoccernetBio'
        db.delete_table('players_soccernetbio')


    def backwards(self, orm):
        
        # Adding model 'SoccernetBio'
        db.create_table('players_soccernetbio', (
            ('birthplace', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Country'], null=True)),
            ('soccernet_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('players', ['SoccernetBio'])


    models = {
        'places.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {})
        },
        'players.genericbio': {
            'Meta': {'ordering': "('-birthdate',)", 'object_name': 'GenericBio'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.Country']", 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'source_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'players.person': {
            'Meta': {'ordering': "('last_name',)", 'object_name': 'Person'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'mls_slug': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.Country']"}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['players']
