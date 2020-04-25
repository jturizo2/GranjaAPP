from django.db import models
import datetime
from apps.Animal.models import animal 
# Create your models here.
class ClassTransInsServ (models.Model):
    clase  =  models.CharField(max_length = 30)
    Detalle = models.CharField(max_length = 100)
    def __str__(self):
        return "%s" % (self.clase)

class serviInsu (models.Model):
    Tipo  = models.ForeignKey (ClassTransInsServ, null = True, blank = True, on_delete = models.CASCADE)
    Nombre = models.CharField(max_length = 30)
    Valor_Unidad  =  models.FloatField()
    Detalle  =  models.CharField(max_length = 100)
    Proveedor  =  models.CharField(max_length = 30)
    Telefono  =  models.CharField(max_length = 30)

    def __str__(self):
        return "%s" % (self.Nombre)

class TypeTrans (models.Model):
    Tipo  =  models.CharField(max_length = 30)
    Detalle = models.CharField(max_length = 100)
    def __str__(self):
        return "%s" % (self.Tipo)

class ClassTrans (models.Model):
    clase  =  models.CharField(max_length = 30)
    Detalle = models.CharField(max_length = 100)
    def __str__(self):
        return "%s" % (self.clase)

class transaction (models.Model):
    TypeTrans = models.ForeignKey (TypeTrans, null = True, blank = True, on_delete = models.CASCADE)
    classTrans = models.ForeignKey (ClassTrans, null = True, blank = True, on_delete = models.CASCADE)
    date = models.DateField(default = datetime.date.today)
    AnimalCode = models.ForeignKey (animal, null = True, blank = True, on_delete = models.CASCADE)
    detail = models.CharField(max_length = 100)
    Value = models.FloatField()
    quantity = models.FloatField()

    def __str__(self):
        return "%s" % (self.id)
