# -*- coding: utf-8 -*-

from json import loads
from urllib2 import urlopen, Request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import FacebookForm
from .models import (
    Usuario, Filme,
    Assistiu_Filme, 
    Diretor, Ator,
    Escritor, Like_Ator,
    Like_Diretor, Like_Escritor,
    Dirigiu_Filme, Atuou_Filme,
    Escreveu_Filme,
    FilmesRecomendados
)
# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return redirect('entrou')
    else:
        filmes = Filme.objects.all()
        return render(request, 'base_login.html', {'filmes': filmes})


@login_required
def inicio(request):
    context = {}

    context['filmes'] = Filme.objects.all()

    print request.user
    id_ = request.user.username
    usuario = Usuario.objects.get(facebook_id=id_)
    context['usuario'] = usuario

    # filmes = Filme.objects.all()
    # for filme in filmes:
    #     filme.link_foto = get_foto(filme.facebook_id, usuario.access_token)
    #     filme.save()

    if 'logou' not in request.session:
        print 'chamou'
        filmes_recomendados = getFilmesRecomendados(usuario)
        request.session['logou'] = True
    else:
        print 'nao chamou'
    context['filmes_recomendados'] = FilmesRecomendados.objects.filter(usuario=usuario)

    context['assistiu'] = Assistiu_Filme.objects.filter(usuario_id=usuario)

    return render(request, 'index.html', context)


@login_required
def detalhe(request, filme_id):
    context = {}

    context['filme'] = Filme.objects.get(id=filme_id)

    id_ = request.user.username
    usuario = Usuario.objects.get(facebook_id=id_)
    context['usuario'] = usuario
    # print dir(context['filme'].atores)
    # print context['filme'].diretores.all()

    return render(request, 'detalhes.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')


def home(request):
    if request.method == 'POST':
        # try:
        form = FacebookForm(request.POST or None)
        if form.is_valid():
            facebook_id = request.POST['facebook_id']
            access_token = request.POST['access_token']
            facebook_json = loads(urlopen('https://graph.facebook.com/' + facebook_id + '?fields=name,email&access_token=' + access_token + '').read())
            try:
                use = User.objects.get(username=facebook_json['id'])
            except User.DoesNotExist:
                use = User.objects.create_user(
                    username=facebook_json['id'],
                    password=facebook_json['id'],
                    email=facebook_json['email']
                )
                use.save()

            login_user = authenticate(username=use.username, password=use.username)
            if login_user is not None:
                if login_user.is_active:
                    auth_login(request, login_user)
                    return facebook_dados(facebook_json, access_token)
                    # Redirecione para uma pagina de sucesso.
                else:
                    messages.error(request, 'Erro. Permissão negada, conta desabilitada.')
                    return HttpResponse(status=403)
                    # return render(request, 'base.html', {})
            else:
                # Return an 'invalid login' error message.
                print "invalido"
                return HttpResponse(status=400)
                # return render_to_response('base_login.html', locals(), context_instance=RequestContext(request), )
        else:
            print 'invalido'
            return HttpResponse(status=404)
        # except Exception as e:
        #     print e
        #     raise e

    print 'nao deveria imprimir isso.'
    # return redirect('/inicio')
    return HttpResponse(status=500)


def get_movie_omdb_json(title):
    title = unicode(title)
    try:
        url = u"http://www.omdbapi.com/?t={0}".format(title).replace(' ', '+');
        request = Request(url)
        response = urlopen(request)
        movie_imdb_json = loads(response.read())
        if 'Error' in movie_imdb_json:
            return get_movie_imdb_json(title)
    except:
        return get_movie_imdb_json(title)

    return movie_imdb_json


def get_movie_imdb_json(title):
    url = u"http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q={0}".format(title).replace(' ', '+');
    list_character_imdb_json = loads(urlopen(url.encode('utf-8')).read())
    try:
        if 'name_popular' in list_character_imdb_json:
            movie_imdb_json = list_character_imdb_json['name_popular'][0]
            return get_movie_omdb_json(movie_imdb_json['title'])
        elif 'title_approx' in list_character_imdb_json:
            movie_imdb_json = list_character_imdb_json['title_approx'][0]
            return get_movie_omdb_json(movie_imdb_json['title'])
        return False
    except Exception as e:
        print e
        print 'Não há Filme'
        return False


def get_character_imdb_json(name):
    url = u"http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q={0}".format(name).replace(' ', '+');
    list_character_imdb_json = loads(urlopen(url).read())
    try:
        if 'name_popular' in list_character_imdb_json:
            character_imdb_json = list_character_imdb_json['name_popular'][0]
            return character_imdb_json
        return False
    except Exception as e:
        print e
        print 'Não há personagem'
        return False


def get_likes(id, access_token):
    url = u"https://graph.facebook.com/{0}/likes?access_token={1}&limit=1000".format(id, access_token)
    likes_json = loads(urlopen(url).read())
    return likes_json


def get_foto(id, access_token):
    url = u"https://graph.facebook.com/{0}/picture?type=large&access_token={1}".format(id, access_token)
    response = urlopen(url)
    return response.url


def facebook_dados(facebook_json, access_token):
    # try:
    facebook_usuario = Usuario()
    facebook_usuario = facebook_usuario.get_or_create(
        unicode(facebook_json['id']),
        unicode(facebook_json['name']),
        access_token
    )

    likes = get_likes(facebook_json['id'], access_token)
    for like in likes['data']:
        if like['category'] == "Movie":
            if not Filme.objects.filter(facebook_id=like['id']).exists():
                movie_imdb = get_movie_omdb_json(like['name'])
                if movie_imdb and 'Error' not in movie_imdb:
                    filme = Filme()
                    filme = filme.get_or_create(
                        movie_imdb['Title'],
                        like['id'],
                        movie_imdb['Plot'],
                        movie_imdb['Genre'],
                        get_foto(like['id'], access_token),
                        movie_imdb['imdbID']
                    )

                    assistiu = Assistiu_Filme()
                    assistiu = assistiu.get_or_create(filme, facebook_usuario)

                    diretores = movie_imdb['Director'].replace(', ',',').split(',')
                    for nome_ in diretores:
                        diretor = Diretor()
                        diretor = diretor.get_or_create(nome_)

                        dirigiu = Dirigiu_Filme()
                        dirigiu = dirigiu.get_or_create(filme, diretor)

                    atores = movie_imdb['Actors'].replace(', ',',').split(',')
                    for nome_ in atores:
                        ator = Ator()
                        ator = ator.get_or_create(nome_)

                        atuou = Atuou_Filme()
                        atuou = atuou.get_or_create(filme, ator)

                    escritores = movie_imdb['Writer'].replace(', ',',').split(',')
                    for nome_ in escritores:
                        escritor = Escritor()
                        escritor = escritor.get_or_create(nome_)

                        escreveu = Escreveu_Filme()
                        escreveu = escreveu.get_or_create(filme, escritor)

        elif like['category'] == "Author":
            if not Escritor.objects.filter(nome=like['name']).exists():
                character_imdb = get_character_imdb_json(like['name'])
                if character_imdb:
                    if character_imdb['description'].startswith('Writer'):
                        escritor = Escritor()
                        escritor = escritor.get_or_create(like['name'])

                        like_escritor = Like_Escritor()
                        like_escritor = like_escritor.get_or_create(facebook_usuario, escritor)

        elif like['category'] == "Actor/director":
            character_imdb = get_character_imdb_json(like['name'])
            if character_imdb:
                if character_imdb['description'].startswith('Actress') or character_imdb['description'].startswith('Actor'):
                    ator = Ator()
                    ator = ator.get_or_create(like['name'])

                    like_ator = Like_Ator()
                    like_ator = like_ator.get_or_create(facebook_usuario, ator)
                elif character_imdb['description'].startswith('Director') or character_imdb['description'].startswith('Producer'):
                    diretor = Diretor()
                    diretor = diretor.get_or_create(like['name'])

                    like_diretor = Like_Diretor()
                    like_diretor = like_diretor.get_or_create(facebook_usuario, diretor)

    return HttpResponse(status=200)
    # except Exception as e:
    #     print 'dados facebook', e
    #     return HttpResponse(status=500)


def getFilmesRecomendados(usuario):

    all_filmes = Filme.objects.all()
    likes_filmes = Assistiu_Filme.objects.filter(usuario_id=usuario)
    next_filmes = []

    lista_ = []
    for movie in all_filmes:
        add = True
        stop = False
        for filme in likes_filmes:
            if filme.filme_id != movie and add and not stop:
                add = True
            else:
                add = False
                stop =True

        if add == True:
            if movie not in next_filmes:
                next_filmes.append(movie)
                next_movie = {}
                next_movie["filme"] = movie
                next_movie["score"] = 0
                lista_.append(next_movie)


    likes_atores = Like_Ator.objects.filter(usuario_id=usuario)
    likes_diretores = Like_Diretor.objects.filter(usuario_id=usuario)
    lista_likes_atores = []
    lista_likes_diretor = []
    likes_both = []

    for like in likes_atores:
        lista_likes_atores.append(like.ator_id)

    for like in likes_diretores:
        lista_likes_diretor.append(like.diretor_id)

    #score por ator
    for ator in lista_likes_atores:
        ator_filme = Atuou_Filme.objects.filter(ator_id=ator)
        for f in ator_filme:
            for m in lista_:
                if f.filme_id.facebook_id == m["filme"].facebook_id:
                    m["score"] += 1
                    print "bateu ator"

    #score por diretor
    for diretor in lista_likes_diretor:
        diretor_filme = Dirigiu_Filme.objects.filter(diretor_id=diretor)
        for d in diretor_filme:
            for m in lista_:
                if d.filme_id.facebook_id == m["filme"].facebook_id:
                    m["score"] += 1
                    print "bateu diretor"

    #por enquanto sem 'both'

    #score por escritor
    likes_escritor = Like_Escritor.objects.filter(usuario_id=usuario)

    for like in likes_escritor:
        escreveu = Escreveu_Filme.objects.filter(escritor_id=like.escritor_id)
        for e in escreveu:
            for m in lista_:
                if e.filme_id.facebook_id == m["filme"].facebook_id:
                    m["score"] += 1
                    print "bateu escritor"

    #score por genero
    lista_genero = []
    for f in likes_filmes:
        generos = f.filme_id.genero.replace(" ", "").lower().split(",")
        for g in generos:
            if g not in lista_genero:
                lista_genero.append(g)

    for m in lista_:
        for g in lista_genero:
            if m["filme"].genero.lower().__contains__(g):
                m["score"] += 1
                print "bateu genero"


    for recomendado in lista_:
        filme = FilmesRecomendados()
        filme = filme.get_or_create(usuario, recomendado['filme'], recomendado['score'])
