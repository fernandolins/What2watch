# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Usuario(models.Model):
    facebook_id        = models.CharField(max_length=50, primary_key=True)
    facebook_nome      = models.CharField(max_length=50)
    access_token       = models.CharField(max_length=200)

    def get_or_create(self, face_id, face_nome, accessToken):
        try:
            facebook_usuario = Usuario.objects.get(facebook_id=face_id)
            print accessToken
            return facebook_usuario
        except Usuario.DoesNotExist:
            facebook_usuario = Usuario(facebook_id=face_id, facebook_nome=face_nome, access_token=accessToken)
            facebook_usuario.save()
            return facebook_usuario

    def __unicode__(self):
        return "Nome: " + unicode(self.facebook_nome)


# class Ator_Diretor(models.Model):
#     nome     = models.CharField(max_length=30, unique=True)
#     tipo     = models.CharField(max_length=20, null=True)
#     usuarios = models.ManyToManyField(Usuario, through="Like_Ator_Diretor")

#     def get_or_create(self, nome_, tipo_):
#         try:
#             ator_diretor = Ator_Diretor.objects.get(nome=nome_)
#             return ator_diretor
#         except Ator_Diretor.DoesNotExist:
#             ator_diretor = Ator_Diretor(nome=nome_, tipo=tipo_)
#             ator_diretor.save()
#             return ator_diretor

#     def __unicode__(self):
#         return "Nome: " + unicode(self.nome) + " - Tipo: " + unicode(self.tipo)


# class Escritor(models.Model):
#     nome     = models.CharField(max_length=30, unique=True)
#     usuarios = models.ManyToManyField(Usuario, through="Like_Escritor")
    
#     def get_or_create(self, nome_):
#         try:
#             esc = Escritor.objects.get(nome=nome_)
#             return esc;
#         except Escritor.DoesNotExist:
#             esc = Escritor(nome=nome_)
#             esc.save()
#             return esc

#     def __unicode__(self):
#         return "Nome: " + unicode(self.nome)


# class Filme(models.Model):
#     nome               = models.CharField(max_length=30, unique=True)
#     sinopse            = models.CharField(max_length=2000)
#     genero             = models.CharField(max_length=20)
#     link_foto          = models.CharField(max_length=100)
#     facebook_id        = models.CharField(max_length=1000)
#     atores_diretores   = models.ManyToManyField(Ator_Diretor, through="Atuou_Dirigiu_Filme")
#     escritores         = models.ManyToManyField(Escritor, through="Escreveu_Filme")
#     usuarios           = models.ManyToManyField(Usuario, through="Assistiu_Filme")

#     def get_or_create(self, nome_, facebook_id_, sinopse_, genero_, link_foto_):
#         try:
#             filme = Filme.objects.get(nome=nome_)
#             return filme
#         except Filme.DoesNotExist:
#             filme = Filme(nome=nome_, sinopse=sinopse_, genero=genero_, link_foto=link_foto_, facebook_id=facebook_id_)
#             filme.save()
#             print filme.nome
#             return filme

#     def __unicode__(self):
#         return "Nome: " + unicode(self.nome) + " - Genero: " + unicode(self.genero) + " - Sinopse: " + unicode(self.sinopse)


# class Like_Ator_Diretor(models.Model):
#     usuario_id = models.ForeignKey(Usuario)
#     ator_diretor_id = models.ForeignKey(Ator_Diretor)

#     class Meta:
#         unique_together = ("usuario_id", "ator_diretor_id")

#     def get_or_create(self, usuario, ator_diretor):
#         try:
#             like = Like_Ator_Diretor.objects.get(usuario_id=usuario, ator_diretor_id=ator_diretor)
#             return like
#         except Like_Ator_Diretor.DoesNotExist:
#             like = Like_Ator_Diretor(usuario_id=usuario, ator_diretor_id=ator_diretor)
#             like.save()
#             return like

#     def __unicode__(self):
#         return "Usuario: " + unicode(self.usuario_id.facebook_nome) + " - Ator/Diretor: " + unicode(self.ator_diretor_id.nome)


# class Like_Escritor(models.Model):
#     usuario_id  = models.ForeignKey(Usuario)
#     escritor_id = models.ForeignKey(Escritor)

#     class Meta:
#         unique_together = ("usuario_id", "escritor_id")

#     def get_or_create(self, usuario, escritor):
#         try:
#             like = Like_Escritor.objects.get(usuario_id=usuario, escritor_id=escritor)
#             return like
#         except Like_Escritor.DoesNotExist:
#             novoEscritor = Escritor()
#             escritor = novoEscritor.get_or_create(escritor.nome)
#             try: 
#                 like = Like_Escritor.objects.get(usuario_id=usuario, escritor_id=escritor)
#                 return like
#             except  Like_Escritor.DoesNotExist:
#                 like = Like_Escritor(usuario_id=usuario, escritor_id=escritor)
#                 like.save()
#                 return like

#     def __unicode__(self):
#         return "Usuario: " + unicode(self.usuario_id.facebook_nome) + " - Escritor: " + unicode(self.escritor_id.nome)


# class Atuou_Dirigiu_Filme(models.Model):
#     filme_id    = models.ForeignKey(Filme)
#     ator_diretor_id  = models.ForeignKey(Ator_Diretor)

#     class Meta:
#         unique_together = ("filme_id", "ator_diretor_id")

#     def get_or_create(self, filme, ator_diretor):
#         try:
#             atuou_dirigiu = Atuou_Dirigiu_Filme.objects.get(filme_id=filme, ator_diretor_id=ator_diretor)
#             return atuou_dirigiu;
#         except Atuou_Dirigiu_Filme.DoesNotExist:
#             atuou_dirigiu = Atuou_Dirigiu_Filme(filme_id=filme, ator_diretor_id=ator_diretor)
#             atuou_dirigiu.save()
#             return atuou_dirigiu

#     def __unicode__(self):
#         return "Filme: " + unicode(self.filme_id.nome) + " - Ator/Diretor: " + unicode(self.ator_diretor_id.nome)


# class Escreveu_Filme(models.Model):
#     filme_id    = models.ForeignKey(Filme)
#     escritor_id = models.ForeignKey(Escritor)

#     class Meta:
#         unique_together = ("filme_id", "escritor_id")

#     def get_or_create(self, filme, escreveu_):
#         try:
#             escreveu = Escreveu_Filme.objects.get(filme_id=filme, escritor_id=escreveu_)
#             return escreveu;
#         except Escreveu_Filme.DoesNotExist:
#             escreveu = Escreveu_Filme(filme_id=filme, escritor_id=escreveu_)
#             escreveu.save()
#             return escreveu

#     def __unicode__(self):
#         return "Filme: " + unicode(self.filme_id.nome) + " - Escritor: " + unicode(self.escritor_id.nome)


# class Assistiu_Filme(models.Model):
#     filme_id    = models.ForeignKey(Filme)
#     usuario_id  = models.ForeignKey(Usuario)

#     class Meta:
#         unique_together = ("filme_id", "usuario_id")

#     def get_or_create(self, filme, assistiu_):
#         try:
#             assistiu = Assistiu_Filme.objects.get(filme_id=filme, usuario_id=assistiu_)
#             return assistiu;
#         except Assistiu_Filme.DoesNotExist:
#             assistiu = Assistiu_Filme(filme_id=filme, usuario_id=assistiu_)
#             assistiu.save()
#             return assistiu

#     def __unicode__(self):
#         return "Filme: " + unicode(self.filme_id.nome) + " - Usuario: " + unicode(self.usuario_id.facebook_nome)









