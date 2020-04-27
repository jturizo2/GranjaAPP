from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class granja (models.Model):
    user = models.ForeignKey (User, null = True, blank = True, on_delete = models.CASCADE)
    Cod = models.CharField(max_length = 20)
    Name = models.CharField(max_length = 80)
    Details = models.CharField(max_length = 500)
    Hec = models.FloatField()
    Div = models.FloatField()
    NumPozos = models.IntegerField()
    image = models.ImageField(upload_to = 'granja/', default = 'gallery/static/images/no-img.jpg')

    def __str__(self):
        return "%s" % (self.Name)

