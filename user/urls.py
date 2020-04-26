from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # url(r'user/$', views.user, ),
    # url(r'^user_list/$', views.user_list),
    # # url(r'^user/(?P<pk>[0-9]+)/$', views.user),
    # url(r'^user/', views.user),
    # url(r'^search/', views.search),
    path('getUser', views.get_user),
    path('searchUser', views.search_user),
    # url(r'^delete_user/', views.user),
    # url(r'^delete_user/', views.delete_user()),
    # path('testapi', views.testapi),
    path('getAllUser', views.get_all_user),
    path('deleteUser', views.delete_user),
]
