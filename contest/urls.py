from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllContest', views.get_all_contest),
    path('searchContestByStudentAccount', views.search_all_contest_by_student_account),
    path('searchContestByOrganizerAccount', views.search_all_contest_by_organizer_account),
    path('searchContestById', views.search_contest_by_id),
    path('searchContestByContestDetailId', views.search_all_contest_by_contest_detail_id),
    path('addContest', views.add_contest),
    path('updateContest', views.update_contest),
    path('deleteContest', views.delete_contest),
]
