from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from .models import Register
from register.serializers import RegisterSerializer

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""

# post 需要加，get请求不用加
# @csrf_exempt


def get_all_register(request):
    try:
        # 获取所有 user 数据
        registers = Register.objects.all()
        serializer = RegisterSerializer(registers, many=True)
        res = serializer.data
        # res = {
        #     "code": 200,
        #     "data": serializer.data
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def search_register_by_phone(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        registers = Register.objects.filter(phone=data.__getitem__('keywords'))
        if registers.__len__() >= 1:
            temp_register = {
                "id": registers[0].id,
                "phone": registers[0].phone,
                "password": registers[0].password
            }
        else:
            temp_register = {}
        res = temp_register
        # res = {
        #     "code": 200,
        #     "data": temp_register
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def add_register(request):
    try:
        data = json.loads(request.body)
        register = Register(
            phone=data.__getitem__('phone'),
            password=data.__getitem__('password'))
        # 获取一个 register 数据
        registers = Register.objects.filter(phone=register.phone)
        print(registers.__len__())
        if registers.__len__() > 0:
            temp_register = {}
        else:
            register.save()
            temp_register = {
                "phone": register.phone,
                "password": register.password
            }
        res = temp_register
        # res = {
        #     "code": 200,
        #     "data": temp_register
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def update_register(request):
    try:
        data = json.loads(request.body)
        register = Register(
            phone=data.__getitem__('phone'),
            password=data.__getitem__('password'))
        # 获取一个 register 数据
        registers = Register.objects.filter(phone=register.phone)
        print(registers.__len__())
        if registers.__len__() > 0:
            registers.update(phone=register.phone,
                             password=register.password)
            temp_register = {
                "id": registers[0].id,
                "phone": registers[0].phone,
                "password": registers[0].password
            }
        else:
            temp_register = {}
        res = temp_register
        # res = {
        #     "code": 200,
        #     "data": temp_register
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def update_register_by_id(request):
    try:
        data = json.loads(request.body)
        register = Register(
            id=data.__getitem__('id'),
            phone=data.__getitem__('phone'),
            password=data.__getitem__('password'))
        # 获取一个 register 数据
        registers = Register.objects.filter(id=register.id)
        print(registers.__len__())
        if registers.__len__() > 0:
            registers.update(phone=register.phone,
                             password=register.password)
            temp_register = {
                "id": registers[0].id,
                "phone": registers[0].phone,
                "password": registers[0].password
            }
        else:
            temp_register = {}
        res = temp_register
        # res = {
        #     "code": 200,
        #     "data": temp_register
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def delete_register(request):
    try:
        data = json.loads(request.body)
        register = Register(id=data.__getitem__('id'),
                            phone=data.__getitem__('phone'),
                            password=data.__getitem__('password'))
        # 获取一个 user 数据
        # users = User.objects.filter(account=user.account)
        registers = Register.objects.filter(id=register.id)
        print(registers.__len__())
        if registers.__len__() > 0:
            registers.delete()
            result = {
                "code": 100
            }
        else:
            result = {
                "code": 400
            }
        res = result
        # res = {
        #     "code": 200,
        #     "data": result
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")
