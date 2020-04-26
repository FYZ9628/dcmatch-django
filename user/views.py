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


# post 需要加，get请求不用加
@csrf_exempt
def search_user(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        users = User.objects.filter(name=data.__getitem__('name'))
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
def search_user_by_account(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        users = User.objects.filter(account=data.__getitem__('keywords'))
        if users.__len__() >= 1:
            temp_user = {
                "id": users[0].id,
                "account": users[0].account,
                "phone": users[0].phone,
                "password": users[0].password,
                "name": users[0].name,
                "type": users[0].type
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


@csrf_exempt
def search_user_by_phone(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        users = User.objects.filter(phone=data.__getitem__('keywords'))
        if users.__len__() >= 1:
            temp_user = {
                "id": users[0].id,
                "account": users[0].account,
                "phone": users[0].phone,
                "password": users[0].password,
                "name": users[0].name,
                "type": users[0].type
            }
        else:
            temp_user = {}
        res = {
            "code": 200,
            "data": temp_user
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def add_user(request):
    try:
        data = json.loads(request.body)
        user = User(account=data.__getitem__('account'),
                    phone=data.__getitem__('phone'),
                    password=data.__getitem__('password'),
                    name=data.__getitem__('name'),
                    type=data.__getitem__('type'))
        # 获取一个 user 数据
        users = User.objects.filter(account=user.account)
        print(users.__len__())
        if users.__len__() > 0:
            temp_user = {}
        else:
            user.save()
            temp_user = {
                "id": users[0].id,
                "account": users[0].account,
                "phone": users[0].phone,
                "password": users[0].password,
                "name": users[0].name,
                "type": users[0].type
            }
        res = {
            "code": 200,
            "data": temp_user
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def update_user(request):
    try:
        data = json.loads(request.body)
        user = User(account=data.__getitem__('account'),
                    phone=data.__getitem__('phone'),
                    password=data.__getitem__('password'),
                    name=data.__getitem__('name'),
                    type=data.__getitem__('type'))
        # 获取一个 user 数据
        users = User.objects.filter(account=user.account)
        print(users.__len__())
        if users.__len__() > 0:
            users.update(phone=user.phone,
                         password=user.password,
                         type=user.type)
            temp_user = {
                "id": users[0].id,
                "account": users[0].account,
                "phone": users[0].phone,
                "password": users[0].password,
                "name": users[0].name,
                "type": users[0].type
            }
        else:
            temp_user = {}
        res = {
            "code": 200,
            "data": temp_user
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
        user = User(account=data.__getitem__('account'),
                    phone=data.__getitem__('phone'),
                    password=data.__getitem__('password'),
                    name=data.__getitem__('name'),
                    type=data.__getitem__('type'))
        # 获取一个 user 数据
        users = User.objects.filter(account=user.account)
        print(users.__len__())
        if users.__len__() > 0:
            users.delete()
            result = {
                "code": 100
            }
        else:
            result = {
                "code": 400
            }
        res = {
            "code": 200,
            "data": result
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")