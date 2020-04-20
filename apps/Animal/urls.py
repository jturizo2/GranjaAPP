from django.conf.urls import url, include
#from django.contrib import admin
#from django.urls import path
from apps.Animal.views import index, animal_form, animal_list, animal_edit, animal_delete

urlpatterns = [
    url(r'^$', index),
    url(r'^nuevo$', animal_form),
    url(r'^listar$', animal_list),
    url(r'^editar/(?P<id_animal>\d+)/$', animal_edit),
    url(r'^eliminar/(?P<id_animal>\d+)/$', animal_delete),

]