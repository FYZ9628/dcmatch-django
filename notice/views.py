from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from notice.serializers import CJsonEncoder
from .models import Notice

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


def get_all_notice(request):
    try:
        # 获取所有 user 数据
        notices = Notice.objects.all()  # 获取全部列表
        notices_list = []
        for notice in notices:
            temp_notice = {
                "id": notice.id,
                "title": notice.title,
                "time": notice.time,
                "organizer": {
                    "id": notice.organizer.id,
                    "user": {
                        "id": notice.organizer.user.id,
                        "account": notice.organizer.user.account,
                        "phone": notice.organizer.user.phone,
                        "password": notice.organizer.user.password,
                        "name": notice.organizer.user.name,
                        "type": notice.organizer.user.type
                    },
                    "email": notice.organizer.email,
                    "school": notice.organizer.school,
                    "establishDate": notice.organizer.establish_date,
                    "schoolType": notice.organizer.school_type,
                    "schoolRunningType": notice.organizer.school_running_type,
                    "idImg": notice.organizer.id_img
                },
                "content": notice.content
            }
            notices_list.append(temp_notice)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": notices_list
            # "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_notice_by_title_like(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        notices = Notice.objects.filter(Q(title__icontains=data.__getitem__('keywords')))
        notices_list = []
        for notice in notices:
            temp_notice = {
                "id": notice.id,
                "title": notice.title,
                "time": notice.time,
                "organizer": {
                    "id": notice.organizer.id,
                    "user": {
                        "id": notice.organizer.user.id,
                        "account": notice.organizer.user.account,
                        "phone": notice.organizer.user.phone,
                        "password": notice.organizer.user.password,
                        "name": notice.organizer.user.name,
                        "type": notice.organizer.user.type
                    },
                    "email": notice.organizer.email,
                    "school": notice.organizer.school,
                    "establishDate": notice.organizer.establish_date,
                    "schoolType": notice.organizer.school_type,
                    "schoolRunningType": notice.organizer.school_running_type,
                    "idImg": notice.organizer.id_img
                },
                "content": notice.content
            }
            notices_list.append(temp_notice)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": notices_list
            # "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def search_notice_by_organizer_account(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        notices = Notice.objects.filter(organizer__user__account=data.__getitem__('keywords'))
        print(notices.__len__())
        if notices.__len__() >= 1:
            temp_notice = {
                "id": notices[0].id,
                "title": notices[0].title,
                "time": notices[0].time,
                "organizer": {
                    "id": notices[0].organizer.id,
                    "user": {
                        "id": notices[0].organizer.user.id,
                        "account": notices[0].organizer.user.account,
                        "phone": notices[0].organizer.user.phone,
                        "password": notices[0].organizer.user.password,
                        "name": notices[0].organizer.user.name,
                        "type": notices[0].organizer.user.type
                    },
                    "email": notices[0].organizer.email,
                    "school": notices[0].organizer.school,
                    "establishDate": notices[0].organizer.establish_date,
                    "schoolType": notices[0].organizer.school_type,
                    "schoolRunningType": notices[0].organizer.school_running_type,
                    "idImg": notices[0].organizer.id_img
                },
                "content": notices[0].content
            }
        else:
            temp_notice = {}
        res = {
            "code": 200,
            "data": temp_notice
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def add_notice(request):
    try:
        data = json.loads(request.body)
        notice = Notice(
            title=data.__getitem__('title'),
            time=data.__getitem__('time'),
            organizer_id=data.__getitem__('organizer').__getitem__('id'),
            content=data.__getitem__('content'),
        )
        # 获取一个 register 数据
        notices = Notice.objects.filter(id=data.__getitem__('id'))
        print(notices.__len__())
        if notices.__len__() > 0:
            temp_notice = {}
        else:
            notice.save()
            temp_notice = {
                "id": notice.id,
                "title": notice.title,
                "time": notice.time,
                "organizer": {
                    "id": notice.organizer.id,
                    "user": {
                        "id": notice.organizer.user.id,
                        "account": notice.organizer.user.account,
                        "phone": notice.organizer.user.phone,
                        "password": notice.organizer.user.password,
                        "name": notice.organizer.user.name,
                        "type": notice.organizer.user.type
                    },
                    "email": notice.organizer.email,
                    "school": notice.organizer.school,
                    "establishDate": notice.organizer.establish_date,
                    "schoolType": notice.organizer.school_type,
                    "schoolRunningType": notice.organizer.school_running_type,
                    "idImg": notice.organizer.id_img
                },
                "content": notice.content
            }
        res = {
            "code": 200,
            "data": temp_notice
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def update_notice(request):
    try:
        data = json.loads(request.body)
        # 获取一个 register 数据
        notices = Notice.objects.filter(id=data.__getitem__('id'))
        print(notices.__len__())
        if notices.__len__() > 0:
            notices.update(
                title=data.__getitem__('title'),
                time=data.__getitem__('time'),
                organizer_id=data.__getitem__('organizer').__getitem__('id'),
                content=data.__getitem__('content'),
            )
            temp_notice = {
                "id": notices[0].id,
                "title": notices[0].title,
                "time": notices[0].time,
                "organizer": {
                    "id": notices[0].organizer.id,
                    "user": {
                        "id": notices[0].organizer.user.id,
                        "account": notices[0].organizer.user.account,
                        "phone": notices[0].organizer.user.phone,
                        "password": notices[0].organizer.user.password,
                        "name": notices[0].organizer.user.name,
                        "type": notices[0].organizer.user.type
                    },
                    "email": notices[0].organizer.email,
                    "school": notices[0].organizer.school,
                    "establishDate": notices[0].organizer.establish_date,
                    "schoolType": notices[0].organizer.school_type,
                    "schoolRunningType": notices[0].organizer.school_running_type,
                    "idImg": notices[0].organizer.id_img
                },
                "content": notices[0].content
            }
        else:
            temp_notice = {}
        res = {
            "code": 200,
            "data": temp_notice
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def delete_notice(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        notices = Notice.objects.filter(id=data.__getitem__('id'))
        print(notices.__len__())
        if notices.__len__() > 0:
            notices.delete()
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
