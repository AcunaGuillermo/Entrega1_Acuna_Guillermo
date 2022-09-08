from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'    

class Equipo(models.Model):
    nombre = models.CharField(max_length=128)
    pais = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.nombre}, {self.pais}'  

class Posicion(models.Model):
    posicion = models.CharField(max_length=128)
    equipo = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.equipo}, {self.posicion}'    