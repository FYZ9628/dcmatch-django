from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('upLoadImg', views.up_load_img),
    path('deleteImg', views.delete_img),
]
