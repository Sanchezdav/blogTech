from django.contrib import admin
from .models import *

admin.site.register(Perfil)
admin.site.register(Categoria)
admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(Like)