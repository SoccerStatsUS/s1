# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Game'
        db.create_table('games_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('home_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_games2', to=orm['teams.Team'])),
            ('home_score', self.gf('django.db.models.fields.IntegerField')()),
            ('away_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='away_games2', to=orm['teams.Team'])),
            ('away_score', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('competition', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('games', ['Game'])

        # Adding unique constraint on 'Game', fields ['home_team', 'date']
        db.create_unique('games_game', ['home_team_id', 'date'])

        # Adding unique constraint on 'Game', fields ['away_team', 'date']
        db.create_unique('games_game', ['away_team_id', 'date'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Game', fields ['away_team', 'date']
        db.delete_unique('games_game', ['away_team_id', 'date'])

        # Removing unique constraint on 'Game', fields ['home_team', 'date']
        db.delete_unique('games_game', ['home_team_id', 'date'])

        # Deleting model 'Game'
        db.delete_table('games_game')


    models = {
        'games.game': {
            'Meta': {'ordering': "('date',)", 'unique_together': "[('home_team', 'date'), ('away_team', 'date')]", 'object_name': 'Game'},
            'away_score': ('django.db.models.fields.IntegerField', [], {}),
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_games2'", 'to': "orm['teams.Team']"}),
            'competition': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'home_score': ('django.db.models.fields.IntegerField', [], {}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_games2'", 'to': "orm['teams.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        'international.confederation': {
            'Meta': {'ordering': "('short_name',)", 'object_name': 'Confederation'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'leagues.league': {
            'Meta': {'ordering': "('name',)", 'object_name': 'League'},
            'confederation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'leagues'", 'to': "orm['international.Confederation']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'places.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {})
        },
        'teams.team': {
            'Meta': {'ordering': "('short_name',)", 'object_name': 'Team'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'defunct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'founded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leagues.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'real': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['games']
