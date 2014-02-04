# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Usuario(models.Model):
    facebook_id        = models.CharField(max_length=100, primary_key=True)
    facebook_nome      = models.CharField(max_length=100)
    access_token       = models.CharField(max_length=300)

    def get_or_create(self, face_id, face_nome, accessToken):
        try:
            facebook_usuario = Usuario.objects.get(facebook_id=face_id)
            facebook_usuario.access_token = accessToken
            print accessToken
            facebook_usuario.save()
            return facebook_usuario
        except Usuario.DoesNotExist:
            facebook_usuario = Usuario(facebook_id=face_id, facebook_nome=face_nome, access_token=accessToken)
            facebook_usuario.save()
            return facebook_usuario

    def __unicode__(self):
        return "Nome: " + unicode(self.facebook_nome)


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "Nome: " + unicode(self.nome)


class Diretor(Pessoa):
    usuarios = models.ManyToManyField(Usuario, through="Like_Diretor")

    def get_or_create(self, nome_):
        try:
            diretor = Diretor.objects.get(nome=nome_)
            return diretor
        except Diretor.DoesNotExist:
            diretor = Diretor(nome=nome_)
            diretor.save()
            return diretor


class Ator(Pessoa):
    usuarios = models.ManyToManyField(Usuario, through="Like_Ator")

    def get_or_create(self, nome_):
        try:
            ator = Ator.objects.get(nome=nome_)
            return ator
        except Ator.DoesNotExist:
            ator = Ator(nome=nome_)
            ator.save()
            return ator


class Escritor(Pessoa):
    usuarios = models.ManyToManyField(Usuario, through="Like_Escritor")

    def get_or_create(self, nome_):
        try:
            esc = Escritor.objects.get(nome=nome_)
            return esc;
        except Escritor.DoesNotExist:
            esc = Escritor(nome=nome_)
            esc.save()
            return esc


class Filme(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sinopse = models.CharField(max_length=2000)
    genero = models.CharField(max_length=100)
    link_foto = models.CharField(max_length=400)
    facebook_id = models.CharField(max_length=1000, unique=True)
    atores = models.ManyToManyField(Ator, through="Atuou_Filme")
    diretores = models.ManyToManyField(Diretor, through="Dirigiu_Filme")
    escritores = models.ManyToManyField(Escritor, through="Escreveu_Filme")
    usuarios  = models.ManyToManyField(Usuario, through="Assistiu_Filme")
    imdb_id = models.CharField(max_length=100, unique=True)

    def get_or_create(self, nome_, facebook_id_, sinopse_, genero_, link_foto_, imdb_id_):
        try:
            filme = Filme.objects.get(nome=nome_)
            return filme
        except Filme.DoesNotExist:
            filme = Filme(
                nome=nome_,
                sinopse=sinopse_,
                genero=genero_,
                link_foto=link_foto_,
                facebook_id=facebook_id_,
                imdb_id=imdb_id_
            )
            filme.save()
            return filme

    def get_foto(self):
        if self.link_foto == 'N/A':
            return 'http://i.media-imdb.com/images/mobile/film-40x54.png'
        return self.link_foto

    def __unicode__(self):
        return "Nome: " + unicode(self.nome) + " - Genero: " + unicode(self.genero) + " - Sinopse: " + unicode(self.sinopse)


class Like_Diretor(models.Model):
    usuario_id = models.ForeignKey(Usuario)
    diretor_id = models.ForeignKey(Diretor)

    class Meta:
        unique_together = ("usuario_id", "diretor_id")

    def get_or_create(self, usuario, diretor):
        try:
            like = Like_Diretor.objects.get(usuario_id=usuario, diretor_id=diretor)
            return like
        except Like_Diretor.DoesNotExist:
            like = Like_Diretor(usuario_id=usuario, diretor_id=diretor)
            like.save()
            return like

    def __unicode__(self):
        return "Usuario: " + unicode(self.usuario_id.facebook_nome) + " - Diretor: " + unicode(self.diretor_id.nome)


class Like_Ator(models.Model):
    usuario_id = models.ForeignKey(Usuario)
    ator_id = models.ForeignKey(Ator)

    class Meta:
        unique_together = ("usuario_id", "ator_id")

    def get_or_create(self, usuario, ator):
        try:
            like = Like_Ator.objects.get(usuario_id=usuario, ator_id=ator)
            return like
        except Like_Ator.DoesNotExist:
            like = Like_Ator(usuario_id=usuario, ator_id=ator)
            like.save()
            return like

    def __unicode__(self):
        return "Usuario: " + unicode(self.usuario_id.facebook_nome) + " - Ator: " + unicode(self.ator_id.nome)


class Like_Escritor(models.Model):
    usuario_id  = models.ForeignKey(Usuario)
    escritor_id = models.ForeignKey(Escritor)

    class Meta:
        unique_together = ("usuario_id", "escritor_id")

    def get_or_create(self, usuario, escritor):
        try:
            like = Like_Escritor.objects.get(usuario_id=usuario, escritor_id=escritor)
            return like
        except Like_Escritor.DoesNotExist:
            novoEscritor = Escritor()
            escritor = novoEscritor.get_or_create(escritor.nome)
            try: 
                like = Like_Escritor.objects.get(usuario_id=usuario, escritor_id=escritor)
                return like
            except  Like_Escritor.DoesNotExist:
                like = Like_Escritor(usuario_id=usuario, escritor_id=escritor)
                like.save()
                return like

    def __unicode__(self):
        return "Usuario: " + unicode(self.usuario_id.facebook_nome) + " - Escritor: " + unicode(self.escritor_id.nome)


class Atuou_Filme(models.Model):
    filme_id    = models.ForeignKey(Filme)
    ator_id  = models.ForeignKey(Ator)

    class Meta:
        unique_together = ("filme_id", "ator_id")

    def get_or_create(self, filme, ator):
        try:
            atuou = Atuou_Filme.objects.get(filme_id=filme, ator_id=ator)
            return atuou
        except Atuou_Filme.DoesNotExist:
            atuou = Atuou_Filme(filme_id=filme, ator_id=ator)
            atuou.save()
            return atuou

    def __unicode__(self):
        return "Filme: " + unicode(self.filme_id.nome) + " - Ator: " + unicode(self.ator_id.nome)


class Dirigiu_Filme(models.Model):
    filme_id    = models.ForeignKey(Filme)
    diretor_id  = models.ForeignKey(Diretor)

    class Meta:
        unique_together = ("filme_id", "diretor_id")

    def get_or_create(self, filme, diretor):
        try:
            dirigiu = Dirigiu_Filme.objects.get(filme_id=filme, diretor_id=diretor)
            return dirigiu;
        except Dirigiu_Filme.DoesNotExist:
            dirigiu = Dirigiu_Filme(filme_id=filme, diretor_id=diretor)
            dirigiu.save()
            return dirigiu

    def __unicode__(self):
        return "Filme: " + unicode(self.filme_id.nome) + " - Diretor: " + unicode(self.diretor_id.nome)


class Escreveu_Filme(models.Model):
    filme_id    = models.ForeignKey(Filme)
    escritor_id = models.ForeignKey(Escritor)

    class Meta:
        unique_together = ("filme_id", "escritor_id")

    def get_or_create(self, filme, escreveu_):
        try:
            escreveu = Escreveu_Filme.objects.get(filme_id=filme, escritor_id=escreveu_)
            return escreveu;
        except Escreveu_Filme.DoesNotExist:
            escreveu = Escreveu_Filme(filme_id=filme, escritor_id=escreveu_)
            escreveu.save()
            return escreveu

    def __unicode__(self):
        return "Filme: " + unicode(self.filme_id.nome) + " - Escritor: " + unicode(self.escritor_id.nome)


class Assistiu_Filme(models.Model):
    filme_id    = models.ForeignKey(Filme)
    usuario_id  = models.ForeignKey(Usuario)

    class Meta:
        unique_together = ("filme_id", "usuario_id")

    def get_or_create(self, filme, assistiu_):
        try:
            assistiu = Assistiu_Filme.objects.get(filme_id=filme, usuario_id=assistiu_)
            return assistiu;
        except Assistiu_Filme.DoesNotExist:
            assistiu = Assistiu_Filme(filme_id=filme, usuario_id=assistiu_)
            assistiu.save()
            return assistiu

    def __unicode__(self):
        return "Filme: " + unicode(self.filme_id.nome) + " - Usuario: " + unicode(self.usuario_id.facebook_nome)


class FilmesRecomendados(models.Model):
    usuario = models.ForeignKey(Usuario)
    filme = models.ForeignKey(Filme)
    score = models.PositiveIntegerField(u'Score')
