# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Draft.draft_type'
        db.add_column('drafts_draft', 'draft_type', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Changing field 'Draft.name'
        db.alter_column('drafts_draft', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255))


    def backwards(self, orm):
        
        # Deleting field 'Draft.draft_type'
        db.delete_column('drafts_draft', 'draft_type')

        # Changing field 'Draft.name'
        db.alter_column('drafts_draft', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50))


    models = {
        'drafts.draft': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Draft'},
            'draft_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'drafts.pick': {
            'Meta': {'ordering': "('-draft', 'number')", 'object_name': 'Pick'},
            'draft': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['drafts.Draft']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'250'"}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['players.Person']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"})
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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
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

    complete_apps = ['drafts']
