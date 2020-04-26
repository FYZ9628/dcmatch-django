from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from .models import User
from user.serializers import UserSerializer

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


def get_all_user(request):
    try:
        # 获取所有 user 数据
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        res = {
            "code": 200,
            "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def get_user(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        user = User.objects.filter(id=data.__getitem__('keywords'))
        if user.__len__() >= 1:
            temp_user = {
                "id": user[0].id,
                "account": user[0].account,
                "phone": user[0].phone,
                "password": user[0].password,
                "name": user[0].name,
                "type": user[0].type
            }
        else:
            temp_user = {}
        # 拿到的是一个对象
        # user = User.objects.get(id=data.__getitem__('keywords'))
        # 拿到的是一个数组
        # users = serializers.serialize("json", User.objects.filter(name=data.__getitem__('keywords')))
        # 获取所有 user 数据
        # users = User.objects.all()
        # 获取符合条件的 user 数据
        # users = User.objects.filter(name=data.__getitem__('keywords'))
        # serializer = UserSerializer(users, many=True)
        # print('测试serializer')
        # print(serializer.data)
        res = {
            "code": 200,
            "data": temp_user
            # "data": {'test1': '接家教'}
            # "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_user(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        users = User.objects.filter(name=data.__getitem__('keywords'))
        serializer = UserSerializer(users, many=True)
        res = {
            "code": 200,
            "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def delete_user(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        user = User.objects.filter(id=data.__getitem__('keywords')).delete()
        print(user.__len__())
        if user.__len__() > 2:
            delete_info = '删除成功'
        else:
            delete_info = '删除失败'
        res = {
            "code": 200,
            "data": delete_info
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")
