from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllTeamContest', views.get_all_team_contest),
    path('searchTeamContestByStudentAccount', views.search_all_team_contest_by_student_account),
    path('searchTeamContestByTeacherAccount', views.search_all_team_contest_by_teacher_account),
    path('searchTeamContestByOrganizerAccount', views.search_all_team_contest_by_organizer_account),
    path('searchTeamContestById', views.search_team_contest_by_id),
    path('searchTeamContestByTeamName', views.search_all_team_contest_by_team_name),
    path('searchTeamContestByTeamNameAndContestDetailId',
         views.search_all_team_contest_by_team_name_and_contest_detail_id),
    path('searchTeamContestByContestDetailId', views.search_all_team_contest_by_contest_detail_id),
    path('addTeamContest', views.add_team_contest),
    path('updateTeamContest', views.update_team_contest),
    path('deleteTeamContest', views.delete_team_contest),
    path('deleteTeam', views.delete_team_contest_by_team),
]
