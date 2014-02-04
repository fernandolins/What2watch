# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Filme.link_foto'
        db.alter_column(u'core_filme', 'link_foto', self.gf('django.db.models.fields.CharField')(max_length=300))

    def backwards(self, orm):

        # Changing field 'Filme.link_foto'
        db.alter_column(u'core_filme', 'link_foto', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
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
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
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
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'usuarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Usuario']", 'through': u"orm['core.Like_Escritor']", 'symmetrical': 'False'})
        },
        u'core.filme': {
            'Meta': {'object_name': 'Filme'},
            'atores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Ator']", 'through': u"orm['core.Atuou_Filme']", 'symmetrical': 'False'}),
            'diretores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Diretor']", 'through': u"orm['core.Dirigiu_Filme']", 'symmetrical': 'False'}),
            'escritores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Escritor']", 'through': u"orm['core.Escreveu_Filme']", 'symmetrical': 'False'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1000'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'link_foto': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sinopse': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'usuarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Usuario']", 'through': u"orm['core.Assistiu_Filme']", 'symmetrical': 'False'})
        },
        u'core.filmesrecomendados': {
            'Meta': {'object_name': 'FilmesRecomendados'},
            'filme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Filme']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Usuario']"})
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
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'facebook_nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']