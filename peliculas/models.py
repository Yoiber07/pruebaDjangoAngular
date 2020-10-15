from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):

    nombre = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,related_name="director")
    class Meta:
        verbose_name = ("Pelicula")
        verbose_name_plural = ("Peliculas")

    def __str__(self):
        return self.nombre
