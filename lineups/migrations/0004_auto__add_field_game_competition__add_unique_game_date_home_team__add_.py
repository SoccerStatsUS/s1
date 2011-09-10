# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Game.competition'
        db.add_column('lineups_game', 'competition', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding unique constraint on 'Game', fields ['date', 'home_team']
        db.create_unique('lineups_game', ['date', 'home_team_id'])

        # Adding unique constraint on 'Game', fields ['date', 'away_team']
        db.create_unique('lineups_game', ['date', 'away_team_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Game', fields ['date', 'away_team']
        db.delete_unique('lineups_game', ['date', 'away_team_id'])

        # Removing unique constraint on 'Game', fields ['date', 'home_team']
        db.delete_unique('lineups_game', ['date', 'home_team_id'])

        # Deleting field 'Game.competition'
        db.delete_column('lineups_game', 'competition')


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
        'lineups.game': {
            'Meta': {'ordering': "('date',)", 'unique_together': "[('home_team', 'date'), ('away_team', 'date')]", 'object_name': 'Game'},
            'away_score': ('django.db.models.fields.IntegerField', [], {}),
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_games'", 'to': "orm['teams.Team']"}),
            'competition': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'home_score': ('django.db.models.fields.IntegerField', [], {}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_games'", 'to': "orm['teams.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neutral': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'lineups.gameappearance': {
            'Meta': {'object_name': 'GameAppearance'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lineups.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'off': ('django.db.models.fields.IntegerField', [], {}),
            'on': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['players.Person']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"})
        },
        'lineups.gamegoal': {
            'Meta': {'object_name': 'GameGoal'},
            'assist_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'assist_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lineups.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {}),
            'penalty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scorer': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'lineups.gameplayed': {
            'Meta': {'object_name': 'GamePlayed'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lineups.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'off': ('django.db.models.fields.IntegerField', [], {}),
            'on': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'lineups.goalrecord': {
            'Meta': {'object_name': 'GoalRecord'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'goals'", 'to': "orm['lineups.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"})
        },
        'places.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {})
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
        },
        'teams.team': {
            'Meta': {'ordering': "('short_name',)", 'object_name': 'Team'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'defunct': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'founded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leagues.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['lineups']
