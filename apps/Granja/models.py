from django.db import models

# Create your models here.
class granja (models.Model):
    Cod = models.CharField(max_length = 20)
    Name = models.CharField(max_length = 80)
    Details = models.CharField(max_length = 500)
    Hec = models.FloatField()
    Div = models.FloatField()
    NumPozos = models.IntegerField()
    Img = models.CharField( max_length = 150)

