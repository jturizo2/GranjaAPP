from django.db import models
import datetime
from apps.Granjero.models import hierro
from apps.Granja.models import granja  
# Create your models here.

class concepto (models.Model):
    concepto =  models.CharField(max_length = 30)
    detalle_concepto = models.CharField(max_length = 500)
    def __str__(self):
        return "%s" % (self.concepto)

class genero (models.Model):
    genero =  models.CharField(max_length = 7)
    
    def __str__(self):
        return "%s" % (self.genero)

class etapa_productiva (models.Model):
    etapa_prod = models.CharField(max_length = 20)
    
    def __str__(self):
        return "%s" % (self.etapa_prod)

class raza (models.Model):
    raza = models.CharField(max_length = 15)
    
    def __str__(self):
        return "%s" % (self.raza)
    
class proposito (models.Model):
    tipo_proposito  = models.CharField(max_length = 25)
    
    def __str__(self):
        return "%s" % (self.tipo_proposito)

class animal (models.Model):
    IdGranja = models.ForeignKey (granja, null = True, blank = True, on_delete = models.CASCADE)
    concepto = models.ForeignKey (concepto, null = True, blank = True, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 50)
    Valor_inicial = models.FloatField()
    Codigo_animal = models.CharField(max_length = 50)
    Genero = models.ForeignKey (genero, null = True, blank = True, on_delete = models.CASCADE)
    Etapa_productiva = models.ForeignKey (etapa_productiva, null = True, blank = True, on_delete = models.CASCADE) 
    Raza = models.ForeignKey (raza, null = True, blank = True, on_delete = models.CASCADE)
    Hierro = models.ForeignKey (hierro, null = True, blank = True, on_delete = models.CASCADE)
    Proposito = models.ForeignKey (proposito, null = True, blank = True, on_delete = models.CASCADE)
    Fecha_recibida = models.DateField(default = datetime.date.today())
    Fecha_nacimiento = models.DateField()
    Código_mama = models.CharField(max_length = 20, null = True, blank = True)
    Código_papa = models.CharField(max_length = 20, null = True, blank = True)
    
    def __str__(self):
        return "%s" % (self.Codigo_animal)
    