from django.db import models
from django.utils import timezone

# Create your models here.

class Estudiante(models.Model):
    rut = models.CharField(max_length=9,primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # campo direccion oculto
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.OneToOneField(Estudiante, related_name="direccion", on_delete=models.CASCADE)    

class Profesor(models.Model):
    rut = models.CharField(max_length=9,primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #atrib fantasma cursos

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, default='-')
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor = models.ForeignKey(Profesor, max_length=9, related_name="cursos", null=True, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')

