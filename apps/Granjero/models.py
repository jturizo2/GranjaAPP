from django.db import models
from apps.Granja.models import granja 
from django.contrib.auth.models import User
# Create your models here.

class propietario (models.Model):
    user = models.ForeignKey (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    IdGranja = models.ForeignKey (granja, null = True, blank = True, on_delete = models.CASCADE)
    correo = models.EmailField(max_length = 100)
    Telefono = models.CharField(max_length = 10)
    imagePropietario = models.ImageField(upload_to = 'propietarios/', default = 'gallery/static/images/no-img.jpg')
    imageHierro = models.ImageField(upload_to = 'hierro/', default = 'gallery/static/images/no-img.jpg')
    
    def __str__(self):
        return "%s %s" % (self.name, self.LastName)



