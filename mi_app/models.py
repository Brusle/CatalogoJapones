from django.db import models

class Anime(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Anime")

    def __str__(self):
        return self.nombre

class Personaje(models.Model):
    # Relacionamos al personaje con un anime. Si se borra el anime, se borran sus personajes.
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='personajes')
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Personaje")
    biografia = models.TextField(verbose_name="Biografía")
    # Campo para subir la imagen del personaje.
    imagen = models.ImageField(upload_to='characters/', blank=True, null=True, verbose_name="Imagen")

    def __str__(self):
        return f"{self.nombre} ({self.anime.nombre})"