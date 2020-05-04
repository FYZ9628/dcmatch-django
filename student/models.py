from django.db import models

from user.models import User

""""
    1、生成迁移文件 -- 》 将模板生成sql语句
        makemigrations
    2、执行迁移 --》 执行sql
        migrate
"""


# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.OneToOneField("user.User", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    sex = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    admission_date = models.CharField(max_length=20)
    graduation_date = models.CharField(max_length=20)
    academy = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    id_img = models.CharField(max_length=255)

    def __str__(self):
        return self.id

    # def __unicode__(self):
    #     return self.username

    # 设置表名
    # 如果不设置的话默认的表名为 user_user
    # 即 app名称_class类名
    class Meta:
        db_table = 'student'
        # 修改自带后台的table名
        # verbose_name = "用户管理"
        # 去掉自带后台table名的复数形式
        verbose_name_plural = db_table
