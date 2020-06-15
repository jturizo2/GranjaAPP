from django.conf.urls import url, include
#from django.contrib import admin
#from django.urls import path
from apps.trans.views import *
app_name = 'trans'
urlpatterns = [
    url(r'^index$', index),
    # Comerio de animales
    url(r'^listar_mov$',mov_list, name='list'),
    url(r'^new_mov$',mov_new , name='new'),
    url(r'^delete_mov/(?P<id_mov>\d+)/$',mov_delete, name='delete'),
    url(r'^edit_mov/(?P<id_mov>\d+)/$',mov_edit, name='edit'),   
    url(r'^search_mov/$',search_mov, name='search'),
    
    # CRUD Insumos Servicios
    url(r'^listar_InsServ$',InsServ_list, name='list_InsServ'),
    url(r'^new_InsServ$',InsServ_new , name='new_InsServ'),
    url(r'^delete_InsServ/(?P<id_mov>\d+)/$',InsServ_delete, name='delete_InsServ'),
    url(r'^edit_InsServ/(?P<id_mov>\d+)/$',InsServ_edit, name='edit_InsServ'),   
    url(r'^search_InsServ/$',search_InsServ, name='search_InsServ'),
]