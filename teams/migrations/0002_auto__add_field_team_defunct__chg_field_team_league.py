# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Team.defunct'
        db.add_column('teams_team', 'defunct', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Renaming column for 'Team.league' to match new field type.
        db.rename_column('teams_team', 'league', 'league_id')
        # Changing field 'Team.league'
        db.alter_column('teams_team', 'league_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['leagues.League']))

        # Adding index on 'Team', fields ['league']
        db.create_index('teams_team', ['league_id'])


    def backwards(self, orm):
        
        # Removing index on 'Team', fields ['league']
        db.delete_index('teams_team', ['league_id'])

        # Deleting field 'Team.defunct'
        db.delete_column('teams_team', 'defunct')

        # Renaming column for 'Team.league' to match new field type.
        db.rename_column('teams_team', 'league_id', 'league')
        # Changing field 'Team.league'
        db.alter_column('teams_team', 'league', self.gf('django.db.models.fields.CharField')(max_length=100))


    models = {
        'international.confederation': {
            'Meta': {'ordering': "('short_name',)", 'object_name': 'Confederation'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'leagues.league': {
            'Meta': {'ordering': "('name',)", 'object_name': 'League'},
            'confederation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'leagues'", 'to': "orm['international.Confederation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'teams.stadium': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Stadium'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opened': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'teams.team': {
            'Meta': {'ordering': "('founded', 'short_name')", 'object_name': 'Team'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'defunct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'founded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leagues.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['teams']
