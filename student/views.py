from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt

from user.models import User
from .models import Student
from student.serializers import StudentSerializer

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


def get_all_student(request):
    try:
        # 获取所有 user 数据
        students = Student.objects.all()  # 获取全部列表
        students_list = []
        for student in students:
            temp_student = {
                "id": student.id,
                "user": {
                    "id": student.user.id,
                    "account": student.user.account,
                    "phone": student.user.phone,
                    "password": student.user.password,
                    "name": student.user.name,
                    "type": student.user.type
                },
                "sex": student.sex,
                "email": student.email,
                "school": student.school,
                "admissionDate": student.admission_date,
                "graduationDate": student.graduation_date,
                "academy": student.academy,
                "major": student.major,
                "education": student.education,
                "idImg": student.id_img,
            }
            students_list.append(temp_student)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": students_list
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
def search_student(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        students = Student.objects.filter(Q(user__name__icontains=data.__getitem__('keywords')) |
                                          Q(user__account__icontains=data.__getitem__('keywords')))
        students_list = []
        for student in students:
            temp_student = {
                "id": student.id,
                "user": {
                    "id": student.user.id,
                    "account": student.user.account,
                    "phone": student.user.phone,
                    "password": student.user.password,
                    "name": student.user.name,
                    "type": student.user.type
                },
                "sex": student.sex,
                "email": student.email,
                "school": student.school,
                "admissionDate": student.admission_date,
                "graduationDate": student.graduation_date,
                "academy": student.academy,
                "major": student.major,
                "education": student.education,
                "idImg": student.id_img,
            }
            students_list.append(temp_student)
        # serializer = StudentSerializer(students, many=True)
        res = {
            "code": 200,
            "data": students_list
            # "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def search_student_by_account(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        students = Student.objects.filter(user__account=data.__getitem__('keywords'))
        if students.__len__() >= 1:
            temp_student = {
                "id": students[0].id,
                "user": {
                    "id": students[0].user.id,
                    "account": students[0].user.account,
                    "phone": students[0].user.phone,
                    "password": students[0].user.password,
                    "name": students[0].user.name,
                    "type": students[0].user.type
                },
                "sex": students[0].sex,
                "email": students[0].email,
                "school": students[0].school,
                "admissionDate": students[0].admission_date,
                "graduationDate": students[0].graduation_date,
                "academy": students[0].academy,
                "major": students[0].major,
                "education": students[0].education,
                "idImg": students[0].id_img,
            }
        else:
            temp_student = {}
        res = {
            "code": 200,
            "data": temp_student
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def add_student(request):
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
            temp_student = {}
        else:
            # 先在 user 表中添加一条数据
            user.save()
            student = Student(
                user_id=user.id,
                sex=data.__getitem__('sex'),
                email=data.__getitem__('email'),
                school=data.__getitem__('school'),
                admission_date=data.__getitem__('admissionDate'),
                graduation_date=data.__getitem__('graduationDate'),
                academy=data.__getitem__('academy'),
                major=data.__getitem__('major'),
                education=data.__getitem__('education'),
                id_img=data.__getitem__('idImg'),
            )
            # 再在 student 表中添加一条数据
            student.save()
            temp_student = {
                "id": student.id,
                "user": {
                    "id": user.id,
                    "account": user.account,
                    "phone": user.phone,
                    "password": user.password,
                    "name": user.name,
                    "type": user.type
                },
                "sex": student.sex,
                "email": student.email,
                "school": student.school,
                "admissionDate": student.admission_date,
                "graduationDate": student.graduation_date,
                "academy": student.academy,
                "major": student.major,
                "education": student.education,
                "idImg": student.id_img,
            }
        res = {
            "code": 200,
            "data": temp_student
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def update_student(request):
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
            students = Student.objects.filter(user_id=users[0].id)
            students.update(
                sex=data.__getitem__('sex'),
                email=data.__getitem__('email'),
                school=data.__getitem__('school'),
                admission_date=data.__getitem__('admissionDate'),
                graduation_date=data.__getitem__('graduationDate'),
                academy=data.__getitem__('academy'),
                major=data.__getitem__('major'),
                education=data.__getitem__('education'),
                id_img=data.__getitem__('idImg'),
            )
            temp_student = {
                "id": students[0].id,
                "user": {
                    "id": users[0].id,
                    "account": users[0].account,
                    "phone": users[0].phone,
                    "password": users[0].password,
                    "name": users[0].name,
                    "type": users[0].type
                },
                "sex": students[0].sex,
                "email": students[0].email,
                "school": students[0].school,
                "admissionDate": students[0].admission_date,
                "graduationDate": students[0].graduation_date,
                "academy": students[0].academy,
                "major": students[0].major,
                "education": students[0].education,
                "idImg": students[0].id_img,
            }
        else:
            temp_student = {}
        res = {
            "code": 200,
            "data": temp_student
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def delete_student(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        # users = User.objects.filter(account=user.account)
        students = Student.objects.filter(id=data.__getitem__('id'))
        print(students.__len__())
        if students.__len__() > 0:
            users = User.objects.filter(id=students[0].user.id)
            students.delete()
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
