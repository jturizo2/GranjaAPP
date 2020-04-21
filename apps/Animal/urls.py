from django.conf.urls import url, include
#from django.contrib import admin
#from django.urls import path
from apps.Animal.views import index, animal_form, animal_list, animal_edit, animal_delete
app_name = 'animal'
urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^nuevo$', animal_form),
    url(r'^listar$', animal_list, name='list'),
    url(r'^editar/(?P<id_animal>\d+)/$', animal_edit,name='edit'),
    url(r'^eliminar/(?P<id_animal>\d+)/$', animal_delete, name='delete'),

]