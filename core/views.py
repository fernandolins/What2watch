# -*- coding: utf-8 -*-

from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'base.html', {})

def home(request):
    if request.user.is_authenticated():
        #print dir(request.user)
        id_ = request.user.username
        usuario = Usuario.objects.get(facebook_id=id_)
        filmes = getFilmesRecomendados(usuario)
        filmes = sort(filmes)

        print request
        for f in filmes[:10]:
            print f["score"]
        return render_to_response('pages/home.html', context_instance=RequestContext(request, {'usuario': usuario.facebook_nome, "recomenda": filmes[:10]}), )
    else:
        return HttpResponseRedirect('/')
