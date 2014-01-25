# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'core_usuario', (
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('facebook_nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Usuario'])


    def backwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table(u'core_usuario')


    models = {
        u'core.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'facebook_nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']