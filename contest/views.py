from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from contest.serializers import CJsonEncoder
from .models import Contest

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


def get_all_contest(request):
    try:
        # 获取所有 user 数据
        contests = Contest.objects.all()  # 获取全部列表
        contests_list = []
        for contest_1 in contests:
            temp_contest = {
                "id": contest_1.id,
                "contestDetail": {
                    "id": contest_1.contest.id,
                    "contestTitle": contest_1.contest.contest_title,
                    "organizer": {
                        "id": contest_1.contest.organizer.id,
                        "user": {
                            "id": contest_1.contest.organizer.user.id,
                            "account": contest_1.contest.organizer.user.account,
                            "phone": contest_1.contest.organizer.user.phone,
                            "password": contest_1.contest.organizer.user.password,
                            "name": contest_1.contest.organizer.user.name,
                            "type": contest_1.contest.organizer.user.type
                        },
                        "email": contest_1.contest.organizer.email,
                        "school": contest_1.contest.organizer.school,
                        "establishDate": contest_1.contest.organizer.establish_date,
                        "schoolType": contest_1.contest.organizer.school_type,
                        "schoolRunningType": contest_1.contest.organizer.school_running_type,
                        "idImg": contest_1.contest.organizer.id_img
                    },
                    "contestContent": contest_1.contest.contest_content,
                    "signUpStartTime": contest_1.contest.sign_up_start_time,
                    "signUpEndTime": contest_1.contest.sign_up_end_time,
                    "publishTime": contest_1.contest.publish_time,
                    "place": contest_1.contest.place,
                    "holdDate": contest_1.contest.hold_date,
                    "holdStartTime": contest_1.contest.hold_start_time,
                    "holdEndTime": contest_1.contest.hold_end_time,
                    "type": contest_1.contest.type,
                    "upperLimit": contest_1.contest.upper_limit,
                    "state": contest_1.contest.state
                },
                "student": {
                    "id": contest_1.student.id,
                    "user": {
                        "id": contest_1.student.user.id,
                        "account": contest_1.student.user.account,
                        "phone": contest_1.student.user.phone,
                        "password": contest_1.student.user.password,
                        "name": contest_1.student.user.name,
                        "type": contest_1.student.user.type
                    },
                    "sex": contest_1.student.sex,
                    "email": contest_1.student.email,
                    "school": contest_1.student.school,
                    "admissionDate": contest_1.student.admission_date,
                    "graduationDate": contest_1.student.graduation_date,
                    "academy": contest_1.student.academy,
                    "major": contest_1.student.major,
                    "education": contest_1.student.education,
                    "idImg": contest_1.student.id_img
                },
                "state": contest_1.state,
                "ticketNumber": contest_1.ticket_number,
                "score": contest_1.score
            }
            contests_list.append(temp_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": contests_list
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
def search_all_contest_by_student_account(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        contests = Contest.objects.filter(student__user__account=data.__getitem__('keywords'))
        contests_list = []
        for contest_1 in contests:
            temp_contest = {
                "id": contest_1.id,
                "contestDetail": {
                    "id": contest_1.contest.id,
                    "contestTitle": contest_1.contest.contest_title,
                    "organizer": {
                        "id": contest_1.contest.organizer.id,
                        "user": {
                            "id": contest_1.contest.organizer.user.id,
                            "account": contest_1.contest.organizer.user.account,
                            "phone": contest_1.contest.organizer.user.phone,
                            "password": contest_1.contest.organizer.user.password,
                            "name": contest_1.contest.organizer.user.name,
                            "type": contest_1.contest.organizer.user.type
                        },
                        "email": contest_1.contest.organizer.email,
                        "school": contest_1.contest.organizer.school,
                        "establishDate": contest_1.contest.organizer.establish_date,
                        "schoolType": contest_1.contest.organizer.school_type,
                        "schoolRunningType": contest_1.contest.organizer.school_running_type,
                        "idImg": contest_1.contest.organizer.id_img
                    },
                    "contestContent": contest_1.contest.contest_content,
                    "signUpStartTime": contest_1.contest.sign_up_start_time,
                    "signUpEndTime": contest_1.contest.sign_up_end_time,
                    "publishTime": contest_1.contest.publish_time,
                    "place": contest_1.contest.place,
                    "holdDate": contest_1.contest.hold_date,
                    "holdStartTime": contest_1.contest.hold_start_time,
                    "holdEndTime": contest_1.contest.hold_end_time,
                    "type": contest_1.contest.type,
                    "upperLimit": contest_1.contest.upper_limit,
                    "state": contest_1.contest.state
                },
                "student": {
                    "id": contest_1.student.id,
                    "user": {
                        "id": contest_1.student.user.id,
                        "account": contest_1.student.user.account,
                        "phone": contest_1.student.user.phone,
                        "password": contest_1.student.user.password,
                        "name": contest_1.student.user.name,
                        "type": contest_1.student.user.type
                    },
                    "sex": contest_1.student.sex,
                    "email": contest_1.student.email,
                    "school": contest_1.student.school,
                    "admissionDate": contest_1.student.admission_date,
                    "graduationDate": contest_1.student.graduation_date,
                    "academy": contest_1.student.academy,
                    "major": contest_1.student.major,
                    "education": contest_1.student.education,
                    "idImg": contest_1.student.id_img
                },
                "state": contest_1.state,
                "ticketNumber": contest_1.ticket_number,
                "score": contest_1.score
            }
            contests_list.append(temp_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": contests_list
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
def search_all_contest_by_organizer_account(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        contests = Contest.objects.filter(contest__organizer__user__account=data.__getitem__('keywords'))
        contests_list = []
        for contest_1 in contests:
            temp_contest = {
                "id": contest_1.id,
                "contestDetail": {
                    "id": contest_1.contest.id,
                    "contestTitle": contest_1.contest.contest_title,
                    "organizer": {
                        "id": contest_1.contest.organizer.id,
                        "user": {
                            "id": contest_1.contest.organizer.user.id,
                            "account": contest_1.contest.organizer.user.account,
                            "phone": contest_1.contest.organizer.user.phone,
                            "password": contest_1.contest.organizer.user.password,
                            "name": contest_1.contest.organizer.user.name,
                            "type": contest_1.contest.organizer.user.type
                        },
                        "email": contest_1.contest.organizer.email,
                        "school": contest_1.contest.organizer.school,
                        "establishDate": contest_1.contest.organizer.establish_date,
                        "schoolType": contest_1.contest.organizer.school_type,
                        "schoolRunningType": contest_1.contest.organizer.school_running_type,
                        "idImg": contest_1.contest.organizer.id_img
                    },
                    "contestContent": contest_1.contest.contest_content,
                    "signUpStartTime": contest_1.contest.sign_up_start_time,
                    "signUpEndTime": contest_1.contest.sign_up_end_time,
                    "publishTime": contest_1.contest.publish_time,
                    "place": contest_1.contest.place,
                    "holdDate": contest_1.contest.hold_date,
                    "holdStartTime": contest_1.contest.hold_start_time,
                    "holdEndTime": contest_1.contest.hold_end_time,
                    "type": contest_1.contest.type,
                    "upperLimit": contest_1.contest.upper_limit,
                    "state": contest_1.contest.state
                },
                "student": {
                    "id": contest_1.student.id,
                    "user": {
                        "id": contest_1.student.user.id,
                        "account": contest_1.student.user.account,
                        "phone": contest_1.student.user.phone,
                        "password": contest_1.student.user.password,
                        "name": contest_1.student.user.name,
                        "type": contest_1.student.user.type
                    },
                    "sex": contest_1.student.sex,
                    "email": contest_1.student.email,
                    "school": contest_1.student.school,
                    "admissionDate": contest_1.student.admission_date,
                    "graduationDate": contest_1.student.graduation_date,
                    "academy": contest_1.student.academy,
                    "major": contest_1.student.major,
                    "education": contest_1.student.education,
                    "idImg": contest_1.student.id_img
                },
                "state": contest_1.state,
                "ticketNumber": contest_1.ticket_number,
                "score": contest_1.score
            }
            contests_list.append(temp_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": contests_list
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
def search_contest_by_id(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        contests = Contest.objects.filter(id=data.__getitem__('keywords'))
        print(contests.__len__())
        if contests.__len__() >= 1:
            temp_contest = {
                "id": contests[0].id,
                "contestDetail": {
                    "id": contests[0].contest.id,
                    "contestTitle": contests[0].contest.contest_title,
                    "organizer": {
                        "id": contests[0].contest.organizer.id,
                        "user": {
                            "id": contests[0].contest.organizer.user.id,
                            "account": contests[0].contest.organizer.user.account,
                            "phone": contests[0].contest.organizer.user.phone,
                            "password": contests[0].contest.organizer.user.password,
                            "name": contests[0].contest.organizer.user.name,
                            "type": contests[0].contest.organizer.user.type
                        },
                        "email": contests[0].contest.organizer.email,
                        "school": contests[0].contest.organizer.school,
                        "establishDate": contests[0].contest.organizer.establish_date,
                        "schoolType": contests[0].contest.organizer.school_type,
                        "schoolRunningType": contests[0].contest.organizer.school_running_type,
                        "idImg": contests[0].contest.organizer.id_img
                    },
                    "contestContent": contests[0].contest.contest_content,
                    "signUpStartTime": contests[0].contest.sign_up_start_time,
                    "signUpEndTime": contests[0].contest.sign_up_end_time,
                    "publishTime": contests[0].contest.publish_time,
                    "place": contests[0].contest.place,
                    "holdDate": contests[0].contest.hold_date,
                    "holdStartTime": contests[0].contest.hold_start_time,
                    "holdEndTime": contests[0].contest.hold_end_time,
                    "type": contests[0].contest.type,
                    "upperLimit": contests[0].contest.upper_limit,
                    "state": contests[0].contest.state
                },
                "student": {
                    "id": contests[0].student.id,
                    "user": {
                        "id": contests[0].student.user.id,
                        "account": contests[0].student.user.account,
                        "phone": contests[0].student.user.phone,
                        "password": contests[0].student.user.password,
                        "name": contests[0].student.user.name,
                        "type": contests[0].student.user.type
                    },
                    "sex": contests[0].student.sex,
                    "email": contests[0].student.email,
                    "school": contests[0].student.school,
                    "admissionDate": contests[0].student.admission_date,
                    "graduationDate": contests[0].student.graduation_date,
                    "academy": contests[0].student.academy,
                    "major": contests[0].student.major,
                    "education": contests[0].student.education,
                    "idImg": contests[0].student.id_img
                },
                "state": contests[0].state,
                "ticketNumber": contests[0].ticket_number,
                "score": contests[0].score
            }
        else:
            temp_contest = {}
        res = {
            "code": 200,
            "data": temp_contest
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_all_contest_by_contest_detail_id(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        contests = Contest.objects.filter(contest__id=data.__getitem__('keywords'))
        contests_list = []
        for contest_1 in contests:
            temp_contest = {
                "id": contest_1.id,
                "contestDetail": {
                    "id": contest_1.contest.id,
                    "contestTitle": contest_1.contest.contest_title,
                    "organizer": {
                        "id": contest_1.contest.organizer.id,
                        "user": {
                            "id": contest_1.contest.organizer.user.id,
                            "account": contest_1.contest.organizer.user.account,
                            "phone": contest_1.contest.organizer.user.phone,
                            "password": contest_1.contest.organizer.user.password,
                            "name": contest_1.contest.organizer.user.name,
                            "type": contest_1.contest.organizer.user.type
                        },
                        "email": contest_1.contest.organizer.email,
                        "school": contest_1.contest.organizer.school,
                        "establishDate": contest_1.contest.organizer.establish_date,
                        "schoolType": contest_1.contest.organizer.school_type,
                        "schoolRunningType": contest_1.contest.organizer.school_running_type,
                        "idImg": contest_1.contest.organizer.id_img
                    },
                    "contestContent": contest_1.contest.contest_content,
                    "signUpStartTime": contest_1.contest.sign_up_start_time,
                    "signUpEndTime": contest_1.contest.sign_up_end_time,
                    "publishTime": contest_1.contest.publish_time,
                    "place": contest_1.contest.place,
                    "holdDate": contest_1.contest.hold_date,
                    "holdStartTime": contest_1.contest.hold_start_time,
                    "holdEndTime": contest_1.contest.hold_end_time,
                    "type": contest_1.contest.type,
                    "upperLimit": contest_1.contest.upper_limit,
                    "state": contest_1.contest.state
                },
                "student": {
                    "id": contest_1.student.id,
                    "user": {
                        "id": contest_1.student.user.id,
                        "account": contest_1.student.user.account,
                        "phone": contest_1.student.user.phone,
                        "password": contest_1.student.user.password,
                        "name": contest_1.student.user.name,
                        "type": contest_1.student.user.type
                    },
                    "sex": contest_1.student.sex,
                    "email": contest_1.student.email,
                    "school": contest_1.student.school,
                    "admissionDate": contest_1.student.admission_date,
                    "graduationDate": contest_1.student.graduation_date,
                    "academy": contest_1.student.academy,
                    "major": contest_1.student.major,
                    "education": contest_1.student.education,
                    "idImg": contest_1.student.id_img
                },
                "state": contest_1.state,
                "ticketNumber": contest_1.ticket_number,
                "score": contest_1.score
            }
            contests_list.append(temp_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": contests_list
            # "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def add_contest(request):
    try:
        data = json.loads(request.body)
        contest_1 = Contest(
            contest_id=data.__getitem__('contestDetail').__getitem__('id'),
            student_id=data.__getitem__('student').__getitem__('id'),
            state=data.__getitem__('state'),
            ticket_number=data.__getitem__('ticketNumber'),
            score=data.__getitem__('score')
        )
        # 获取一个 register 数据
        contests = Contest.objects.filter(id=data.__getitem__('id'))
        print(contests.__len__())
        if contests.__len__() > 0:
            temp_contest = {}
        else:
            contest_1.save()
            temp_contest = {
                "id": contest_1.id,
                "contestDetail": {
                    "id": contest_1.contest.id,
                    "contestTitle": contest_1.contest.contest_title,
                    "organizer": {
                        "id": contest_1.contest.organizer.id,
                        "user": {
                            "id": contest_1.contest.organizer.user.id,
                            "account": contest_1.contest.organizer.user.account,
                            "phone": contest_1.contest.organizer.user.phone,
                            "password": contest_1.contest.organizer.user.password,
                            "name": contest_1.contest.organizer.user.name,
                            "type": contest_1.contest.organizer.user.type
                        },
                        "email": contest_1.contest.organizer.email,
                        "school": contest_1.contest.organizer.school,
                        "establishDate": contest_1.contest.organizer.establish_date,
                        "schoolType": contest_1.contest.organizer.school_type,
                        "schoolRunningType": contest_1.contest.organizer.school_running_type,
                        "idImg": contest_1.contest.organizer.id_img
                    },
                    "contestContent": contest_1.contest.contest_content,
                    "signUpStartTime": contest_1.contest.sign_up_start_time,
                    "signUpEndTime": contest_1.contest.sign_up_end_time,
                    "publishTime": contest_1.contest.publish_time,
                    "place": contest_1.contest.place,
                    "holdDate": contest_1.contest.hold_date,
                    "holdStartTime": contest_1.contest.hold_start_time,
                    "holdEndTime": contest_1.contest.hold_end_time,
                    "type": contest_1.contest.type,
                    "upperLimit": contest_1.contest.upper_limit,
                    "state": contest_1.contest.state
                },
                "student": {
                    "id": contest_1.student.id,
                    "user": {
                        "id": contest_1.student.user.id,
                        "account": contest_1.student.user.account,
                        "phone": contest_1.student.user.phone,
                        "password": contest_1.student.user.password,
                        "name": contest_1.student.user.name,
                        "type": contest_1.student.user.type
                    },
                    "sex": contest_1.student.sex,
                    "email": contest_1.student.email,
                    "school": contest_1.student.school,
                    "admissionDate": contest_1.student.admission_date,
                    "graduationDate": contest_1.student.graduation_date,
                    "academy": contest_1.student.academy,
                    "major": contest_1.student.major,
                    "education": contest_1.student.education,
                    "idImg": contest_1.student.id_img
                },
                "state": contest_1.state,
                "ticketNumber": contest_1.ticket_number,
                "score": contest_1.score
            }
        res = {
            "code": 200,
            "data": temp_contest
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def update_contest(request):
    try:
        data = json.loads(request.body)
        # 获取一个 register 数据
        contests = Contest.objects.filter(id=data.__getitem__('id'))
        print(contests.__len__())
        if contests.__len__() > 0:
            contests.update(
                contest_id=data.__getitem__('contestDetail').__getitem__('id'),
                student_id=data.__getitem__('student').__getitem__('id'),
                state=data.__getitem__('state'),
                ticket_number=data.__getitem__('ticketNumber'),
                score=data.__getitem__('score')
            )
            temp_contest = {
                "id": contests[0].id,
                "contestDetail": {
                    "id": contests[0].contest.id,
                    "contestTitle": contests[0].contest.contest_title,
                    "organizer": {
                        "id": contests[0].contest.organizer.id,
                        "user": {
                            "id": contests[0].contest.organizer.user.id,
                            "account": contests[0].contest.organizer.user.account,
                            "phone": contests[0].contest.organizer.user.phone,
                            "password": contests[0].contest.organizer.user.password,
                            "name": contests[0].contest.organizer.user.name,
                            "type": contests[0].contest.organizer.user.type
                        },
                        "email": contests[0].contest.organizer.email,
                        "school": contests[0].contest.organizer.school,
                        "establishDate": contests[0].contest.organizer.establish_date,
                        "schoolType": contests[0].contest.organizer.school_type,
                        "schoolRunningType": contests[0].contest.organizer.school_running_type,
                        "idImg": contests[0].contest.organizer.id_img
                    },
                    "contestContent": contests[0].contest.contest_content,
                    "signUpStartTime": contests[0].contest.sign_up_start_time,
                    "signUpEndTime": contests[0].contest.sign_up_end_time,
                    "publishTime": contests[0].contest.publish_time,
                    "place": contests[0].contest.place,
                    "holdDate": contests[0].contest.hold_date,
                    "holdStartTime": contests[0].contest.hold_start_time,
                    "holdEndTime": contests[0].contest.hold_end_time,
                    "type": contests[0].contest.type,
                    "upperLimit": contests[0].contest.upper_limit,
                    "state": contests[0].contest.state
                },
                "student": {
                    "id": contests[0].student.id,
                    "user": {
                        "id": contests[0].student.user.id,
                        "account": contests[0].student.user.account,
                        "phone": contests[0].student.user.phone,
                        "password": contests[0].student.user.password,
                        "name": contests[0].student.user.name,
                        "type": contests[0].student.user.type
                    },
                    "sex": contests[0].student.sex,
                    "email": contests[0].student.email,
                    "school": contests[0].student.school,
                    "admissionDate": contests[0].student.admission_date,
                    "graduationDate": contests[0].student.graduation_date,
                    "academy": contests[0].student.academy,
                    "major": contests[0].student.major,
                    "education": contests[0].student.education,
                    "idImg": contests[0].student.id_img
                },
                "state": contests[0].state,
                "ticketNumber": contests[0].ticket_number,
                "score": contests[0].score
            }
        else:
            temp_contest = {}
        res = {
            "code": 200,
            "data": temp_contest
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def delete_contest(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        contests = Contest.objects.filter(id=data.__getitem__('id'))
        print(contests.__len__())
        if contests.__len__() > 0:
            contests.delete()
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
