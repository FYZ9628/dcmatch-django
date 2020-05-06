from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from team_contest.serializers import CJsonEncoder
from .models import TeamContest

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


def get_all_team_contest(request):
    try:
        # 获取所有 user 数据
        team_contests = TeamContest.objects.all()  # 获取全部列表
        team_contests_list = []
        for team_contest in team_contests:
            temp_team_contest = {
                "id": team_contest.id,
                "contestDetail": {
                    "id": team_contest.contest.id,
                    "contestTitle": team_contest.contest.contest_title,
                    "organizer": {
                        "id": team_contest.contest.organizer.id,
                        "user": {
                            "id": team_contest.contest.organizer.user.id,
                            "account": team_contest.contest.organizer.user.account,
                            "phone": team_contest.contest.organizer.user.phone,
                            "password": team_contest.contest.organizer.user.password,
                            "name": team_contest.contest.organizer.user.name,
                            "type": team_contest.contest.organizer.user.type
                        },
                        "email": team_contest.contest.organizer.email,
                        "school": team_contest.contest.organizer.school,
                        "establishDate": team_contest.contest.organizer.establish_date,
                        "schoolType": team_contest.contest.organizer.school_type,
                        "schoolRunningType": team_contest.contest.organizer.school_running_type,
                        "idImg": team_contest.contest.organizer.id_img
                    },
                    "contestContent": team_contest.contest.contest_content,
                    "signUpStartTime": team_contest.contest.sign_up_start_time,
                    "signUpEndTime": team_contest.contest.sign_up_end_time,
                    "publishTime": team_contest.contest.publish_time,
                    "place": team_contest.contest.place,
                    "holdDate": team_contest.contest.hold_date,
                    "holdStartTime": team_contest.contest.hold_start_time,
                    "holdEndTime": team_contest.contest.hold_end_time,
                    "type": team_contest.contest.type,
                    "upperLimit": team_contest.contest.upper_limit,
                    "state": team_contest.contest.state
                },
                "student": {
                    "id": team_contest.student.id,
                    "user": {
                        "id": team_contest.student.user.id,
                        "account": team_contest.student.user.account,
                        "phone": team_contest.student.user.phone,
                        "password": team_contest.student.user.password,
                        "name": team_contest.student.user.name,
                        "type": team_contest.student.user.type
                    },
                    "sex": team_contest.student.sex,
                    "email": team_contest.student.email,
                    "school": team_contest.student.school,
                    "admissionDate": team_contest.student.admission_date,
                    "graduationDate": team_contest.student.graduation_date,
                    "academy": team_contest.student.academy,
                    "major": team_contest.student.major,
                    "education": team_contest.student.education,
                    "idImg": team_contest.student.id_img
                },
                "teacherAccount": team_contest.teacher_account,
                "teacherName": team_contest.teacher_name,
                "state": team_contest.state,
                "ticketNumber": team_contest.ticket_number,
                "score": team_contest.score,
                "teamName": team_contest.team_name,
                "remarks": team_contest.remarks
            }
            team_contests_list.append(temp_team_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": team_contests_list
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
def search_all_team_contest_by_student_account(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        team_contests = TeamContest.objects.filter(student__user__account=data.__getitem__('keywords'))
        team_contests_list = []
        for team_contest in team_contests:
            temp_team_contest = {
                "id": team_contest.id,
                "contestDetail": {
                    "id": team_contest.contest.id,
                    "contestTitle": team_contest.contest.contest_title,
                    "organizer": {
                        "id": team_contest.contest.organizer.id,
                        "user": {
                            "id": team_contest.contest.organizer.user.id,
                            "account": team_contest.contest.organizer.user.account,
                            "phone": team_contest.contest.organizer.user.phone,
                            "password": team_contest.contest.organizer.user.password,
                            "name": team_contest.contest.organizer.user.name,
                            "type": team_contest.contest.organizer.user.type
                        },
                        "email": team_contest.contest.organizer.email,
                        "school": team_contest.contest.organizer.school,
                        "establishDate": team_contest.contest.organizer.establish_date,
                        "schoolType": team_contest.contest.organizer.school_type,
                        "schoolRunningType": team_contest.contest.organizer.school_running_type,
                        "idImg": team_contest.contest.organizer.id_img
                    },
                    "contestContent": team_contest.contest.contest_content,
                    "signUpStartTime": team_contest.contest.sign_up_start_time,
                    "signUpEndTime": team_contest.contest.sign_up_end_time,
                    "publishTime": team_contest.contest.publish_time,
                    "place": team_contest.contest.place,
                    "holdDate": team_contest.contest.hold_date,
                    "holdStartTime": team_contest.contest.hold_start_time,
                    "holdEndTime": team_contest.contest.hold_end_time,
                    "type": team_contest.contest.type,
                    "upperLimit": team_contest.contest.upper_limit,
                    "state": team_contest.contest.state
                },
                "student": {
                    "id": team_contest.student.id,
                    "user": {
                        "id": team_contest.student.user.id,
                        "account": team_contest.student.user.account,
                        "phone": team_contest.student.user.phone,
                        "password": team_contest.student.user.password,
                        "name": team_contest.student.user.name,
                        "type": team_contest.student.user.type
                    },
                    "sex": team_contest.student.sex,
                    "email": team_contest.student.email,
                    "school": team_contest.student.school,
                    "admissionDate": team_contest.student.admission_date,
                    "graduationDate": team_contest.student.graduation_date,
                    "academy": team_contest.student.academy,
                    "major": team_contest.student.major,
                    "education": team_contest.student.education,
                    "idImg": team_contest.student.id_img
                },
                "teacherAccount": team_contest.teacher_account,
                "teacherName": team_contest.teacher_name,
                "state": team_contest.state,
                "ticketNumber": team_contest.ticket_number,
                "score": team_contest.score,
                "teamName": team_contest.team_name,
                "remarks": team_contest.remarks
            }
            team_contests_list.append(temp_team_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": team_contests_list
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
def search_all_team_contest_by_teacher_account(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        team_contests = TeamContest.objects.filter(teacher_account=data.__getitem__('keywords'))
        team_contests_list = []
        for team_contest in team_contests:
            temp_team_contest = {
                "id": team_contest.id,
                "contestDetail": {
                    "id": team_contest.contest.id,
                    "contestTitle": team_contest.contest.contest_title,
                    "organizer": {
                        "id": team_contest.contest.organizer.id,
                        "user": {
                            "id": team_contest.contest.organizer.user.id,
                            "account": team_contest.contest.organizer.user.account,
                            "phone": team_contest.contest.organizer.user.phone,
                            "password": team_contest.contest.organizer.user.password,
                            "name": team_contest.contest.organizer.user.name,
                            "type": team_contest.contest.organizer.user.type
                        },
                        "email": team_contest.contest.organizer.email,
                        "school": team_contest.contest.organizer.school,
                        "establishDate": team_contest.contest.organizer.establish_date,
                        "schoolType": team_contest.contest.organizer.school_type,
                        "schoolRunningType": team_contest.contest.organizer.school_running_type,
                        "idImg": team_contest.contest.organizer.id_img
                    },
                    "contestContent": team_contest.contest.contest_content,
                    "signUpStartTime": team_contest.contest.sign_up_start_time,
                    "signUpEndTime": team_contest.contest.sign_up_end_time,
                    "publishTime": team_contest.contest.publish_time,
                    "place": team_contest.contest.place,
                    "holdDate": team_contest.contest.hold_date,
                    "holdStartTime": team_contest.contest.hold_start_time,
                    "holdEndTime": team_contest.contest.hold_end_time,
                    "type": team_contest.contest.type,
                    "upperLimit": team_contest.contest.upper_limit,
                    "state": team_contest.contest.state
                },
                "student": {
                    "id": team_contest.student.id,
                    "user": {
                        "id": team_contest.student.user.id,
                        "account": team_contest.student.user.account,
                        "phone": team_contest.student.user.phone,
                        "password": team_contest.student.user.password,
                        "name": team_contest.student.user.name,
                        "type": team_contest.student.user.type
                    },
                    "sex": team_contest.student.sex,
                    "email": team_contest.student.email,
                    "school": team_contest.student.school,
                    "admissionDate": team_contest.student.admission_date,
                    "graduationDate": team_contest.student.graduation_date,
                    "academy": team_contest.student.academy,
                    "major": team_contest.student.major,
                    "education": team_contest.student.education,
                    "idImg": team_contest.student.id_img
                },
                "teacherAccount": team_contest.teacher_account,
                "teacherName": team_contest.teacher_name,
                "state": team_contest.state,
                "ticketNumber": team_contest.ticket_number,
                "score": team_contest.score,
                "teamName": team_contest.team_name,
                "remarks": team_contest.remarks
            }
            team_contests_list.append(temp_team_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": team_contests_list
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
def search_all_team_contest_by_organizer_account(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        team_contests = TeamContest.objects.filter(
            contest__organizer__user__account=data.__getitem__('keywords')
        )
        team_contests_list = []
        for team_contest in team_contests:
            temp_team_contest = {
                "id": team_contest.id,
                "contestDetail": {
                    "id": team_contest.contest.id,
                    "contestTitle": team_contest.contest.contest_title,
                    "organizer": {
                        "id": team_contest.contest.organizer.id,
                        "user": {
                            "id": team_contest.contest.organizer.user.id,
                            "account": team_contest.contest.organizer.user.account,
                            "phone": team_contest.contest.organizer.user.phone,
                            "password": team_contest.contest.organizer.user.password,
                            "name": team_contest.contest.organizer.user.name,
                            "type": team_contest.contest.organizer.user.type
                        },
                        "email": team_contest.contest.organizer.email,
                        "school": team_contest.contest.organizer.school,
                        "establishDate": team_contest.contest.organizer.establish_date,
                        "schoolType": team_contest.contest.organizer.school_type,
                        "schoolRunningType": team_contest.contest.organizer.school_running_type,
                        "idImg": team_contest.contest.organizer.id_img
                    },
                    "contestContent": team_contest.contest.contest_content,
                    "signUpStartTime": team_contest.contest.sign_up_start_time,
                    "signUpEndTime": team_contest.contest.sign_up_end_time,
                    "publishTime": team_contest.contest.publish_time,
                    "place": team_contest.contest.place,
                    "holdDate": team_contest.contest.hold_date,
                    "holdStartTime": team_contest.contest.hold_start_time,
                    "holdEndTime": team_contest.contest.hold_end_time,
                    "type": team_contest.contest.type,
                    "upperLimit": team_contest.contest.upper_limit,
                    "state": team_contest.contest.state
                },
                "student": {
                    "id": team_contest.student.id,
                    "user": {
                        "id": team_contest.student.user.id,
                        "account": team_contest.student.user.account,
                        "phone": team_contest.student.user.phone,
                        "password": team_contest.student.user.password,
                        "name": team_contest.student.user.name,
                        "type": team_contest.student.user.type
                    },
                    "sex": team_contest.student.sex,
                    "email": team_contest.student.email,
                    "school": team_contest.student.school,
                    "admissionDate": team_contest.student.admission_date,
                    "graduationDate": team_contest.student.graduation_date,
                    "academy": team_contest.student.academy,
                    "major": team_contest.student.major,
                    "education": team_contest.student.education,
                    "idImg": team_contest.student.id_img
                },
                "teacherAccount": team_contest.teacher_account,
                "teacherName": team_contest.teacher_name,
                "state": team_contest.state,
                "ticketNumber": team_contest.ticket_number,
                "score": team_contest.score,
                "teamName": team_contest.team_name,
                "remarks": team_contest.remarks
            }
            team_contests_list.append(temp_team_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": team_contests_list
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
def search_team_contest_by_id(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        team_contests = TeamContest.objects.filter(id=data.__getitem__('keywords'))
        print(team_contests.__len__())
        if team_contests.__len__() >= 1:
            temp_team_contest = {
                "id": team_contests[0].id,
                "contestDetail": {
                    "id": team_contests[0].contest.id,
                    "contestTitle": team_contests[0].contest.contest_title,
                    "organizer": {
                        "id": team_contests[0].contest.organizer.id,
                        "user": {
                            "id": team_contests[0].contest.organizer.user.id,
                            "account": team_contests[0].contest.organizer.user.account,
                            "phone": team_contests[0].contest.organizer.user.phone,
                            "password": team_contests[0].contest.organizer.user.password,
                            "name": team_contests[0].contest.organizer.user.name,
                            "type": team_contests[0].contest.organizer.user.type
                        },
                        "email": team_contests[0].contest.organizer.email,
                        "school": team_contests[0].contest.organizer.school,
                        "establishDate": team_contests[0].contest.organizer.establish_date,
                        "schoolType": team_contests[0].contest.organizer.school_type,
                        "schoolRunningType": team_contests[0].contest.organizer.school_running_type,
                        "idImg": team_contests[0].contest.organizer.id_img
                    },
                    "contestContent": team_contests[0].contest.contest_content,
                    "signUpStartTime": team_contests[0].contest.sign_up_start_time,
                    "signUpEndTime": team_contests[0].contest.sign_up_end_time,
                    "publishTime": team_contests[0].contest.publish_time,
                    "place": team_contests[0].contest.place,
                    "holdDate": team_contests[0].contest.hold_date,
                    "holdStartTime": team_contests[0].contest.hold_start_time,
                    "holdEndTime": team_contests[0].contest.hold_end_time,
                    "type": team_contests[0].contest.type,
                    "upperLimit": team_contests[0].contest.upper_limit,
                    "state": team_contests[0].contest.state
                },
                "student": {
                    "id": team_contests[0].student.id,
                    "user": {
                        "id": team_contests[0].student.user.id,
                        "account": team_contests[0].student.user.account,
                        "phone": team_contests[0].student.user.phone,
                        "password": team_contests[0].student.user.password,
                        "name": team_contests[0].student.user.name,
                        "type": team_contests[0].student.user.type
                    },
                    "sex": team_contests[0].student.sex,
                    "email": team_contests[0].student.email,
                    "school": team_contests[0].student.school,
                    "admissionDate": team_contests[0].student.admission_date,
                    "graduationDate": team_contests[0].student.graduation_date,
                    "academy": team_contests[0].student.academy,
                    "major": team_contests[0].student.major,
                    "education": team_contests[0].student.education,
                    "idImg": team_contests[0].student.id_img
                },
                "teacherAccount": team_contests[0].teacher_account,
                "teacherName": team_contests[0].teacher_name,
                "state": team_contests[0].state,
                "ticketNumber": team_contests[0].ticket_number,
                "score": team_contests[0].score,
                "teamName": team_contests[0].team_name,
                "remarks": team_contests[0].remarks
            }
        else:
            temp_team_contest = {}
        res = {
            "code": 200,
            "data": temp_team_contest
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


# post 需要加，get请求不用加
@csrf_exempt
def search_all_team_contest_by_team_name(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        team_contests = TeamContest.objects.filter(team_name=data.__getitem__('keywords'))
        team_contests_list = []
        for team_contest in team_contests:
            temp_team_contest = {
                "id": team_contest.id,
                "contestDetail": {
                    "id": team_contest.contest.id,
                    "contestTitle": team_contest.contest.contest_title,
                    "organizer": {
                        "id": team_contest.contest.organizer.id,
                        "user": {
                            "id": team_contest.contest.organizer.user.id,
                            "account": team_contest.contest.organizer.user.account,
                            "phone": team_contest.contest.organizer.user.phone,
                            "password": team_contest.contest.organizer.user.password,
                            "name": team_contest.contest.organizer.user.name,
                            "type": team_contest.contest.organizer.user.type
                        },
                        "email": team_contest.contest.organizer.email,
                        "school": team_contest.contest.organizer.school,
                        "establishDate": team_contest.contest.organizer.establish_date,
                        "schoolType": team_contest.contest.organizer.school_type,
                        "schoolRunningType": team_contest.contest.organizer.school_running_type,
                        "idImg": team_contest.contest.organizer.id_img
                    },
                    "contestContent": team_contest.contest.contest_content,
                    "signUpStartTime": team_contest.contest.sign_up_start_time,
                    "signUpEndTime": team_contest.contest.sign_up_end_time,
                    "publishTime": team_contest.contest.publish_time,
                    "place": team_contest.contest.place,
                    "holdDate": team_contest.contest.hold_date,
                    "holdStartTime": team_contest.contest.hold_start_time,
                    "holdEndTime": team_contest.contest.hold_end_time,
                    "type": team_contest.contest.type,
                    "upperLimit": team_contest.contest.upper_limit,
                    "state": team_contest.contest.state
                },
                "student": {
                    "id": team_contest.student.id,
                    "user": {
                        "id": team_contest.student.user.id,
                        "account": team_contest.student.user.account,
                        "phone": team_contest.student.user.phone,
                        "password": team_contest.student.user.password,
                        "name": team_contest.student.user.name,
                        "type": team_contest.student.user.type
                    },
                    "sex": team_contest.student.sex,
                    "email": team_contest.student.email,
                    "school": team_contest.student.school,
                    "admissionDate": team_contest.student.admission_date,
                    "graduationDate": team_contest.student.graduation_date,
                    "academy": team_contest.student.academy,
                    "major": team_contest.student.major,
                    "education": team_contest.student.education,
                    "idImg": team_contest.student.id_img
                },
                "teacherAccount": team_contest.teacher_account,
                "teacherName": team_contest.teacher_name,
                "state": team_contest.state,
                "ticketNumber": team_contest.ticket_number,
                "score": team_contest.score,
                "teamName": team_contest.team_name,
                "remarks": team_contest.remarks
            }
            team_contests_list.append(temp_team_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": team_contests_list
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
def search_all_team_contest_by_team_name_and_contest_detail_id(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        team_contests = TeamContest.objects.filter(
            team_name=data.__getitem__('keywords'),
            contest__id=data.__getitem__('id')
        )
        team_contests_list = []
        for team_contest in team_contests:
            temp_team_contest = {
                "id": team_contest.id,
                "contestDetail": {
                    "id": team_contest.contest.id,
                    "contestTitle": team_contest.contest.contest_title,
                    "organizer": {
                        "id": team_contest.contest.organizer.id,
                        "user": {
                            "id": team_contest.contest.organizer.user.id,
                            "account": team_contest.contest.organizer.user.account,
                            "phone": team_contest.contest.organizer.user.phone,
                            "password": team_contest.contest.organizer.user.password,
                            "name": team_contest.contest.organizer.user.name,
                            "type": team_contest.contest.organizer.user.type
                        },
                        "email": team_contest.contest.organizer.email,
                        "school": team_contest.contest.organizer.school,
                        "establishDate": team_contest.contest.organizer.establish_date,
                        "schoolType": team_contest.contest.organizer.school_type,
                        "schoolRunningType": team_contest.contest.organizer.school_running_type,
                        "idImg": team_contest.contest.organizer.id_img
                    },
                    "contestContent": team_contest.contest.contest_content,
                    "signUpStartTime": team_contest.contest.sign_up_start_time,
                    "signUpEndTime": team_contest.contest.sign_up_end_time,
                    "publishTime": team_contest.contest.publish_time,
                    "place": team_contest.contest.place,
                    "holdDate": team_contest.contest.hold_date,
                    "holdStartTime": team_contest.contest.hold_start_time,
                    "holdEndTime": team_contest.contest.hold_end_time,
                    "type": team_contest.contest.type,
                    "upperLimit": team_contest.contest.upper_limit,
                    "state": team_contest.contest.state
                },
                "student": {
                    "id": team_contest.student.id,
                    "user": {
                        "id": team_contest.student.user.id,
                        "account": team_contest.student.user.account,
                        "phone": team_contest.student.user.phone,
                        "password": team_contest.student.user.password,
                        "name": team_contest.student.user.name,
                        "type": team_contest.student.user.type
                    },
                    "sex": team_contest.student.sex,
                    "email": team_contest.student.email,
                    "school": team_contest.student.school,
                    "admissionDate": team_contest.student.admission_date,
                    "graduationDate": team_contest.student.graduation_date,
                    "academy": team_contest.student.academy,
                    "major": team_contest.student.major,
                    "education": team_contest.student.education,
                    "idImg": team_contest.student.id_img
                },
                "teacherAccount": team_contest.teacher_account,
                "teacherName": team_contest.teacher_name,
                "state": team_contest.state,
                "ticketNumber": team_contest.ticket_number,
                "score": team_contest.score,
                "teamName": team_contest.team_name,
                "remarks": team_contest.remarks
            }
            team_contests_list.append(temp_team_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": team_contests_list
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
def search_all_team_contest_by_contest_detail_id(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        team_contests = TeamContest.objects.filter(contest__id=data.__getitem__('keywords'))
        team_contests_list = []
        for team_contest in team_contests:
            temp_team_contest = {
                "id": team_contest.id,
                "contestDetail": {
                    "id": team_contest.contest.id,
                    "contestTitle": team_contest.contest.contest_title,
                    "organizer": {
                        "id": team_contest.contest.organizer.id,
                        "user": {
                            "id": team_contest.contest.organizer.user.id,
                            "account": team_contest.contest.organizer.user.account,
                            "phone": team_contest.contest.organizer.user.phone,
                            "password": team_contest.contest.organizer.user.password,
                            "name": team_contest.contest.organizer.user.name,
                            "type": team_contest.contest.organizer.user.type
                        },
                        "email": team_contest.contest.organizer.email,
                        "school": team_contest.contest.organizer.school,
                        "establishDate": team_contest.contest.organizer.establish_date,
                        "schoolType": team_contest.contest.organizer.school_type,
                        "schoolRunningType": team_contest.contest.organizer.school_running_type,
                        "idImg": team_contest.contest.organizer.id_img
                    },
                    "contestContent": team_contest.contest.contest_content,
                    "signUpStartTime": team_contest.contest.sign_up_start_time,
                    "signUpEndTime": team_contest.contest.sign_up_end_time,
                    "publishTime": team_contest.contest.publish_time,
                    "place": team_contest.contest.place,
                    "holdDate": team_contest.contest.hold_date,
                    "holdStartTime": team_contest.contest.hold_start_time,
                    "holdEndTime": team_contest.contest.hold_end_time,
                    "type": team_contest.contest.type,
                    "upperLimit": team_contest.contest.upper_limit,
                    "state": team_contest.contest.state
                },
                "student": {
                    "id": team_contest.student.id,
                    "user": {
                        "id": team_contest.student.user.id,
                        "account": team_contest.student.user.account,
                        "phone": team_contest.student.user.phone,
                        "password": team_contest.student.user.password,
                        "name": team_contest.student.user.name,
                        "type": team_contest.student.user.type
                    },
                    "sex": team_contest.student.sex,
                    "email": team_contest.student.email,
                    "school": team_contest.student.school,
                    "admissionDate": team_contest.student.admission_date,
                    "graduationDate": team_contest.student.graduation_date,
                    "academy": team_contest.student.academy,
                    "major": team_contest.student.major,
                    "education": team_contest.student.education,
                    "idImg": team_contest.student.id_img
                },
                "teacherAccount": team_contest.teacher_account,
                "teacherName": team_contest.teacher_name,
                "state": team_contest.state,
                "ticketNumber": team_contest.ticket_number,
                "score": team_contest.score,
                "teamName": team_contest.team_name,
                "remarks": team_contest.remarks
            }
            team_contests_list.append(temp_team_contest)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": team_contests_list
            # "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def add_team_contest(request):
    try:
        data = json.loads(request.body)
        team_contest = TeamContest(
            contest_id=data.__getitem__('contestDetail').__getitem__('id'),
            student_id=data.__getitem__('student').__getitem__('id'),
            teacher_account=data.__getitem__('teacherAccount'),
            teacher_name=data.__getitem__('teacherName'),
            state=data.__getitem__('state'),
            ticket_number=data.__getitem__('ticketNumber'),
            score=data.__getitem__('score'),
            team_name=data.__getitem__('teamName'),
            remarks=data.__getitem__('remarks'),
        )
        # 获取一个 register 数据
        team_contests = TeamContest.objects.filter(id=data.__getitem__('id'))
        print(team_contests.__len__())
        if team_contests.__len__() > 0:
            temp_team_contest = {}
        else:
            team_contest.save()
            temp_team_contest = {
                "id": team_contest.id,
                "contestDetail": {
                    "id": team_contest.contest.id,
                    "contestTitle": team_contest.contest.contest_title,
                    "organizer": {
                        "id": team_contest.contest.organizer.id,
                        "user": {
                            "id": team_contest.contest.organizer.user.id,
                            "account": team_contest.contest.organizer.user.account,
                            "phone": team_contest.contest.organizer.user.phone,
                            "password": team_contest.contest.organizer.user.password,
                            "name": team_contest.contest.organizer.user.name,
                            "type": team_contest.contest.organizer.user.type
                        },
                        "email": team_contest.contest.organizer.email,
                        "school": team_contest.contest.organizer.school,
                        "establishDate": team_contest.contest.organizer.establish_date,
                        "schoolType": team_contest.contest.organizer.school_type,
                        "schoolRunningType": team_contest.contest.organizer.school_running_type,
                        "idImg": team_contest.contest.organizer.id_img
                    },
                    "contestContent": team_contest.contest.contest_content,
                    "signUpStartTime": team_contest.contest.sign_up_start_time,
                    "signUpEndTime": team_contest.contest.sign_up_end_time,
                    "publishTime": team_contest.contest.publish_time,
                    "place": team_contest.contest.place,
                    "holdDate": team_contest.contest.hold_date,
                    "holdStartTime": team_contest.contest.hold_start_time,
                    "holdEndTime": team_contest.contest.hold_end_time,
                    "type": team_contest.contest.type,
                    "upperLimit": team_contest.contest.upper_limit,
                    "state": team_contest.contest.state
                },
                "student": {
                    "id": team_contest.student.id,
                    "user": {
                        "id": team_contest.student.user.id,
                        "account": team_contest.student.user.account,
                        "phone": team_contest.student.user.phone,
                        "password": team_contest.student.user.password,
                        "name": team_contest.student.user.name,
                        "type": team_contest.student.user.type
                    },
                    "sex": team_contest.student.sex,
                    "email": team_contest.student.email,
                    "school": team_contest.student.school,
                    "admissionDate": team_contest.student.admission_date,
                    "graduationDate": team_contest.student.graduation_date,
                    "academy": team_contest.student.academy,
                    "major": team_contest.student.major,
                    "education": team_contest.student.education,
                    "idImg": team_contest.student.id_img
                },
                "teacherAccount": team_contest.teacher_account,
                "teacherName": team_contest.teacher_name,
                "state": team_contest.state,
                "ticketNumber": team_contest.ticket_number,
                "score": team_contest.score,
                "teamName": team_contest.team_name,
                "remarks": team_contest.remarks
            }
        res = {
            "code": 200,
            "data": temp_team_contest
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def update_team_contest(request):
    try:
        data = json.loads(request.body)
        # 获取一个 register 数据
        team_contests = TeamContest.objects.filter(id=data.__getitem__('id'))
        print(team_contests.__len__())
        if team_contests.__len__() > 0:
            team_contests.update(
                contest_id=data.__getitem__('contestDetail').__getitem__('id'),
                student_id=data.__getitem__('student').__getitem__('id'),
                teacher_account=data.__getitem__('teacherAccount'),
                teacher_name=data.__getitem__('teacherName'),
                state=data.__getitem__('state'),
                ticket_number=data.__getitem__('ticketNumber'),
                score=data.__getitem__('score'),
                team_name=data.__getitem__('teamName'),
                remarks=data.__getitem__('remarks'),
            )
            temp_team_contest = {
                "id": team_contests[0].id,
                "contestDetail": {
                    "id": team_contests[0].contest.id,
                    "contestTitle": team_contests[0].contest.contest_title,
                    "organizer": {
                        "id": team_contests[0].contest.organizer.id,
                        "user": {
                            "id": team_contests[0].contest.organizer.user.id,
                            "account": team_contests[0].contest.organizer.user.account,
                            "phone": team_contests[0].contest.organizer.user.phone,
                            "password": team_contests[0].contest.organizer.user.password,
                            "name": team_contests[0].contest.organizer.user.name,
                            "type": team_contests[0].contest.organizer.user.type
                        },
                        "email": team_contests[0].contest.organizer.email,
                        "school": team_contests[0].contest.organizer.school,
                        "establishDate": team_contests[0].contest.organizer.establish_date,
                        "schoolType": team_contests[0].contest.organizer.school_type,
                        "schoolRunningType": team_contests[0].contest.organizer.school_running_type,
                        "idImg": team_contests[0].contest.organizer.id_img
                    },
                    "contestContent": team_contests[0].contest.contest_content,
                    "signUpStartTime": team_contests[0].contest.sign_up_start_time,
                    "signUpEndTime": team_contests[0].contest.sign_up_end_time,
                    "publishTime": team_contests[0].contest.publish_time,
                    "place": team_contests[0].contest.place,
                    "holdDate": team_contests[0].contest.hold_date,
                    "holdStartTime": team_contests[0].contest.hold_start_time,
                    "holdEndTime": team_contests[0].contest.hold_end_time,
                    "type": team_contests[0].contest.type,
                    "upperLimit": team_contests[0].contest.upper_limit,
                    "state": team_contests[0].contest.state
                },
                "student": {
                    "id": team_contests[0].student.id,
                    "user": {
                        "id": team_contests[0].student.user.id,
                        "account": team_contests[0].student.user.account,
                        "phone": team_contests[0].student.user.phone,
                        "password": team_contests[0].student.user.password,
                        "name": team_contests[0].student.user.name,
                        "type": team_contests[0].student.user.type
                    },
                    "sex": team_contests[0].student.sex,
                    "email": team_contests[0].student.email,
                    "school": team_contests[0].student.school,
                    "admissionDate": team_contests[0].student.admission_date,
                    "graduationDate": team_contests[0].student.graduation_date,
                    "academy": team_contests[0].student.academy,
                    "major": team_contests[0].student.major,
                    "education": team_contests[0].student.education,
                    "idImg": team_contests[0].student.id_img
                },
                "teacherAccount": team_contests[0].teacher_account,
                "teacherName": team_contests[0].teacher_name,
                "state": team_contests[0].state,
                "ticketNumber": team_contests[0].ticket_number,
                "score": team_contests[0].score,
                "teamName": team_contests[0].team_name,
                "remarks": team_contests[0].remarks
            }
        else:
            temp_team_contest = {}
        res = {
            "code": 200,
            "data": temp_team_contest
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res, cls=CJsonEncoder), content_type="application/json")


@csrf_exempt
def delete_team_contest(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        team_contests = TeamContest.objects.filter(id=data.__getitem__('id'))
        print(team_contests.__len__())
        if team_contests.__len__() > 0:
            team_contests.delete()
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


@csrf_exempt
def delete_team_contest_by_team(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        team_contests = TeamContest.objects.filter(team_name=data.__getitem__('keywords'))
        print(team_contests.__len__())
        if team_contests.__len__() > 0:
            team_contests.delete()
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