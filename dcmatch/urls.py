"""dcmatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api/', include(user.urls)),
    # 和下面用 path 这条语句作用相同
    path('api/', include('user.urls')),
    path('api/', include('register.urls')),
    path('api/', include('student.urls')),
    path('api/', include('teacher.urls')),
    path('api/', include('organizer.urls')),
    path('api/', include('school.urls')),
    path('api/', include('notice.urls')),
    path('api/', include('banner.urls')),
    path('api/', include('contest_detail.urls')),
    path('api/', include('contest.urls')),
    path('api/', include('team_contest.urls')),
    path('api/', include('login.urls')),
    path('api/', include('admin_login.urls')),
    path('api/', include('sign_up.urls')),
    path('api/', include('up_load_img.urls')),
    # 和上面两个语句的作用一样，都是可以访问到数据，不同的是这种方法不用在user中创建一个urls表
    # url(r'^user', user_views.user),
]
