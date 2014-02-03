from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.index', name='inicio'),
    url(r'^home', 'core.views.home', name='home'),
    url(r'^inicio', 'core.views.inicio', name='entrou'),
    url(r'^filme/(?P<filme_id>\d+)/detalhes', 'core.views.detalhe', name='detalhe'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'base_login.html'}, name='logout'),
    # url(r'^What2Watch/', include('What2Watch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
