from django.conf.urls import url, include
from django.urls import path
#from django.contrib import admin
#from django.urls import path
from apps.Granja.views import index, granja_list, granja_new, granja_delete, granja_edit
app_name = 'granja'
urlpatterns = [
    url(r'^index$', index),
    url(r'^listar$', granja_list.as_view(), name='list'),
    url(r'^nueva$', granja_new , name='new'),
    url(r'^eliminar/(?P<pk>\d+)/$', granja_delete.as_view() , name='delete'),
    url(r'^editar/(?P<pk>\d+)/$', granja_edit.as_view() , name='edit'),
] 