from django.conf.urls import url, include
#from django.contrib import admin
#from django.urls import path
from apps.usuario.views import registar_usuario
app_name = 'usuario'
urlpatterns = [
    url(r'^nuevo$',registar_usuario.as_view() , name="new"),
]