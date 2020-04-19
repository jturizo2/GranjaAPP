from django.contrib import admin
from apps.Animal.models import concepto, genero, etapa_productiva, raza, proposito, animal

# Register your models here.
admin.site.register(concepto)
admin.site.register(genero)
admin.site.register(etapa_productiva)
admin.site.register(raza)
admin.site.register(proposito)
admin.site.register(animal)
