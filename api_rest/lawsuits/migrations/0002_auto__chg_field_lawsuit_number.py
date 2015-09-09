# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Lawsuit.number'
        db.alter_column(u'lawsuits_lawsuit', 'number', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):

        # Changing field 'Lawsuit.number'
        db.alter_column(u'lawsuits_lawsuit', 'number', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'lawsuits.lawsuit': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Lawsuit'},
            'data': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['lawsuits']