from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('teamSignUpAddStudent', views.team_sign_up_add_student),
    path('teamSignUpAddTeacher', views.team_sign_up_add_teacher),
]
