from django.conf.urls import url, include
#from django.contrib import admin
#from django.urls import path
from apps.Animal.views import *
app_name = 'animal'
urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^nuevo$', animal_form,name='new'),
    url(r'^listar$', animal_list, name='list'),
    url(r'^editar/(?P<id_animal>\d+)/$', animal_edit,name='edit'),
    url(r'^eliminar/(?P<id_animal>\d+)/$', animal_delete, name='delete'),
    url(r'^vista/(?P<id_animal>\d+)/$', animal_view, name='view'),
    url(r'^buscar/$', animal_search, name='search'),
    url(r'^descargar/$', animal_descargar, name='descargar'),
]