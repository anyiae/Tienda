from email.mime import image
from django.db import models

# Create your models here.


class Perro(models.Model):
    idPerro = models.IntegerField(
        primary_key=True, verbose_name='Id de Articulo de Perro')
    nombrePerro = models.CharField(
        max_length=50, verbose_name='Nombre del Artículo')
    precio = models.CharField(
        max_length=50, verbose_name='Precio')
    descripcionperro = models.CharField(
        max_length=50, verbose_name='Descripcion Perro')

    def __str__(self):
        return self.idPerro


class Gato(models.Model):
    idGato = models.IntegerField(
        primary_key=True, verbose_name='Id de Articulo de Gato')
    nombreGato = models.CharField(
        max_length=50, verbose_name='Nombre del Artículo')
    preciogato = models.CharField(
        max_length=50, verbose_name='Precio')
    descripciongato = models.CharField(
        max_length=50, verbose_name='Descripcion Gato')

    def __str__(self):
        return self.idGato
