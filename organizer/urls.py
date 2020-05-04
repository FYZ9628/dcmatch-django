from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllOrganizer', views.get_all_organizer),
    path('organizerInfo', views.get_all_organizer),
    path('searchOrganizer', views.search_organizer),
    path('searchOrganizerByAccount', views.search_organizer_by_account),
    path('addOrganizer', views.add_organizer),
    path('updateOrganizer', views.update_organizer),
    path('deleteOrganizer', views.delete_organizer),
]
