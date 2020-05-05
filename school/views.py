from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from .models import School
from school.serializers import SchoolSerializer

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""

# post 需要加，get请求不用加
# @csrf_exempt


def get_all_school(request):
    try:
        # 获取所有 user 数据
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        res = {
            "code": 200,
            "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def search_school_by_name_like(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        schools = School.objects.filter(Q(name__icontains=data.__getitem__('keywords')))
        # schools = School.objects.filter(name=data.__getitem__('keywords'))
        serializer = SchoolSerializer(schools, many=True)
        res = {
            "code": 200,
            "data": serializer.data
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def add_school(request):
    try:
        data = json.loads(request.body)
        school = School(name=data.__getitem__('name'))
        # 获取一个 register 数据
        schools = School.objects.filter(name=data.__getitem__('name'))
        print(schools.__len__())
        if schools.__len__() > 0:
            temp_school = {}
        else:
            school.save()
            temp_school = {
                "id": school.id,
                "name": school.name
            }
        res = {
            "code": 200,
            "data": temp_school
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def update_school(request):
    try:
        data = json.loads(request.body)
        # 获取一个 register 数据
        schools = School.objects.filter(id=data.__getitem__('id'))
        print(schools.__len__())
        if schools.__len__() > 0:
            schools.update(name=data.__getitem__('name'))
            temp_school = {
                "id": schools[0].id,
                "name": schools[0].name
            }
        else:
            temp_school = {}
        res = {
            "code": 200,
            "data": temp_school
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def delete_school(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        schools = School.objects.filter(id=data.__getitem__('id'))
        print(schools.__len__())
        if schools.__len__() > 0:
            schools.delete()
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
