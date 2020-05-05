from rest_framework import serializers
from user.models import User

# 用于编写序列化规则

# 序列化适用于没有外键的表
# 有外键的表用序列化就只有引用的那一列列名
class UserSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似

    # 把id设置为非必填，否则添加时前端传递的数据缺少id会导致is_invalid方法校验不通过
    # id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = User
        # 写了几个字段在GET请求时就返回几个字段的数据
        # fields = ('id', 'account', 'phone', 'password', 'name', 'type')
        # 所有参数都要
        fields = '__all__'
