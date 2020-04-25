from django.urls import path
from django.conf.urls import url, include
from . import views
app_name = 'gallery'
urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
     path('image_gallery/', views.image_gallery, name='image_gallery'),
     url(r'^imagen/(?P<category_id>\d+)/$', views.image_gallery, name='image_gallery'),
                       
]