from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt

from user.models import User
from .models import Organizer
from student.serializers import StudentSerializer

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


def get_all_organizer(request):
    try:
        # 获取所有 user 数据
        organizers = Organizer.objects.all()  # 获取全部列表
        organizers_list = []
        for organizer in organizers:
            temp_organizer = {
                "id": organizer.id,
                "user": {
                    "id": organizer.user.id,
                    "account": organizer.user.account,
                    "phone": organizer.user.phone,
                    "password": organizer.user.password,
                    "name": organizer.user.name,
                    "type": organizer.user.type
                },
                "email": organizer.email,
                "school": organizer.school,
                "establishDate": organizer.establish_date,
                "schoolType": organizer.school_type,
                "schoolRunningType": organizer.school_running_type,
                "idImg": organizer.id_img,
            }
            organizers_list.append(temp_organizer)
        # serializer = StudentSerializer(students, many=True)
        res = organizers_list
        # res = {
        #     "code": 200,
        #     "data": organizers_list
        #     # "data": serializer.data
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_organizer(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        organizers = Organizer.objects.filter(
            Q(user__name__icontains=data.__getitem__('keywords')) |
            Q(user__account__icontains=data.__getitem__('keywords')))
        organizers_list = []
        for organizer in organizers:
            temp_organizer = {
                "id": organizer.id,
                "user": {
                    "id": organizer.user.id,
                    "account": organizer.user.account,
                    "phone": organizer.user.phone,
                    "password": organizer.user.password,
                    "name": organizer.user.name,
                    "type": organizer.user.type
                },
                "email": organizer.email,
                "school": organizer.school,
                "establishDate": organizer.establish_date,
                "schoolType": organizer.school_type,
                "schoolRunningType": organizer.school_running_type,
                "idImg": organizer.id_img,
            }
            organizers_list.append(temp_organizer)
        # serializer = StudentSerializer(students, many=True)
        res = organizers_list
        # res = {
        #     "code": 200,
        #     "data": organizers_list
        #     # "data": serializer.data
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def search_organizer_by_account(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        organizers = Organizer.objects.filter(user__account=data.__getitem__('keywords'))
        if organizers.__len__() >= 1:
            temp_organizer = {
                "id": organizers[0].id,
                "user": {
                    "id": organizers[0].user.id,
                    "account": organizers[0].user.account,
                    "phone": organizers[0].user.phone,
                    "password": organizers[0].user.password,
                    "name": organizers[0].user.name,
                    "type": organizers[0].user.type
                },
                "email": organizers[0].email,
                "school": organizers[0].school,
                "establishDate": organizers[0].establish_date,
                "schoolType": organizers[0].school_type,
                "schoolRunningType": organizers[0].school_running_type,
                "idImg": organizers[0].id_img,
            }
        else:
            temp_organizer = {}
        res = temp_organizer
        # res = {
        #     "code": 200,
        #     "data": temp_organizer
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def add_organizer(request):
    try:
        data = json.loads(request.body)
        user = User(
            account=data.__getitem__('user').__getitem__('account'),
            phone=data.__getitem__('user').__getitem__('phone'),
            password=data.__getitem__('user').__getitem__('password'),
            name=data.__getitem__('user').__getitem__('name'),
            type=data.__getitem__('user').__getitem__('type')
        )
        # 获取一个 user 数据
        users = User.objects.filter(account=user.account)
        print(users.__len__())
        if users.__len__() > 0:
            temp_organizer = {}
        else:
            # 先在 user 表中添加一条数据
            user.save()
            organizer = Organizer(
                user_id=user.id,
                email=data.__getitem__('email'),
                school=data.__getitem__('school'),
                establish_date=data.__getitem__('establishDate'),
                school_type=data.__getitem__('schoolType'),
                school_running_type=data.__getitem__('schoolRunningType'),
                id_img=data.__getitem__('idImg'),
            )
            # 再在 student 表中添加一条数据
            organizer.save()
            temp_organizer = {
                "id": organizer.id,
                "user": {
                    "id": user.id,
                    "account": user.account,
                    "phone": user.phone,
                    "password": user.password,
                    "name": user.name,
                    "type": user.type
                },
                "email": organizer.email,
                "school": organizer.school,
                "establishDate": organizer.establish_date,
                "schoolType": organizer.school_type,
                "schoolRunningType": organizer.school_running_type,
                "idImg": organizer.id_img,
            }
        res = temp_organizer
        # res = {
        #     "code": 200,
        #     "data": temp_organizer
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def update_organizer(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        users = User.objects.filter(account=data.__getitem__('user').__getitem__('account'))
        print(users.__len__())
        if users.__len__() > 0:
            users.update(
                phone=data.__getitem__('user').__getitem__('phone'),
                password=data.__getitem__('user').__getitem__('password'),
                name=data.__getitem__('user').__getitem__('name'),
                type=data.__getitem__('user').__getitem__('type')
            )
            # 获取一个 user 数据
            organizers = Organizer.objects.filter(user_id=users[0].id)
            organizers.update(
                email=data.__getitem__('email'),
                school=data.__getitem__('school'),
                establish_date=data.__getitem__('establishDate'),
                school_type=data.__getitem__('schoolType'),
                school_running_type=data.__getitem__('schoolRunningType'),
                id_img=data.__getitem__('idImg'),
            )
            temp_organizer = {
                "id": organizers[0].id,
                "user": {
                    "id": users[0].id,
                    "account": users[0].account,
                    "phone": users[0].phone,
                    "password": users[0].password,
                    "name": users[0].name,
                    "type": users[0].type
                },
                "email": organizers[0].email,
                "school": organizers[0].school,
                "establishDate": organizers[0].establish_date,
                "schoolType": organizers[0].school_type,
                "schoolRunningType": organizers[0].school_running_type,
                "idImg": organizers[0].id_img,
            }
        else:
            temp_organizer = {}
        res = temp_organizer
        # res = {
        #     "code": 200,
        #     "data": temp_organizer
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def delete_organizer(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        # users = User.objects.filter(account=user.account)
        organizers = Organizer.objects.filter(id=data.__getitem__('id'))
        print(organizers.__len__())
        if organizers.__len__() > 0:
            users = User.objects.filter(id=organizers[0].user.id)
            organizers.delete()
            users.delete()
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
