from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from contest_detail.serializers import CJsonEncoder
from .models import ContestDetail

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


def get_all_contest_detail(request):
    try:
        # 获取所有 user 数据
        contest_details = ContestDetail.objects.all()  # 获取全部列表
        contest_details_list = []
        for contest_detail in contest_details:
            temp_contest_detail = {
                "id": contest_detail.id,
                "contestTitle": contest_detail.contest_title,
                "organizer": {
                    "id": contest_detail.organizer.id,
                    "user": {
                        "id": contest_detail.organizer.user.id,
                        "account": contest_detail.organizer.user.account,
                        "phone": contest_detail.organizer.user.phone,
                        "password": contest_detail.organizer.user.password,
                        "name": contest_detail.organizer.user.name,
                        "type": contest_detail.organizer.user.type,
                    },
                    "email": contest_detail.organizer.email,
                    "school": contest_detail.organizer.school,
                    "establishDate": contest_detail.organizer.establish_date,
                    "schoolType": contest_detail.organizer.school_type,
                    "schoolRunningType": contest_detail.organizer.school_running_type,
                    "idImg": contest_detail.organizer.id_img,
                },
                "contestContent": contest_detail.contest_content,
                "signUpStartTime": contest_detail.sign_up_start_time,
                "signUpEndTime": contest_detail.sign_up_end_time,
                "publishTime": contest_detail.publish_time,
                "place": contest_detail.place,
                "holdDate": contest_detail.hold_date,
                "holdStartTime": contest_detail.hold_start_time,
                "holdEndTime": contest_detail.hold_end_time,
                "type": contest_detail.type,
                "upperLimit": contest_detail.upper_limit,
                "state": contest_detail.state,
            }
            contest_details_list.append(temp_contest_detail)
        # serializer = StudentSerializer(students, many=True)
        res = contest_details_list
        # res = {
        #     "code": 200,
        #     "data": contest_details_list
        #     # "data": serializer.data
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_all_contest_detail_by_title_like(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        contest_details = ContestDetail.objects.filter(Q(contest_title__icontains=data.__getitem__('keywords')))
        contest_details_list = []
        for contest_detail in contest_details:
            temp_contest_detail = {
                "id": contest_detail.id,
                "contestTitle": contest_detail.contest_title,
                "organizer": {
                    "id": contest_detail.organizer.id,
                    "user": {
                        "id": contest_detail.organizer.user.id,
                        "account": contest_detail.organizer.user.account,
                        "phone": contest_detail.organizer.user.phone,
                        "password": contest_detail.organizer.user.password,
                        "name": contest_detail.organizer.user.name,
                        "type": contest_detail.organizer.user.type,
                    },
                    "email": contest_detail.organizer.email,
                    "school": contest_detail.organizer.school,
                    "establishDate": contest_detail.organizer.establish_date,
                    "schoolType": contest_detail.organizer.school_type,
                    "schoolRunningType": contest_detail.organizer.school_running_type,
                    "idImg": contest_detail.organizer.id_img,
                },
                "contestContent": contest_detail.contest_content,
                "signUpStartTime": contest_detail.sign_up_start_time,
                "signUpEndTime": contest_detail.sign_up_end_time,
                "publishTime": contest_detail.publish_time,
                "place": contest_detail.place,
                "holdDate": contest_detail.hold_date,
                "holdStartTime": contest_detail.hold_start_time,
                "holdEndTime": contest_detail.hold_end_time,
                "type": contest_detail.type,
                "upperLimit": contest_detail.upper_limit,
                "state": contest_detail.state,
            }
            contest_details_list.append(temp_contest_detail)
        # serializer = StudentSerializer(students, many=True)
        res = contest_details_list
        # res = {
        #     "code": 200,
        #     "data": contest_details_list
        #     # "data": serializer.data
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_contest_detail_by_id(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        contest_details = ContestDetail.objects.filter(id=data.__getitem__('keywords'))
        print(contest_details.__len__())
        if contest_details.__len__() >= 1:
            temp_contest_detail = {
                "id": contest_details[0].id,
                "contestTitle": contest_details[0].contest_title,
                "organizer": {
                    "id": contest_details[0].organizer.id,
                    "user": {
                        "id": contest_details[0].organizer.user.id,
                        "account": contest_details[0].organizer.user.account,
                        "phone": contest_details[0].organizer.user.phone,
                        "password": contest_details[0].organizer.user.password,
                        "name": contest_details[0].organizer.user.name,
                        "type": contest_details[0].organizer.user.type,
                    },
                    "email": contest_details[0].organizer.email,
                    "school": contest_details[0].organizer.school,
                    "establishDate": contest_details[0].organizer.establish_date,
                    "schoolType": contest_details[0].organizer.school_type,
                    "schoolRunningType": contest_details[0].organizer.school_running_type,
                    "idImg": contest_details[0].organizer.id_img,
                },
                "contestContent": contest_details[0].contest_content,
                "signUpStartTime": contest_details[0].sign_up_start_time,
                "signUpEndTime": contest_details[0].sign_up_end_time,
                "publishTime": contest_details[0].publish_time,
                "place": contest_details[0].place,
                "holdDate": contest_details[0].hold_date,
                "holdStartTime": contest_details[0].hold_start_time,
                "holdEndTime": contest_details[0].hold_end_time,
                "type": contest_details[0].type,
                "upperLimit": contest_details[0].upper_limit,
                "state": contest_details[0].state,
            }
        else:
            temp_contest_detail = {}
        res = temp_contest_detail
        # res = {
        #     "code": 200,
        #     "data": temp_contest_detail
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_contest_detail_by_title(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        contest_details = ContestDetail.objects.filter(contest_title=data.__getitem__('keywords'))
        print(contest_details.__len__())
        if contest_details.__len__() >= 1:
            temp_contest_detail = {
                "id": contest_details[0].id,
                "contestTitle": contest_details[0].contest_title,
                "organizer": {
                    "id": contest_details[0].organizer.id,
                    "user": {
                        "id": contest_details[0].organizer.user.id,
                        "account": contest_details[0].organizer.user.account,
                        "phone": contest_details[0].organizer.user.phone,
                        "password": contest_details[0].organizer.user.password,
                        "name": contest_details[0].organizer.user.name,
                        "type": contest_details[0].organizer.user.type,
                    },
                    "email": contest_details[0].organizer.email,
                    "school": contest_details[0].organizer.school,
                    "establishDate": contest_details[0].organizer.establish_date,
                    "schoolType": contest_details[0].organizer.school_type,
                    "schoolRunningType": contest_details[0].organizer.school_running_type,
                    "idImg": contest_details[0].organizer.id_img,
                },
                "contestContent": contest_details[0].contest_content,
                "signUpStartTime": contest_details[0].sign_up_start_time,
                "signUpEndTime": contest_details[0].sign_up_end_time,
                "publishTime": contest_details[0].publish_time,
                "place": contest_details[0].place,
                "holdDate": contest_details[0].hold_date,
                "holdStartTime": contest_details[0].hold_start_time,
                "holdEndTime": contest_details[0].hold_end_time,
                "type": contest_details[0].type,
                "upperLimit": contest_details[0].upper_limit,
                "state": contest_details[0].state,
            }
        else:
            temp_contest_detail = {}
        res = temp_contest_detail
        # res = {
        #     "code": 200,
        #     "data": temp_contest_detail
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_all_contest_detail_by_organizer_account(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        contest_details = ContestDetail.objects.filter(organizer__user__account=data.__getitem__('keywords'))
        contest_details_list = []
        for contest_detail in contest_details:
            temp_contest_detail = {
                "id": contest_detail.id,
                "contestTitle": contest_detail.contest_title,
                "organizer": {
                    "id": contest_detail.organizer.id,
                    "user": {
                        "id": contest_detail.organizer.user.id,
                        "account": contest_detail.organizer.user.account,
                        "phone": contest_detail.organizer.user.phone,
                        "password": contest_detail.organizer.user.password,
                        "name": contest_detail.organizer.user.name,
                        "type": contest_detail.organizer.user.type,
                    },
                    "email": contest_detail.organizer.email,
                    "school": contest_detail.organizer.school,
                    "establishDate": contest_detail.organizer.establish_date,
                    "schoolType": contest_detail.organizer.school_type,
                    "schoolRunningType": contest_detail.organizer.school_running_type,
                    "idImg": contest_detail.organizer.id_img,
                },
                "contestContent": contest_detail.contest_content,
                "signUpStartTime": contest_detail.sign_up_start_time,
                "signUpEndTime": contest_detail.sign_up_end_time,
                "publishTime": contest_detail.publish_time,
                "place": contest_detail.place,
                "holdDate": contest_detail.hold_date,
                "holdStartTime": contest_detail.hold_start_time,
                "holdEndTime": contest_detail.hold_end_time,
                "type": contest_detail.type,
                "upperLimit": contest_detail.upper_limit,
                "state": contest_detail.state,
            }
            contest_details_list.append(temp_contest_detail)
        # serializer = StudentSerializer(students, many=True)
        res = contest_details_list
        # res = {
        #     "code": 200,
        #     "data": contest_details_list
        #     # "data": serializer.data
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def add_contest_detail(request):
    try:
        data = json.loads(request.body)
        contest_detail = ContestDetail(
            contest_title=data.__getitem__('contestTitle'),
            organizer_id=data.__getitem__('organizer').__getitem__('id'),
            contest_content=data.__getitem__('contestContent'),
            sign_up_start_time=data.__getitem__('signUpStartTime'),
            sign_up_end_time=data.__getitem__('signUpEndTime'),
            publish_time=data.__getitem__('publishTime'),
            place=data.__getitem__('place'),
            hold_date=data.__getitem__('holdDate'),
            hold_start_time=data.__getitem__('holdStartTime'),
            hold_end_time=data.__getitem__('holdEndTime'),
            type=data.__getitem__('type'),
            upper_limit=data.__getitem__('upperLimit'),
            state=data.__getitem__('state'),
        )
        # 获取一个 register 数据
        contest_details = ContestDetail.objects.filter(id=data.__getitem__('id'))
        print(contest_details.__len__())
        if contest_details.__len__() > 0:
            temp_contest_detail = {}
        else:
            contest_detail.save()
            temp_contest_detail = {
                "id": contest_detail.id,
                "contestTitle": contest_detail.contest_title,
                "organizer": {
                    "id": contest_detail.organizer.id,
                    "user": {
                        "id": contest_detail.organizer.user.id,
                        "account": contest_detail.organizer.user.account,
                        "phone": contest_detail.organizer.user.phone,
                        "password": contest_detail.organizer.user.password,
                        "name": contest_detail.organizer.user.name,
                        "type": contest_detail.organizer.user.type,
                    },
                    "email": contest_detail.organizer.email,
                    "school": contest_detail.organizer.school,
                    "establishDate": contest_detail.organizer.establish_date,
                    "schoolType": contest_detail.organizer.school_type,
                    "schoolRunningType": contest_detail.organizer.school_running_type,
                    "idImg": contest_detail.organizer.id_img,
                },
                "contestContent": contest_detail.contest_content,
                "signUpStartTime": contest_detail.sign_up_start_time,
                "signUpEndTime": contest_detail.sign_up_end_time,
                "publishTime": contest_detail.publish_time,
                "place": contest_detail.place,
                "holdDate": contest_detail.hold_date,
                "holdStartTime": contest_detail.hold_start_time,
                "holdEndTime": contest_detail.hold_end_time,
                "type": contest_detail.type,
                "upperLimit": contest_detail.upper_limit,
                "state": contest_detail.state,
            }
        res = temp_contest_detail
        # res = {
        #     "code": 200,
        #     "data": temp_contest_detail
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def update_contest_detail(request):
    try:
        data = json.loads(request.body)
        # 获取一个 register 数据
        contest_details = ContestDetail.objects.filter(id=data.__getitem__('id'))
        print(contest_details.__len__())
        if contest_details.__len__() > 0:
            contest_details.update(
                contest_title=data.__getitem__('contestTitle'),
                organizer_id=data.__getitem__('organizer').__getitem__('id'),
                contest_content=data.__getitem__('contestContent'),
                sign_up_start_time=data.__getitem__('signUpStartTime'),
                sign_up_end_time=data.__getitem__('signUpEndTime'),
                publish_time=data.__getitem__('publishTime'),
                place=data.__getitem__('place'),
                hold_date=data.__getitem__('holdDate'),
                hold_start_time=data.__getitem__('holdStartTime'),
                hold_end_time=data.__getitem__('holdEndTime'),
                type=data.__getitem__('type'),
                upper_limit=data.__getitem__('upperLimit'),
                state=data.__getitem__('state'),
            )
            temp_contest_detail = {
                "id": contest_details[0].id,
                "contestTitle": contest_details[0].contest_title,
                "organizer": {
                    "id": contest_details[0].organizer.id,
                    "user": {
                        "id": contest_details[0].organizer.user.id,
                        "account": contest_details[0].organizer.user.account,
                        "phone": contest_details[0].organizer.user.phone,
                        "password": contest_details[0].organizer.user.password,
                        "name": contest_details[0].organizer.user.name,
                        "type": contest_details[0].organizer.user.type,
                    },
                    "email": contest_details[0].organizer.email,
                    "school": contest_details[0].organizer.school,
                    "establishDate": contest_details[0].organizer.establish_date,
                    "schoolType": contest_details[0].organizer.school_type,
                    "schoolRunningType": contest_details[0].organizer.school_running_type,
                    "idImg": contest_details[0].organizer.id_img,
                },
                "contestContent": contest_details[0].contest_content,
                "signUpStartTime": contest_details[0].sign_up_start_time,
                "signUpEndTime": contest_details[0].sign_up_end_time,
                "publishTime": contest_details[0].publish_time,
                "place": contest_details[0].place,
                "holdDate": contest_details[0].hold_date,
                "holdStartTime": contest_details[0].hold_start_time,
                "holdEndTime": contest_details[0].hold_end_time,
                "type": contest_details[0].type,
                "upperLimit": contest_details[0].upper_limit,
                "state": contest_details[0].state,
            }
        else:
            temp_contest_detail = {}
        res = temp_contest_detail
        # res = {
        #     "code": 200,
        #     "data": temp_contest_detail
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def delete_contest_detail(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        contest_details = ContestDetail.objects.filter(id=data.__getitem__('id'))
        print(contest_details.__len__())
        if contest_details.__len__() > 0:
            contest_details.delete()
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
