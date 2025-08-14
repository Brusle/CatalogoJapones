from django.contrib import admin
# CORRECCIÓN: Importamos los nuevos modelos Anime y Personaje
from .models import Anime, Personaje

# Registramos el modelo Anime en el panel de administrador
@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Registramos el modelo Personaje en el panel de administrador
@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'anime')
    list_filter = ('anime',)
    search_fields = ('nombre', 'biografia', 'anime__nombre')