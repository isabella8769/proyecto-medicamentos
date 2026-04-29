from django.db import models

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_especialidad

# Create your models here.
class Agente(models.Model):
    id_agente = models.AutoField(primary_key=True)
    dni=models.IntegerField(unique=True)
    nombre_apellido = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    id_especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_apellido
    