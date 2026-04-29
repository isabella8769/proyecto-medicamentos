from django.db import models


class Supervisor(models.Model):

    nombre_apellido=models.CharField(max_length=100)
    contacto=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_apellido
    
class Deposito(models.Model):
    id_deposito= models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Hueco(models.Model):
    id_hueco=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)
    id_supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion
