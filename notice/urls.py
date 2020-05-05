from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllNotice', views.get_all_notice),
    path('searchNotice', views.search_notice_by_title_like),
    path('searchNoticeByOrganizerAccount', views.search_notice_by_organizer_account),
    path('addNotice', views.add_notice),
    path('updateNotice', views.update_notice),
    path('deleteNotice', views.delete_notice),
]
