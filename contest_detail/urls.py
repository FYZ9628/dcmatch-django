from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllContestDetail', views.get_all_contest_detail),
    path('searchContestDetail', views.search_all_contest_detail_by_title_like),
    path('searchContestDetailById', views.search_contest_detail_by_id),
    path('searchContestDetailByContestTitle', views.search_contest_detail_by_title),
    path('searchContestDetailByOrganizerAccount', views.search_all_contest_detail_by_organizer_account),
    path('addContestDetail', views.add_contest_detail),
    path('updateContestDetail', views.update_contest_detail),
    path('deleteContestDetail', views.delete_contest_detail),
]
