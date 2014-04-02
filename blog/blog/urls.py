from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from app.views import PublicacionView

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^$', 'app.views.inicio', name='inicio'),
    url(r'^noticias/$', 'app.views.noticias', name='noticias'),
    url(r'^categorias/$', 'app.views.categorias', name='categorias'),
    url(r'^noticia/(?P<id_noticia>\d+)$','app.views.detalle_noticia', name='detalle_noticia'),
    url(r'^contacto/$','app.views.contacto', name='contacto'),
    url(r'^exitoso/$','app.views.exitoso', name='exitoso'),
    url(r'^salir/$','app.views.salir', name='salir'),
    url(r'^login/$','app.views.ingresar', name='login'),

    url(r'^up/(\d+)$','app.views.up', name='up'),
    url(r'^down/(\d+)$','app.views.down', name='down'),

    url(r'^registrarse/$', 'app.views.register', name='registrarse'),
    url(r'^publicacion/$', PublicacionView.as_view(), name='publicacion'),

    url(r'^admin/', include(admin.site.urls)),
)
