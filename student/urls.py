from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllStudent', views.get_all_student),
    path('searchStudent', views.search_student),
    path('searchStudentByAccount', views.search_student_by_account),
    path('addStudent', views.add_student),
    path('updateStudent', views.update_student),
    path('deleteStudent', views.delete_student),
]
