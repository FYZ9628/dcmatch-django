from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt

from user.models import User
from .models import Teacher
from student.serializers import StudentSerializer

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


def get_all_teacher(request):
    try:
        # 获取所有 user 数据
        teachers = Teacher.objects.all()  # 获取全部列表
        teachers_list = []
        for teacher in teachers:
            temp_teacher = {
                "id": teacher.id,
                "user": {
                    "id": teacher.user.id,
                    "account": teacher.user.account,
                    "phone": teacher.user.phone,
                    "password": teacher.user.password,
                    "name": teacher.user.name,
                    "type": teacher.user.type
                },
                "sex": teacher.sex,
                "email": teacher.email,
                "school": teacher.school,
                "entryDate": teacher.entry_date,
                "academy": teacher.academy,
                "professionalTitle": teacher.professional_title,
                "education": teacher.education,
                "idImg": teacher.id_img,
            }
            teachers_list.append(temp_teacher)
        # serializer = StudentSerializer(students, many=True)
        res = teachers_list
        # res = {
        #     "code": 200,
        #     "data": teachers_list
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
def search_teacher(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        teachers = Teacher.objects.filter(Q(user__name__icontains=data.__getitem__('keywords')) |
                                          Q(user__account__icontains=data.__getitem__('keywords')))
        teachers_list = []
        for teacher in teachers:
            temp_teacher = {
                "id": teacher.id,
                "user": {
                    "id": teacher.user.id,
                    "account": teacher.user.account,
                    "phone": teacher.user.phone,
                    "password": teacher.user.password,
                    "name": teacher.user.name,
                    "type": teacher.user.type
                },
                "sex": teacher.sex,
                "email": teacher.email,
                "school": teacher.school,
                "entryDate": teacher.entry_date,
                "academy": teacher.academy,
                "professionalTitle": teacher.professional_title,
                "education": teacher.education,
                "idImg": teacher.id_img,
            }
            teachers_list.append(temp_teacher)
        # serializer = StudentSerializer(students, many=True)
        res = teachers_list
        # res = {
        #     "code": 200,
        #     "data": teachers_list
        #     # "data": serializer.data
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def search_teacher_by_account(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        teachers = Teacher.objects.filter(user__account=data.__getitem__('keywords'))
        if teachers.__len__() >= 1:
            temp_teacher = {
                "id": teachers[0].id,
                "user": {
                    "id": teachers[0].user.id,
                    "account": teachers[0].user.account,
                    "phone": teachers[0].user.phone,
                    "password": teachers[0].user.password,
                    "name": teachers[0].user.name,
                    "type": teachers[0].user.type
                },
                "sex": teachers[0].sex,
                "email": teachers[0].email,
                "school": teachers[0].school,
                "entryDate": teachers[0].entry_date,
                "academy": teachers[0].academy,
                "professionalTitle": teachers[0].professional_title,
                "education": teachers[0].education,
                "idImg": teachers[0].id_img,
            }
        else:
            temp_teacher = {}
        res = temp_teacher
        # res = {
        #     "code": 200,
        #     "data": temp_teacher
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def add_teacher(request):
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
            temp_teacher = {}
        else:
            # 先在 user 表中添加一条数据
            user.save()
            teacher = Teacher(
                user_id=user.id,
                sex=data.__getitem__('sex'),
                email=data.__getitem__('email'),
                school=data.__getitem__('school'),
                entry_date=data.__getitem__('entryDate'),
                academy=data.__getitem__('academy'),
                professional_title=data.__getitem__('professionalTitle'),
                education=data.__getitem__('education'),
                id_img=data.__getitem__('idImg'),
            )
            # 再在 student 表中添加一条数据
            teacher.save()
            temp_teacher = {
                "id": teacher.id,
                "user": {
                    "id": user.id,
                    "account": user.account,
                    "phone": user.phone,
                    "password": user.password,
                    "name": user.name,
                    "type": user.type
                },
                "sex": teacher.sex,
                "email": teacher.email,
                "school": teacher.school,
                "entryDate": teacher.entry_date,
                "academy": teacher.academy,
                "professionalTitle": teacher.professional_title,
                "education": teacher.education,
                "idImg": teacher.id_img,
            }
        res = temp_teacher
        # res = {
        #     "code": 200,
        #     "data": temp_teacher
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def update_teacher(request):
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
            teachers = Teacher.objects.filter(user_id=users[0].id)
            teachers.update(
                sex=data.__getitem__('sex'),
                email=data.__getitem__('email'),
                school=data.__getitem__('school'),
                entry_date=data.__getitem__('entryDate'),
                academy=data.__getitem__('academy'),
                professional_title=data.__getitem__('professionalTitle'),
                education=data.__getitem__('education'),
                id_img=data.__getitem__('idImg'),
            )
            temp_teacher = {
                "id": teachers[0].id,
                "user": {
                    "id": users[0].id,
                    "account": users[0].account,
                    "phone": users[0].phone,
                    "password": users[0].password,
                    "name": users[0].name,
                    "type": users[0].type
                },
                "sex": teachers[0].sex,
                "email": teachers[0].email,
                "school": teachers[0].school,
                "entryDate": teachers[0].entry_date,
                "academy": teachers[0].academy,
                "professionalTitle": teachers[0].professional_title,
                "education": teachers[0].education,
                "idImg": teachers[0].id_img,
            }
        else:
            temp_teacher = {}
        res = temp_teacher
        # res = {
        #     "code": 200,
        #     "data": temp_teacher
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def delete_teacher(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        # users = User.objects.filter(account=user.account)
        teachers = Teacher.objects.filter(id=data.__getitem__('id'))
        print(teachers.__len__())
        if teachers.__len__() > 0:
            users = User.objects.filter(id=teachers[0].user.id)
            teachers.delete()
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
