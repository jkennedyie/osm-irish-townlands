# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CivilParish.place'
        db.add_column(u'irish_townlands_civilparish', 'place',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Townland.place'
        db.add_column(u'irish_townlands_townland', 'place',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Barony.place'
        db.add_column(u'irish_townlands_barony', 'place',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True),
                      keep_default=False)

        # Adding field 'County.place'
        db.add_column(u'irish_townlands_county', 'place',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True),
                      keep_default=False)

        # Adding field 'ElectoralDivision.place'
        db.add_column(u'irish_townlands_electoraldivision', 'place',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CivilParish.place'
        db.delete_column(u'irish_townlands_civilparish', 'place')

        # Deleting field 'Townland.place'
        db.delete_column(u'irish_townlands_townland', 'place')

        # Deleting field 'Barony.place'
        db.delete_column(u'irish_townlands_barony', 'place')

        # Deleting field 'County.place'
        db.delete_column(u'irish_townlands_county', 'place')

        # Deleting field 'ElectoralDivision.place'
        db.delete_column(u'irish_townlands_electoraldivision', 'place')


    models = {
        u'irish_townlands.barony': {
            'Meta': {'object_name': 'Barony'},
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'baronies'", 'null': 'True', 'to': u"orm['irish_townlands.County']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'polygon_geojson': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'water_area_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'irish_townlands.civilparish': {
            'Meta': {'object_name': 'CivilParish'},
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'civil_parishes'", 'null': 'True', 'to': u"orm['irish_townlands.County']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'polygon_geojson': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'water_area_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'irish_townlands.county': {
            'Meta': {'object_name': 'County'},
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'polygon_barony_gaps': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'polygon_barony_overlaps': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'polygon_civil_parish_gaps': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'polygon_civil_parish_overlaps': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'polygon_geojson': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'polygon_townland_gaps': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'polygon_townland_overlaps': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'water_area_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'irish_townlands.electoraldivision': {
            'Meta': {'object_name': 'ElectoralDivision'},
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'eds'", 'null': 'True', 'to': u"orm['irish_townlands.County']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'polygon_geojson': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'water_area_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'irish_townlands.error': {
            'Meta': {'object_name': 'Error'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        },
        u'irish_townlands.metadata': {
            'Meta': {'object_name': 'Metadata'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'irish_townlands.progress': {
            'Meta': {'object_name': 'Progress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'percent': ('django.db.models.fields.FloatField', [], {}),
            'when': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'irish_townlands.townland': {
            'Meta': {'object_name': 'Townland'},
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'barony': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'townlands'", 'null': 'True', 'to': u"orm['irish_townlands.Barony']"}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'civil_parish': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'townlands'", 'null': 'True', 'to': u"orm['irish_townlands.CivilParish']"}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'townlands'", 'null': 'True', 'to': u"orm['irish_townlands.County']"}),
            'ed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'townlands'", 'null': 'True', 'to': u"orm['irish_townlands.ElectoralDivision']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'polygon_geojson': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'water_area_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'irish_townlands.townlandtouch': {
            'Meta': {'unique_together': "[('townland_a', 'townland_b')]", 'object_name': 'TownlandTouch'},
            'direction_radians': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_m': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'townland_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'touching_as_a'", 'to': u"orm['irish_townlands.Townland']"}),
            'townland_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'touching_as_b'", 'to': u"orm['irish_townlands.Townland']"})
        }
    }

    complete_apps = ['irish_townlands']