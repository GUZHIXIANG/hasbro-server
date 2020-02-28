from wechatapp.views import *
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
