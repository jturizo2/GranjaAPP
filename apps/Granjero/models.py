from django.db import models
from apps.Granja.models import granja 
# Create your models here.

class hierro (models.Model):
    idIronCode =  models.CharField(max_length = 20)
    Img =  models.CharField(max_length = 100)

    def __str__(self):
        return "%s" % (self.idIronCode)

class propietario (models.Model):
    name = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    IdGranja = models.ForeignKey (granja, null = True, blank = True, on_delete = models.CASCADE)
    IdHierro = models.ForeignKey (hierro, null = True, blank = True, on_delete = models.CASCADE)
    correo = models.EmailField(max_length = 100)
    Telefono = models.CharField(max_length = 10)
    
    def __str__(self):
        return "%s %s" % (self.name, self.LastName)



