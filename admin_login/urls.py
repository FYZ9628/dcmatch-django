from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('admin_login', views.admin_login),
    path('updatePassword', views.update_password),
]
