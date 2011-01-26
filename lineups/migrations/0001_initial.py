# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Game'
        db.create_table('lineups_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('neutral', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('home_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_games', to=orm['teams.Team'])),
            ('home_score', self.gf('django.db.models.fields.IntegerField')()),
            ('away_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='away_games', to=orm['teams.Team'])),
            ('away_score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('lineups', ['Game'])

        # Adding model 'GameGoal'
        db.create_table('lineups_gamegoal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lineups.Game'])),
            ('scorer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('assist_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('assist_2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('minute', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('lineups', ['GameGoal'])

        # Adding model 'GamePlayed'
        db.create_table('lineups_gameplayed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lineups.Game'])),
            ('player', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('on', self.gf('django.db.models.fields.IntegerField')()),
            ('off', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('lineups', ['GamePlayed'])

        # Adding model 'GoalRecord'
        db.create_table('lineups_goalrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lineups.Game'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Team'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('lineups', ['GoalRecord'])

        # Adding model 'GameAppearance'
        db.create_table('lineups_gameappearance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lineups.Game'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['players.Person'])),
            ('on', self.gf('django.db.models.fields.IntegerField')()),
            ('off', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('lineups', ['GameAppearance'])


    def backwards(self, orm):
        
        # Deleting model 'Game'
        db.delete_table('lineups_game')

        # Deleting model 'GameGoal'
        db.delete_table('lineups_gamegoal')

        # Deleting model 'GamePlayed'
        db.delete_table('lineups_gameplayed')

        # Deleting model 'GoalRecord'
        db.delete_table('lineups_goalrecord')

        # Deleting model 'GameAppearance'
        db.delete_table('lineups_gameappearance')


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
            'Meta': {'ordering': "('date',)", 'object_name': 'Game'},
            'away_score': ('django.db.models.fields.IntegerField', [], {}),
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_games'", 'to': "orm['teams.Team']"}),
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
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['players.Person']"})
        },
        'lineups.gamegoal': {
            'Meta': {'object_name': 'GameGoal'},
            'assist_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'assist_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lineups.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {}),
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
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lineups.Game']"}),
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

    complete_apps = ['lineups']
