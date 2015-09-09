# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lawsuit'
        db.create_table(u'lawsuits_lawsuit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'lawsuits', ['Lawsuit'])


    def backwards(self, orm):
        # Deleting model 'Lawsuit'
        db.delete_table(u'lawsuits_lawsuit')


    models = {
        u'lawsuits.lawsuit': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Lawsuit'},
            'data': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['lawsuits']