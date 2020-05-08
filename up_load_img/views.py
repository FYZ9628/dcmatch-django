import os
import random

from django.http import HttpResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt

""""
1、json.dumps()和json.loads()是json格式处理函数（两函数为互逆过程）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

2、json.dump()和json.load()主要用来读写json文件函数

"""


@csrf_exempt
def up_load_img(request):
    try:
        img_files = request.FILES.get('upLoadImg')
        base_name = random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 6)
        img_name = ''
        for index in range(len(base_name)):
            img_name += base_name[index]
        destination = open(
            os.path.join("D:\\workspace\\img\\dcmatch", img_name + '.jpg'), 'wb+')
        for chunk in img_files.chunks():
            destination.write(chunk)
        destination.close()
        img_url = "http://localhost:8999/api/file/" + img_name + '.jpg'
        res = img_url
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
        xie_gang_num = 0
        image_name = ''
        ke_jia = False
        for index in range(len(image_path)):
            if image_path[index] == '/':
                print(index)
                print(image_path[index])
                xie_gang_num += 1
            if ke_jia:
                image_name += image_path[index]
            if xie_gang_num >= 5:
                ke_jia = True
        dir_path = 'D:\\workspace\\img\\dcmatch\\'
        os.remove(dir_path + image_name)
        result_info = ''
        res = result_info
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")