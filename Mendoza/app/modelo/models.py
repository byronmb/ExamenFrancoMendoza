from django.db import models

# Create your models here.

class Estudiante(models.Model):

    listaGenero= (
        ('f', 'Femenino'),
        ('m', 'Masculino')
    )

    cedula = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    genero = models.CharField(max_length=15, choices= listaGenero, null=True)
    matricula = models.CharField(max_length=10)
    curso = models.CharField(max_length=1)
