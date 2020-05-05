from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllBanner', views.get_all_banner),
    path('searchBanner', views.search_banner_by_name_like),
    path('addBanner', views.add_banner),
    path('updateBanner', views.update_banner),
    path('deleteBanner', views.delete_banner),
]
