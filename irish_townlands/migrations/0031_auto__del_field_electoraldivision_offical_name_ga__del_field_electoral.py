# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ElectoralDivision.offical_name_ga'
        db.delete_column(u'irish_townlands_electoraldivision', 'offical_name_ga')

        # Deleting field 'ElectoralDivision.offical_name_en'
        db.delete_column(u'irish_townlands_electoraldivision', 'offical_name_en')

        # Adding field 'ElectoralDivision.official_name_en'
        db.add_column(u'irish_townlands_electoraldivision', 'official_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'ElectoralDivision.official_name_ga'
        db.add_column(u'irish_townlands_electoraldivision', 'official_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'Townland.offical_name_ga'
        db.delete_column(u'irish_townlands_townland', 'offical_name_ga')

        # Deleting field 'Townland.offical_name_en'
        db.delete_column(u'irish_townlands_townland', 'offical_name_en')

        # Adding field 'Townland.official_name_en'
        db.add_column(u'irish_townlands_townland', 'official_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Townland.official_name_ga'
        db.add_column(u'irish_townlands_townland', 'official_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'CivilParish.offical_name_ga'
        db.delete_column(u'irish_townlands_civilparish', 'offical_name_ga')

        # Deleting field 'CivilParish.offical_name_en'
        db.delete_column(u'irish_townlands_civilparish', 'offical_name_en')

        # Adding field 'CivilParish.official_name_en'
        db.add_column(u'irish_townlands_civilparish', 'official_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'CivilParish.official_name_ga'
        db.add_column(u'irish_townlands_civilparish', 'official_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'Barony.offical_name_ga'
        db.delete_column(u'irish_townlands_barony', 'offical_name_ga')

        # Deleting field 'Barony.offical_name_en'
        db.delete_column(u'irish_townlands_barony', 'offical_name_en')

        # Adding field 'Barony.official_name_en'
        db.add_column(u'irish_townlands_barony', 'official_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Barony.official_name_ga'
        db.add_column(u'irish_townlands_barony', 'official_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'County.offical_name_ga'
        db.delete_column(u'irish_townlands_county', 'offical_name_ga')

        # Deleting field 'County.offical_name_en'
        db.delete_column(u'irish_townlands_county', 'offical_name_en')

        # Adding field 'County.official_name_en'
        db.add_column(u'irish_townlands_county', 'official_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'County.official_name_ga'
        db.add_column(u'irish_townlands_county', 'official_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ElectoralDivision.offical_name_ga'
        db.add_column(u'irish_townlands_electoraldivision', 'offical_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'ElectoralDivision.offical_name_en'
        db.add_column(u'irish_townlands_electoraldivision', 'offical_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'ElectoralDivision.official_name_en'
        db.delete_column(u'irish_townlands_electoraldivision', 'official_name_en')

        # Deleting field 'ElectoralDivision.official_name_ga'
        db.delete_column(u'irish_townlands_electoraldivision', 'official_name_ga')

        # Adding field 'Townland.offical_name_ga'
        db.add_column(u'irish_townlands_townland', 'offical_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Townland.offical_name_en'
        db.add_column(u'irish_townlands_townland', 'offical_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'Townland.official_name_en'
        db.delete_column(u'irish_townlands_townland', 'official_name_en')

        # Deleting field 'Townland.official_name_ga'
        db.delete_column(u'irish_townlands_townland', 'official_name_ga')

        # Adding field 'CivilParish.offical_name_ga'
        db.add_column(u'irish_townlands_civilparish', 'offical_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'CivilParish.offical_name_en'
        db.add_column(u'irish_townlands_civilparish', 'offical_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'CivilParish.official_name_en'
        db.delete_column(u'irish_townlands_civilparish', 'official_name_en')

        # Deleting field 'CivilParish.official_name_ga'
        db.delete_column(u'irish_townlands_civilparish', 'official_name_ga')

        # Adding field 'Barony.offical_name_ga'
        db.add_column(u'irish_townlands_barony', 'offical_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Barony.offical_name_en'
        db.add_column(u'irish_townlands_barony', 'offical_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'Barony.official_name_en'
        db.delete_column(u'irish_townlands_barony', 'official_name_en')

        # Deleting field 'Barony.official_name_ga'
        db.delete_column(u'irish_townlands_barony', 'official_name_ga')

        # Adding field 'County.offical_name_ga'
        db.add_column(u'irish_townlands_county', 'offical_name_ga',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'County.offical_name_en'
        db.add_column(u'irish_townlands_county', 'offical_name_en',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, db_index=True),
                      keep_default=False)

        # Deleting field 'County.official_name_en'
        db.delete_column(u'irish_townlands_county', 'official_name_en')

        # Deleting field 'County.official_name_ga'
        db.delete_column(u'irish_townlands_county', 'official_name_ga')


    models = {
        u'irish_townlands.barony': {
            'Meta': {'object_name': 'Barony'},
            '_polygon_geojson': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['irish_townlands.Polygon']", 'null': 'True'}),
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'attribution': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'baronies'", 'null': 'True', 'to': u"orm['irish_townlands.County']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logainm_ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_census1901_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_census1911_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'water_area_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'irish_townlands.civilparish': {
            'Meta': {'object_name': 'CivilParish'},
            '_polygon_geojson': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['irish_townlands.Polygon']", 'null': 'True'}),
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'attribution': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'counties': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'civil_parishes'", 'default': 'None', 'to': u"orm['irish_townlands.County']", 'symmetrical': 'False', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logainm_ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_census1901_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_census1911_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'water_area_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'irish_townlands.county': {
            'Meta': {'object_name': 'County'},
            '_polygon_geojson': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['irish_townlands.Polygon']", 'null': 'True'}),
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'attribution': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logainm_ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_census1901_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_census1911_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'polygon_barony_gaps': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'polygon_barony_overlaps': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'polygon_civil_parish_gaps': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'polygon_civil_parish_overlaps': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'polygon_ed_gaps': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'polygon_ed_overlaps': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'polygon_townland_gaps': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'polygon_townland_overlaps': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'water_area_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'irish_townlands.electoraldivision': {
            'Meta': {'object_name': 'ElectoralDivision'},
            '_polygon_geojson': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['irish_townlands.Polygon']", 'null': 'True'}),
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'attribution': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'eds'", 'null': 'True', 'to': u"orm['irish_townlands.County']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logainm_ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_census1901_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_census1911_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
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
        u'irish_townlands.polygon': {
            'Meta': {'object_name': 'Polygon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {}),
            'polygon_geojson': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'irish_townlands.progress': {
            'Meta': {'object_name': 'Progress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'percent': ('django.db.models.fields.FloatField', [], {}),
            'when': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'irish_townlands.subtownland': {
            'Meta': {'object_name': 'Subtownland'},
            'alt_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'logainm_ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_census1901_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_census1911_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'townland': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subtownlands'", 'to': u"orm['irish_townlands.Townland']"}),
            'unique_suffix': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'irish_townlands.townland': {
            'Meta': {'object_name': 'Townland'},
            '_polygon_geojson': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['irish_townlands.Polygon']", 'null': 'True'}),
            'alt_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'alt_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'area_m2': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'attribution': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'barony': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'townlands'", 'null': 'True', 'to': u"orm['irish_townlands.Barony']"}),
            'bbox_height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bbox_width': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centre_y': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'civil_parish': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'townlands'", 'null': 'True', 'to': u"orm['irish_townlands.CivilParish']"}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'townlands'", 'null': 'True', 'to': u"orm['irish_townlands.County']"}),
            'ed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'townlands'", 'null': 'True', 'to': u"orm['irish_townlands.ElectoralDivision']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logainm_ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_census1901_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_census1911_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'official_name_ga': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'osm_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'osm_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'osm_uid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'osm_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
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