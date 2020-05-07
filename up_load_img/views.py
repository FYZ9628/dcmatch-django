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
def up_load_img(request):
    try:
        img_files = request.FILES.get('')
        print('测试上传图片')
        print(img_files)
        res = {
            "code": 200,
            "data": {}
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def delete_img(request):
    try:
        data = json.loads(request.body)
        image_path = data.__getitem__('imagePath')
        print('测试删除图片')
        print(image_path)
        res = {
            "code": 200,
            "data": {}
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")