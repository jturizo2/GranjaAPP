from django.conf.urls import url, include
#from django.contrib import admin
#from django.urls import path
from apps.Granja.views import index

urlpatterns = [
    url(r'^index$', index),

]