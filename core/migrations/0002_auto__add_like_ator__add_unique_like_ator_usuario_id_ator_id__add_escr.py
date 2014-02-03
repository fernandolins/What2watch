# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Like_Ator'
        db.create_table(u'core_like_ator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Usuario'])),
            ('ator_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Ator'])),
        ))
        db.send_create_signal(u'core', ['Like_Ator'])

        # Adding unique constraint on 'Like_Ator', fields ['usuario_id', 'ator_id']
        db.create_unique(u'core_like_ator', ['usuario_id_id', 'ator_id_id'])

        # Adding model 'Escritor'
        db.create_table(u'core_escritor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'core', ['Escritor'])

        # Adding model 'Like_Diretor'
        db.create_table(u'core_like_diretor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Usuario'])),
            ('diretor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Diretor'])),
        ))
        db.send_create_signal(u'core', ['Like_Diretor'])

        # Adding unique constraint on 'Like_Diretor', fields ['usuario_id', 'diretor_id']
        db.create_unique(u'core_like_diretor', ['usuario_id_id', 'diretor_id_id'])

        # Adding model 'Assistiu_Filme'
        db.create_table(u'core_assistiu_filme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filme_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Filme'])),
            ('usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Usuario'])),
        ))
        db.send_create_signal(u'core', ['Assistiu_Filme'])

        # Adding unique constraint on 'Assistiu_Filme', fields ['filme_id', 'usuario_id']
        db.create_unique(u'core_assistiu_filme', ['filme_id_id', 'usuario_id_id'])

        # Adding model 'Filme'
        db.create_table(u'core_filme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('sinopse', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('link_foto', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1000)),
            ('imdb_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'core', ['Filme'])

        # Adding model 'Ator'
        db.create_table(u'core_ator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'core', ['Ator'])

        # Adding model 'Dirigiu_Filme'
        db.create_table(u'core_dirigiu_filme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filme_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Filme'])),
            ('diretor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Diretor'])),
        ))
        db.send_create_signal(u'core', ['Dirigiu_Filme'])

        # Adding unique constraint on 'Dirigiu_Filme', fields ['filme_id', 'diretor_id']
        db.create_unique(u'core_dirigiu_filme', ['filme_id_id', 'diretor_id_id'])

        # Adding model 'Like_Escritor'
        db.create_table(u'core_like_escritor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Usuario'])),
            ('escritor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Escritor'])),
        ))
        db.send_create_signal(u'core', ['Like_Escritor'])

        # Adding unique constraint on 'Like_Escritor', fields ['usuario_id', 'escritor_id']
        db.create_unique(u'core_like_escritor', ['usuario_id_id', 'escritor_id_id'])

        # Adding model 'Escreveu_Filme'
        db.create_table(u'core_escreveu_filme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filme_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Filme'])),
            ('escritor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Escritor'])),
        ))
        db.send_create_signal(u'core', ['Escreveu_Filme'])

        # Adding unique constraint on 'Escreveu_Filme', fields ['filme_id', 'escritor_id']
        db.create_unique(u'core_escreveu_filme', ['filme_id_id', 'escritor_id_id'])

        # Adding model 'Atuou_Filme'
        db.create_table(u'core_atuou_filme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filme_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Filme'])),
            ('ator_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Ator'])),
        ))
        db.send_create_signal(u'core', ['Atuou_Filme'])

        # Adding unique constraint on 'Atuou_Filme', fields ['filme_id', 'ator_id']
        db.create_unique(u'core_atuou_filme', ['filme_id_id', 'ator_id_id'])

        # Adding model 'Diretor'
        db.create_table(u'core_diretor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'core', ['Diretor'])


    def backwards(self, orm):
        # Removing unique constraint on 'Atuou_Filme', fields ['filme_id', 'ator_id']
        db.delete_unique(u'core_atuou_filme', ['filme_id_id', 'ator_id_id'])

        # Removing unique constraint on 'Escreveu_Filme', fields ['filme_id', 'escritor_id']
        db.delete_unique(u'core_escreveu_filme', ['filme_id_id', 'escritor_id_id'])

        # Removing unique constraint on 'Like_Escritor', fields ['usuario_id', 'escritor_id']
        db.delete_unique(u'core_like_escritor', ['usuario_id_id', 'escritor_id_id'])

        # Removing unique constraint on 'Dirigiu_Filme', fields ['filme_id', 'diretor_id']
        db.delete_unique(u'core_dirigiu_filme', ['filme_id_id', 'diretor_id_id'])

        # Removing unique constraint on 'Assistiu_Filme', fields ['filme_id', 'usuario_id']
        db.delete_unique(u'core_assistiu_filme', ['filme_id_id', 'usuario_id_id'])

        # Removing unique constraint on 'Like_Diretor', fields ['usuario_id', 'diretor_id']
        db.delete_unique(u'core_like_diretor', ['usuario_id_id', 'diretor_id_id'])

        # Removing unique constraint on 'Like_Ator', fields ['usuario_id', 'ator_id']
        db.delete_unique(u'core_like_ator', ['usuario_id_id', 'ator_id_id'])

        # Deleting model 'Like_Ator'
        db.delete_table(u'core_like_ator')

        # Deleting model 'Escritor'
        db.delete_table(u'core_escritor')

        # Deleting model 'Like_Diretor'
        db.delete_table(u'core_like_diretor')

        # Deleting model 'Assistiu_Filme'
        db.delete_table(u'core_assistiu_filme')

        # Deleting model 'Filme'
        db.delete_table(u'core_filme')

        # Deleting model 'Ator'
        db.delete_table(u'core_ator')

        # Deleting model 'Dirigiu_Filme'
        db.delete_table(u'core_dirigiu_filme')

        # Deleting model 'Like_Escritor'
        db.delete_table(u'core_like_escritor')

        # Deleting model 'Escreveu_Filme'
        db.delete_table(u'core_escreveu_filme')

        # Deleting model 'Atuou_Filme'
        db.delete_table(u'core_atuou_filme')

        # Deleting model 'Diretor'
        db.delete_table(u'core_diretor')


    models = {
        u'core.assistiu_filme': {
            'Meta': {'unique_together': "(('filme_id', 'usuario_id'),)", 'object_name': 'Assistiu_Filme'},
            'filme_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Filme']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Usuario']"})
        },
        u'core.ator': {
            'Meta': {'object_name': 'Ator'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'usuarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Usuario']", 'through': u"orm['core.Like_Ator']", 'symmetrical': 'False'})
        },
        u'core.atuou_filme': {
            'Meta': {'unique_together': "(('filme_id', 'ator_id'),)", 'object_name': 'Atuou_Filme'},
            'ator_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Ator']"}),
            'filme_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Filme']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.diretor': {
            'Meta': {'object_name': 'Diretor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'usuarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Usuario']", 'through': u"orm['core.Like_Diretor']", 'symmetrical': 'False'})
        },
        u'core.dirigiu_filme': {
            'Meta': {'unique_together': "(('filme_id', 'diretor_id'),)", 'object_name': 'Dirigiu_Filme'},
            'diretor_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Diretor']"}),
            'filme_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Filme']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.escreveu_filme': {
            'Meta': {'unique_together': "(('filme_id', 'escritor_id'),)", 'object_name': 'Escreveu_Filme'},
            'escritor_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Escritor']"}),
            'filme_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Filme']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.escritor': {
            'Meta': {'object_name': 'Escritor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'usuarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Usuario']", 'through': u"orm['core.Like_Escritor']", 'symmetrical': 'False'})
        },
        u'core.filme': {
            'Meta': {'object_name': 'Filme'},
            'atores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Ator']", 'through': u"orm['core.Atuou_Filme']", 'symmetrical': 'False'}),
            'diretores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Diretor']", 'through': u"orm['core.Dirigiu_Filme']", 'symmetrical': 'False'}),
            'escritores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Escritor']", 'through': u"orm['core.Escreveu_Filme']", 'symmetrical': 'False'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1000'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'link_foto': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'sinopse': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'usuarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Usuario']", 'through': u"orm['core.Assistiu_Filme']", 'symmetrical': 'False'})
        },
        u'core.like_ator': {
            'Meta': {'unique_together': "(('usuario_id', 'ator_id'),)", 'object_name': 'Like_Ator'},
            'ator_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Ator']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Usuario']"})
        },
        u'core.like_diretor': {
            'Meta': {'unique_together': "(('usuario_id', 'diretor_id'),)", 'object_name': 'Like_Diretor'},
            'diretor_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Diretor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Usuario']"})
        },
        u'core.like_escritor': {
            'Meta': {'unique_together': "(('usuario_id', 'escritor_id'),)", 'object_name': 'Like_Escritor'},
            'escritor_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Escritor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Usuario']"})
        },
        u'core.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'facebook_nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']