from django.db import models
from django.contrib.auth.models import User
#libreria para los thumbnails
from easy_thumbnails.fields import ThumbnailerImageField
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.categoria
    
class Publicacion(models.Model):
    autor = models.ForeignKey(User)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=60, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    contenido = models.TextField(max_length = 255)
    categoria = models.ForeignKey(Categoria)
    fechaPub = models.DateTimeField(auto_now_add = True)
    imagen = ThumbnailerImageField(upload_to="img-pub", null=True, blank=True)
    votos = models.IntegerField(default=0)
    
    class Meta():
        verbose_name_plural = 'Publicaciones'
    
    def __unicode__(self):
        return self.titulo
    
class Comentario(models.Model):
    autor = models.ForeignKey(User)
    publicacion = models.ForeignKey(Publicacion)
    comentario = models.TextField(max_length = 255)
    
    def __unicode__(self):
        return self.comentario
    
    

