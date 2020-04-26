from django.contrib import admin
from user.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # 后台要显示的字段和可点击的链接
    list_display = ["id", "account", "phone", "password", "name", "type"]
    list_display_links = ["id", "account", "phone", "password", "name", "type"]
    list_per_page = 10
    # 设置按id正序
    ordering = ("id",)

    # 搜索功能及可搜索字段
    search_fields = ('name',)


admin.site.site_header = '学科竞赛赛程管理信息系统'
admin.site.site_title = '学科竞赛赛程管理信息系统后台'
admin.site.register(User, UserAdmin)
