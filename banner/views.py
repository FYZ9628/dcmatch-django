from django.db.models import Q
from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
from .models import Banner
from banner.serializers import BannerSerializer

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""

# post 需要加，get请求不用加
# @csrf_exempt


def get_all_banner(request):
    try:
        # 获取所有 user 数据
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
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
def search_banner_by_name_like(request):
    try:
        data = json.loads(request.body)
        # 获取符合条件的 user 数据
        banners = Banner.objects.filter(Q(name__icontains=data.__getitem__('keywords')))
        # schools = School.objects.filter(name=data.__getitem__('keywords'))
        serializer = BannerSerializer(banners, many=True)
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
def add_banner(request):
    try:
        data = json.loads(request.body)
        banner = Banner(
            name=data.__getitem__('name'),
            src=data.__getitem__('src')
        )
        # 获取一个 register 数据
        banners = Banner.objects.filter(name=data.__getitem__('name'))
        print(banners.__len__())
        if banners.__len__() > 0:
            temp_banner = {}
        else:
            banner.save()
            temp_banner = {
                "id": banner.id,
                "name": banner.name,
                "src": banner.src,
            }
        res = {
            "code": 200,
            "data": temp_banner
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def update_banner(request):
    try:
        data = json.loads(request.body)
        # 获取一个 register 数据
        banners = Banner.objects.filter(id=data.__getitem__('id'))
        print(banners.__len__())
        if banners.__len__() > 0:
            banners.update(
                name=data.__getitem__('name'),
                src=data.__getitem__('src')
            )
            temp_banner = {
                "id": banners[0].id,
                "name": banners[0].name,
                "src": banners[0].src
            }
        else:
            temp_banner = {}
        res = {
            "code": 200,
            "data": temp_banner
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def delete_banner(request):
    try:
        data = json.loads(request.body)
        # 获取一个 user 数据
        banners = Banner.objects.filter(id=data.__getitem__('id'))
        print(banners.__len__())
        if banners.__len__() > 0:
            banners.delete()
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
