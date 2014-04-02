from django.contrib import admin
from .models import *

class PublicacionAdmin(admin.ModelAdmin):
	list_display = ('autor', 'titulo')
	raw_id_fields = ('autor',)

admin.site.register(Categoria)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Comentario)
