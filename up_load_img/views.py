from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt

from student.models import Student
from teacher.models import Teacher
from user.models import User
from register.models import Register

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


@csrf_exempt
def team_sign_up_add_student(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        users1 = User.objects.filter(
            account=data.__getitem__('account'),
            name=data.__getitem__('name')
        )
        users2 = User.objects.filter(
            phone=data.__getitem__('account'),
            name=data.__getitem__('name')
        )
        if users1.__len__() != 0:
            students = Student.objects.filter(user_id=users1[0].id)
            temp_student = {
                "id": students[0].id,
                "user": {
                    "id": users1[0].id,
                    "account": users1[0].account,
                    "phone": users1[0].phone,
                    "password": users1[0].password,
                    "name": users1[0].name,
                    "type": users1[0].type
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
            res = temp_student
            # res = {
            #     "code": 200,
            #     "data": temp_student
            # }
            return HttpResponse(json.dumps(res), content_type="application/json")
        if users2.__len__() != 0:
            students = Student.objects.filter(user_id=users2[0].id)
            temp_student = {
                "id": students[0].id,
                "user": {
                    "id": users2[0].id,
                    "account": users2[0].account,
                    "phone": users2[0].phone,
                    "password": users2[0].password,
                    "name": users2[0].name,
                    "type": users2[0].type
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
            res = temp_student
            # res = {
            #     "code": 200,
            #     "data": temp_student
            # }
            return HttpResponse(json.dumps(res), content_type="application/json")
        temp_student = {}
        res = temp_student
        # res = {
        #     "code": 200,
        #     "data": temp_student
        # }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def team_sign_up_add_teacher(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        users1 = User.objects.filter(
            account=data.__getitem__('account'),
            name=data.__getitem__('name')
        )
        users2 = User.objects.filter(
            phone=data.__getitem__('account'),
            name=data.__getitem__('name')
        )
        if users1.__len__() != 0:
            teachers = Teacher.objects.filter(user_id=users1[0].id)
            temp_teacher = {
                "id": teachers[0].id,
                "user": {
                    "id": users1[0].id,
                    "account": users1[0].account,
                    "phone": users1[0].phone,
                    "password": users1[0].password,
                    "name": users1[0].name,
                    "type": users1[0].type
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
            res = temp_teacher
            # res = {
            #     "code": 200,
            #     "data": temp_teacher
            # }
            return HttpResponse(json.dumps(res), content_type="application/json")
        if users2.__len__() != 0:
            teachers = Teacher.objects.filter(user_id=users2[0].id)
            temp_teacher = {
                "id": teachers[0].id,
                "user": {
                    "id": users2[0].id,
                    "account": users2[0].account,
                    "phone": users2[0].phone,
                    "password": users2[0].password,
                    "name": users2[0].name,
                    "type": users2[0].type
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
            res = temp_teacher
            # res = {
            #     "code": 200,
            #     "data": temp_teacher
            # }
            return HttpResponse(json.dumps(res), content_type="application/json")
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

