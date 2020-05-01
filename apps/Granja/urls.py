from django.conf.urls import url, include
from django.urls import path
#from django.contrib import admin
#from django.urls import path
from apps.Granja.views import *
from django.contrib.auth.decorators import login_required
app_name = 'granja'
urlpatterns = [
    url(r'^listar$', login_required(granja_list.as_view()), name='list'),
    url(r'^nueva$', granja_new , name='new'),
    url(r'^eliminar/(?P<pk>\d+)/$', granja_delete.as_view() , name='delete'),
    url(r'^editar/(?P<pk>\d+)/$', granja_edit.as_view() , name='edit'),
    url(r'^admin/(?P<id_granja>\d+)/$', granja_admin , name='admin'),
    url(r'^config$', granja_config , name='config'),
    #Concepto
    url(r'^listar_concepto$', granja_concepto_list.as_view() , name='list_concepto'),
    url(r'^new_concepto$', granja_concepto_new.as_view() , name='new_concepto'),
    url(r'^delete_concepto/(?P<pk>\d+)/$', granja_concepto_delete.as_view() , name='delete_concepto'),
    url(r'^edit_concepto/(?P<pk>\d+)/$', granja_concepto_edit.as_view() , name='edit_concepto'),
    #Concepto
    url(r'^listar_genero$', granja_genero_list.as_view() , name='list_genero'),
    url(r'^new_genero$', granja_genero_new.as_view() , name='new_genero'),
    url(r'^delete_genero/(?P<pk>\d+)/$', granja_genero_delete.as_view() , name='delete_genero'),
    url(r'^edit_genero/(?P<pk>\d+)/$', granja_genero_edit.as_view() , name='edit_genero'),
    #Etapas productivas
    url(r'^listar_eProductiva$', granja_eProductiva_list.as_view() , name='list_eProductiva'),
    url(r'^new_eProductiva$', granja_eProductiva_new.as_view() , name='new_eProductiva'),
    url(r'^delete_eProductiva/(?P<pk>\d+)/$', granja_eProductiva_delete.as_view() , name='delete_eProductiva'),
    url(r'^edit_eProductiva/(?P<pk>\d+)/$', granja_eProductiva_edit.as_view() , name='edit_eProductiva'),
    #Raza
    url(r'^listar_raza$', granja_raza_list.as_view() , name='list_raza'),
    url(r'^new_raza$', granja_raza_new.as_view() , name='new_raza'),
    url(r'^delete_raza/(?P<pk>\d+)/$', granja_raza_delete.as_view() , name='delete_raza'),
    url(r'^edit_raza/(?P<pk>\d+)/$', granja_raza_edit.as_view() , name='edit_raza'),
    #Proposito
    url(r'^listar_proposito$', granja_proposito_list.as_view() , name='list_proposito'),
    url(r'^new_proposito$', granja_proposito_new.as_view() , name='new_proposito'),
    url(r'^delete_proposito/(?P<pk>\d+)/$', granja_proposito_delete.as_view() , name='delete_proposito'),
    url(r'^edit_proposito/(?P<pk>\d+)/$', granja_proposito_edit.as_view() , name='edit_proposito'),
    #propietario
    url(r'^listar_propietario$', granja_propietario_list.as_view() , name='list_propietario'),
    url(r'^new_propietario$', granja_propietario_new , name='new_propietario'),
    url(r'^delete_propietario/(?P<pk>\d+)/$', granja_propietario_delete.as_view() , name='delete_propietario'),
    url(r'^edit_propietario/(?P<pk>\d+)/$', granja_propietario_edit.as_view() , name='edit_propietario'),
    #Insumo o servicio serviInsu
    url(r'^listar_serviInsu$', granja_serviInsu_list.as_view() , name='list_serviInsu'),
    url(r'^new_serviInsu$', granja_serviInsu_new , name='new_serviInsu'),
    url(r'^delete_serviInsu/(?P<pk>\d+)/$', granja_serviInsu_delete.as_view() , name='delete_serviInsu'),
    url(r'^edit_serviInsu/(?P<pk>\d+)/$', granja_serviInsu_edit.as_view() , name='edit_serviInsu'),
] 