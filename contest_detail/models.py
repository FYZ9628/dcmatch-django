from django.db import models

""""
    1、生成迁移文件 -- 》 将模板生成sql语句
        makemigrations
    2、执行迁移 --》 执行sql
        migrate
"""


# Create your models here.
class ContestDetail(models.Model):
    id = models.AutoField(primary_key=True)
    contestTitle = models.CharField(max_length=255)
    organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE)
    contestContent = models.TextField()
    signUpStartTime = models.CharField()
    signUpEndTime = models.CharField()
    publishTime = models.CharField()
    place = models.CharField(max_length=255)
    holdDate = models.CharField(max_length=255)
    holdStartTime = models.CharField(max_length=255)
    holdEndTime = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    upperLimit = models.IntegerField()
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.id

    # def __unicode__(self):
    #     return self.username

    # 设置表名
    # 如果不设置的话默认的表名为 user_user
    # 即 app名称_class类名
    class Meta:
        db_table = 'contest_detail'
        # 修改自带后台的table名
        # verbose_name = "用户管理"
        # 去掉自带后台table名的复数形式
        verbose_name_plural = db_table