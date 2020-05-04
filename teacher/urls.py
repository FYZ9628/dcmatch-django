from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllTeacher', views.get_all_teacher),
    path('searchTeacher', views.search_teacher),
    path('searchTeacherByAccount', views.search_teacher_by_account),
    path('addTeacher', views.add_teacher),
    path('updateTeacher', views.update_teacher),
    path('deleteTeacher', views.delete_teacher),
]
