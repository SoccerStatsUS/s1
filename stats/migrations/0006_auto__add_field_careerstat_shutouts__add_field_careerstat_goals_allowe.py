# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CareerStat.shutouts'
        db.add_column('stats_careerstat', 'shutouts', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'CareerStat.goals_allowed'
        db.add_column('stats_careerstat', 'goals_allowed', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'CareerStat.shots_faced'
        db.add_column('stats_careerstat', 'shots_faced', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'CareerStat.saves'
        db.add_column('stats_careerstat', 'saves', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'CareerStat.penalties_allowed'
        db.add_column('stats_careerstat', 'penalties_allowed', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'CareerStat.penalties_faced'
        db.add_column('stats_careerstat', 'penalties_faced', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CareerStat.shutouts'
        db.delete_column('stats_careerstat', 'shutouts')

        # Deleting field 'CareerStat.goals_allowed'
        db.delete_column('stats_careerstat', 'goals_allowed')

        # Deleting field 'CareerStat.shots_faced'
        db.delete_column('stats_careerstat', 'shots_faced')

        # Deleting field 'CareerStat.saves'
        db.delete_column('stats_careerstat', 'saves')

        # Deleting field 'CareerStat.penalties_allowed'
        db.delete_column('stats_careerstat', 'penalties_allowed')

        # Deleting field 'CareerStat.penalties_faced'
        db.delete_column('stats_careerstat', 'penalties_faced')


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
        'stats.careerstat': {
            'Meta': {'object_name': 'CareerStat'},
            'assists': ('django.db.models.fields.IntegerField', [], {}),
            'fouls_committed': ('django.db.models.fields.IntegerField', [], {}),
            'fouls_suffered': ('django.db.models.fields.IntegerField', [], {}),
            'game_winning_goals': ('django.db.models.fields.IntegerField', [], {}),
            'games_played': ('django.db.models.fields.IntegerField', [], {}),
            'games_started': ('django.db.models.fields.IntegerField', [], {}),
            'goals': ('django.db.models.fields.IntegerField', [], {}),
            'goals_allowed': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'offsides': ('django.db.models.fields.IntegerField', [], {}),
            'penalties_allowed': ('django.db.models.fields.IntegerField', [], {}),
            'penalties_faced': ('django.db.models.fields.IntegerField', [], {}),
            'penalty_attempts': ('django.db.models.fields.IntegerField', [], {}),
            'penalty_goals': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['players.Person']"}),
            'red_cards': ('django.db.models.fields.IntegerField', [], {}),
            'saves': ('django.db.models.fields.IntegerField', [], {}),
            'shots': ('django.db.models.fields.IntegerField', [], {}),
            'shots_faced': ('django.db.models.fields.IntegerField', [], {}),
            'shots_on_goal': ('django.db.models.fields.IntegerField', [], {}),
            'shutouts': ('django.db.models.fields.IntegerField', [], {}),
            'yellow_cards': ('django.db.models.fields.IntegerField', [], {})
        },
        'stats.gamestat': {
            'Meta': {'object_name': 'GameStat'},
            'assists': ('django.db.models.fields.IntegerField', [], {}),
            'corner_kicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'crosses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fouls_committed': ('django.db.models.fields.IntegerField', [], {}),
            'fouls_suffered': ('django.db.models.fields.IntegerField', [], {}),
            'goals': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'offsides': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['players.Person']"}),
            'red_cards': ('django.db.models.fields.IntegerField', [], {}),
            'saves': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'shots': ('django.db.models.fields.IntegerField', [], {}),
            'shots_on_goal': ('django.db.models.fields.IntegerField', [], {}),
            'yellow_cards': ('django.db.models.fields.IntegerField', [], {})
        },
        'stats.seasonstat': {
            'Meta': {'ordering': "('player', 'year')", 'object_name': 'SeasonStat'},
            'assists': ('django.db.models.fields.IntegerField', [], {}),
            'fouls_committed': ('django.db.models.fields.IntegerField', [], {}),
            'fouls_suffered': ('django.db.models.fields.IntegerField', [], {}),
            'game_winning_goals': ('django.db.models.fields.IntegerField', [], {}),
            'games_played': ('django.db.models.fields.IntegerField', [], {}),
            'games_started': ('django.db.models.fields.IntegerField', [], {}),
            'goals': ('django.db.models.fields.IntegerField', [], {}),
            'goals_allowed': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'offsides': ('django.db.models.fields.IntegerField', [], {}),
            'penalties_allowed': ('django.db.models.fields.IntegerField', [], {}),
            'penalties_faced': ('django.db.models.fields.IntegerField', [], {}),
            'penalty_attempts': ('django.db.models.fields.IntegerField', [], {}),
            'penalty_goals': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['players.Person']"}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '7'}),
            'red_cards': ('django.db.models.fields.IntegerField', [], {}),
            'saves': ('django.db.models.fields.IntegerField', [], {}),
            'shots': ('django.db.models.fields.IntegerField', [], {}),
            'shots_faced': ('django.db.models.fields.IntegerField', [], {}),
            'shots_on_goal': ('django.db.models.fields.IntegerField', [], {}),
            'shutouts': ('django.db.models.fields.IntegerField', [], {}),
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
