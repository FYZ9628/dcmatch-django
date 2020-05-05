from rest_framework import serializers
from contest_detail.models import ContestDetail
import json
import datetime


# 用于编写序列化规则


class ContestDetailSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似

    # 把id设置为非必填，否则添加时前端传递的数据缺少id会导致is_invalid方法校验不通过
    # id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = ContestDetail
        # 写了几个字段在GET请求时就返回几个字段的数据
        # fields = ('id', 'account', 'phone', 'password', 'name', 'type')
        # 所有参数都要
        fields = '__all__'


# 解决Python自带的json序列化工具不能序列化datetime类型数据问题
# 使用时候只要在json.dumps增加一个cls参数即可：
# json.dumps(res, cls=CJsonEncoder),
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
