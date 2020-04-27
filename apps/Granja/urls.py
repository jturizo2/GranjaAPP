from django.conf.urls import url, include
from django.urls import path
#from django.contrib import admin
#from django.urls import path
from apps.Granja.views import granja_list, granja_new, granja_delete, granja_edit, granja_admin
from django.contrib.auth.decorators import login_required
app_name = 'granja'
urlpatterns = [
    url(r'^listar$', login_required(granja_list.as_view()), name='list'),
    url(r'^nueva$', granja_new , name='new'),
    url(r'^eliminar/(?P<pk>\d+)/$', granja_delete.as_view() , name='delete'),
    url(r'^editar/(?P<pk>\d+)/$', granja_edit.as_view() , name='edit'),
    url(r'^admin/(?P<id_granja>\d+)/$', granja_admin , name='admin'),
] 