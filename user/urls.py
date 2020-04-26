from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('getAllUser', views.get_all_user),
    path('searchUser', views.search_user),
    path('searchUserByAccount', views.search_user_by_account),
    path('searchUserByPhone', views.search_user_by_phone),
    path('addUser', views.add_user),
    path('updateUser', views.update_user),
    path('deleteUser', views.delete_user),
    # url(r'user/$', views.user, ),
    # url(r'^user_list/$', views.user_list),
    # # url(r'^user/(?P<pk>[0-9]+)/$', views.user),
    # url(r'^user/', views.user),
    # url(r'^search/', views.search),
    # url(r'^delete_user/', views.user),
    # url(r'^delete_user/', views.delete_user()),
    # path('testapi', views.testapi),
]
