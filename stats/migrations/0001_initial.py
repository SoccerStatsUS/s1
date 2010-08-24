# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SeasonStat'
        db.create_table('stats_seasonstat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['players.Person'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Team'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('games_played', self.gf('django.db.models.fields.IntegerField')()),
            ('games_started', self.gf('django.db.models.fields.IntegerField')()),
            ('minutes', self.gf('django.db.models.fields.IntegerField')()),
            ('goals', self.gf('django.db.models.fields.IntegerField')()),
            ('game_winning_goals', self.gf('django.db.models.fields.IntegerField')()),
            ('assists', self.gf('django.db.models.fields.IntegerField')()),
            ('shots', self.gf('django.db.models.fields.IntegerField')()),
            ('shots_on_goal', self.gf('django.db.models.fields.IntegerField')()),
            ('offsides', self.gf('django.db.models.fields.IntegerField')()),
            ('penalty_goals', self.gf('django.db.models.fields.IntegerField')()),
            ('penalty_attempts', self.gf('django.db.models.fields.IntegerField')()),
            ('fouls_committed', self.gf('django.db.models.fields.IntegerField')()),
            ('fouls_suffered', self.gf('django.db.models.fields.IntegerField')()),
            ('yellow_cards', self.gf('django.db.models.fields.IntegerField')()),
            ('red_cards', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('stats', ['SeasonStat'])


    def backwards(self, orm):
        
        # Deleting model 'SeasonStat'
        db.delete_table('stats_seasonstat')


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
        'stats.seasonstat': {
            'Meta': {'object_name': 'SeasonStat'},
            'assists': ('django.db.models.fields.IntegerField', [], {}),
            'fouls_committed': ('django.db.models.fields.IntegerField', [], {}),
            'fouls_suffered': ('django.db.models.fields.IntegerField', [], {}),
            'game_winning_goals': ('django.db.models.fields.IntegerField', [], {}),
            'games_played': ('django.db.models.fields.IntegerField', [], {}),
            'games_started': ('django.db.models.fields.IntegerField', [], {}),
            'goals': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'offsides': ('django.db.models.fields.IntegerField', [], {}),
            'penalty_attempts': ('django.db.models.fields.IntegerField', [], {}),
            'penalty_goals': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['players.Person']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'red_cards': ('django.db.models.fields.IntegerField', [], {}),
            'shots': ('django.db.models.fields.IntegerField', [], {}),
            'shots_on_goal': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"}),
            'year': ('django.db.models.fields.IntegerField', [], {}),
            'yellow_cards': ('django.db.models.fields.IntegerField', [], {})
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

    complete_apps = ['stats']
