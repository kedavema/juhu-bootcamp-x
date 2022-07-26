from django.db import models


class Laboratorio (models.Model):
    '''Modelo de Laboratorio'''
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=250)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=50)
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)
    estudios_clinicos = models.ManyToManyField('EstudioClinico', blank=True)

    def __str__(self):
        return self.nombre
        

class EstudioClinico (models.Model):
    '''Modelo para los Estudios Clinicos'''
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    precio = models.CharField(max_length=100)
    tipo_de_estudio = models.CharField(max_length=100)
    enfermedad = models.ForeignKey('Enfermedad', on_delete=models.CASCADE)
    laboratorios = models.ManyToManyField('laboratorio', blank=True)

    def __str__(self):
        return self.nombre


class Enfermedad(models.Model):
    '''Modelo para las enfermedades'''
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre