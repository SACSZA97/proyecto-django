from django.contrib import admin
from .models import Alumnos
from .models import Comentarios
from .models import ComentarioContacto
# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields  = ('created', 'updated')
    list_display = ('matricula','nombre','carrera','turnno')
    search_fields = ('matricula','nombre','carrera','turnno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turnno')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    readonly_fields  = ('created', 'id')
    list_display = ('id','created')
    search_fields = ('id','created')
    date_hierarchy = 'created'

admin.site.register(Comentarios, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)