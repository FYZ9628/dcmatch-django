from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from register.models import Register

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


@csrf_exempt
def admin_login(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        users1 = User.objects.filter(
            account=data.__getitem__('account'),
            password=data.__getitem__('password')
        )
        if users1.__len__() != 0:
            if users1[0].type == 1:
                result = {
                    "code": 100,
                    "account": users1[0].account,
                    "password": users1[0].password,
                    "name": users1[0].name
                }
            else:
                result = {
                    "code": 400
                }
            res = {
                "code": 200,
                "data": result
            }
            return HttpResponse(json.dumps(res), content_type="application/json")
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


@csrf_exempt
def update_password(request):
    try:
        data = json.loads(request.body)
        user = User(account=data.__getitem__('account'),
                    phone=data.__getitem__('phone'),
                    password=data.__getitem__('password'),
                    name=data.__getitem__('name'),
                    type=data.__getitem__('type'))
        # 获取一个 user 数据
        users = User.objects.filter(
            account=data.__getitem__('account'),
            password=data.__getitem__('password')
        )
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
