# 每层view文件必须import
from wechatapp.views import *

# 本view层所需要模型和序列化对象
from django.contrib.auth.models import User
from wechatapp.models.AddressModel import *
from wechatapp.serializers.AddressSerializer import *

class address(APIView):
    '''地址创建/修改'''
    @swagger_auto_schema(
        operation_description="小程序用户地址创建/修改接口",
        manual_parameters=[
            openapi.Parameter("address_id", openapi.IN_QUERY, 
            description="地址ID",
            type=openapi.TYPE_INTEGER)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["name","mobile","province","city","district","address","is_default"],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'mobile': openapi.Schema(type=openapi.TYPE_STRING),
                'province': openapi.Schema(type=openapi.TYPE_STRING),
                "city": openapi.Schema(type=openapi.TYPE_STRING),
                "district": openapi.Schema(type=openapi.TYPE_STRING),
                "address": openapi.Schema(type=openapi.TYPE_STRING),
                "is_default": openapi.Schema(type=openapi.TYPE_NUMBER),
            },
        ),
        responses={200: ""},
        security=[]
    )
    def post(self, request, format=None):
        if request.method == "POST": # 验证请求方式
            # 获取用户key
            user_key = request.META.get("HTTP_SESSION_KEY")
            users = User.objects.filter(password=user_key)
            if users.exists():
                user = User.objects.get(password=user_key)
                data = request.data.copy()
                data['user'] = user.id
            else:
                message = "请登录"
                return Response().errorMessage(error="login requried",status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,message=message)
            try: # 验证是否为修改
                address_id = request.data.get('address_id')
                if Address.objects.filter(id=address_id).exists():
                    address = Address.objects.get(id=address_id)
                    address_serializer = AddressSerializer(instance=address, data=request.data, partial=True)
                else:  # 资源不存在异常
                    message = "未找到指定资源"
                    return Response().errorMessage(status=status.HTTP_404_NOT_FOUND, message=message)
            except Exception as e:
                address_serializer = AddressSerializer(
                data=request.data, partial=True)
            if address_serializer.is_valid(): # 验证数据是否合法
                address_serializer.validated_data
                address_serializer.save()
                message = "操作成功"
                return Response().successMessage(status=status.HTTP_200_OK, message=message)
            else: # 数据非法异常
                message = address_serializer.errors
                return Response().errorMessage(status=status.HTTP_406_NOT_ACCEPTABLE, message=message)
        else: # 请求方式异常
            message = "请求方式错误"
            return Response().successMessage(status=status.HTTP_405_METHOD_NOT_ALLOWED, message=message)

    '''地址删除'''
    @swagger_auto_schema(
        operation_description="小程序用户地址删除接口",
        manual_parameters=[
            openapi.Parameter("address_id", openapi.IN_QUERY, 
            description="地址ID",
            type=openapi.TYPE_INTEGER)
        ],
        responses={200: ""},
        security=[]
    )
    def delete(self, request, format=None):
        if request.method == "DELETE":  # 验证请求方式
            # 获取用户key
            user_key = request.META.get("HTTP_SESSION_KEY")
            users = User.objects.filter(password=user_key)
            if users.exists():
                user = User.objects.get(password=user_key)
            else:
                message = "请登录"
                return Response().errorMessage(error="login requried",status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,message=message)
            address_id = request.data.get('address_id')
            # 删除操作
            if Address.objects.filter(id=address_id).exists(): # 验证资源是否存在
                Address.objects.get(id=address_id).delete()
                message = "删除成功"
                return Response().successMessage(status=status.HTTP_200_OK, message=message)
            else: # 资源不存在异常
                message = "未找到指定资源"
                return Response().errorMessage(status=status.HTTP_404_NOT_FOUND, message=message)
        else: # 请求方式异常
            message = "请求方式错误"
            return Response().successMessage(status=status.HTTP_405_METHOD_NOT_ALLOWED, message=message)

    '''地址列表查询'''
    @swagger_auto_schema(
        operation_description="小程序用户地址列表查询接口",
        responses={200: "success"
                   },
        security=[]
    )
    def get(self, request, format=None):
        if request.method == "GET": # 验证请求方式
            # 获取用户key
            user_key = request.META.get("HTTP_SESSION_KEY")
            users = User.objects.filter(password=user_key)
            if users.exists():
                user = User.objects.get(password=user_key)
            else:
                message = "请登录"
                return Response().errorMessage(error="login requried",status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,message=message)
            if Address.objects.filter().exists(): # 验证资源是否存在
                addresses = Address.objects.all()
                address_serializer = StoreSerializer(
                    addresses, many=True)
                message = "查询成功"
                return Response().successMessage(status=status.HTTP_200_OK,
                                                message=message, data=address_serializer.data)
            else:  # 资源不存在异常
                message = "未找到指定资源"
                return Response().errorMessage(status=status.HTTP_404_NOT_FOUND, message=message)
        else: # 请求方式异常
            message = "请求方式错误"
            return Response().successMessage(status=status.HTTP_405_METHOD_NOT_ALLOWED, message=message)


class address_detail(APIView):
    '''地址详情查询'''
    @swagger_auto_schema(
        operation_description="小程序用户地址详情显示接口",
        manual_parameters=[
            openapi.Parameter("address_id", openapi.IN_QUERY, description="地址ID",type=openapi.TYPE_STRING),
        ],
        responses={200: "success"},
        security=[]
    )
    def get(self,request,format=None):
        if request.method == 'GET': # 验证请求方式
            # 获取用户key
            user_key = request.META.get("HTTP_SESSION_KEY")
            users = User.objects.filter(password=user_key)
            if users.exists():
                user = User.objects.get(password=user_key)
            else:
                message = "请登录"
                return Response().errorMessage(error="login requried",status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,message=message)
            address_id = request.data.get('address_id')
            if Address.objects.filter(id=address_id).exists(): # 验证资源是否存在
                address = Address.objects.get(id=address_id).get()
                address_serializer = AddressDetailSerializer(address)
                message = "查询成功"
                return Response().successMessage(status=status.HTTP_200_OK,
                                                message=message, data=address_serializer.data)
            else: # 资源不存在异常
                message = "未找到指定资源"
                return Response().errorMessage(status=status.HTTP_404_NOT_FOUND, message=message)
        else: # 请求方式异常
            message = "请求方式错误"
            return Response().successMessage(status=status.HTTP_405_METHOD_NOT_ALLOWED, message=message)


'''####################################'''

import json
import os
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
JSONFILES_FOLDER = os.path.join(PROJECT_ROOT, 'json_files/')

class area_view(APIView):
    '''活动详情查询'''
    @swagger_auto_schema(
        operation_description="省市区信息查询接口",
        manual_parameters=[
            openapi.Parameter("parent_id", openapi.IN_QUERY, description="父ID",
                              type=openapi.TYPE_STRING),
        ],
        responses={200: "success"
                   },
        security=[]
    )
    def get(self, request, format=None):
        if request.method == "GET":  # 验证请求方式
            parent_id = request.GET.get('parent_id')
            try:
                path = JSONFILES_FOLDER + "areas.json"
                with open(path, 'r') as f:
                    areas = json.loads(f.read())
                message = "查询成功"
                return Response().successMessage(status=status.HTTP_200_OK,
                                                    message=message, data=areas)
            except Exception as e:  # 资源不存在异常
                message = "未找到指定资源"
                return Response().errorMessage(status=status.HTTP_404_NOT_FOUND, message=message)
        else:  # 请求方式异常
            message = "请求方式错误"
            return Response().successMessage(status=status.HTTP_405_METHOD_NOT_ALLOWED, message=message)


class area_view2(APIView):
    '''活动详情查询'''
    @swagger_auto_schema(
        operation_description="省市区信息查询接口",
        manual_parameters=[
            openapi.Parameter("parent_id", openapi.IN_QUERY, description="父ID",
                              type=openapi.TYPE_STRING),
        ],
        responses={200: "success"
                   },
        security=[]
    )
    def get(self, request, format=None):
        if request.method == "GET":  # 验证请求方式
            parent_id = request.GET.get('parent_id')
            try:
                path = JSONFILES_FOLDER + "areas.json"
                with open(path, 'r') as f:
                    areas = json.loads(f.read())
                areas = [x for x in areas if x['parent_id']==parent_id]
                message = "查询成功"
                return Response().successMessage(status=status.HTTP_200_OK,
                                                 message=message, data=areas)
            except Exception as e:  # 资源不存在异常
                message = "未找到指定资源"
                return Response().errorMessage(status=status.HTTP_404_NOT_FOUND, message=message)
        else:  # 请求方式异常
            message = "请求方式错误"
            return Response().successMessage(status=status.HTTP_405_METHOD_NOT_ALLOWED, message=message)