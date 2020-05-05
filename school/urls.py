from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllSchool', views.get_all_school),
    path('searchSchool', views.search_school_by_name_like),
    path('addSchool', views.add_school),
    path('updateSchool', views.update_school),
    path('deleteSchool', views.delete_school),
]
