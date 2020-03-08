from wechatapp.views import *
# 模型
from wechatapp.models.ProductModel import (ProductBaseInfo,ProductUrl,PTag)
# 序列器
from wechatapp.serializers.ProductBaseInfoSerializer import *

class goodsList(APIView):
    @swagger_auto_schema(
        operation_description="测试*",
        responses={200: "success"
                   },
        manual_parameters=[
            openapi.Parameter("isHot", openapi.IN_QUERY, description="热门",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter("isNew", openapi.IN_QUERY, description="新品",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter("isDis", openapi.IN_QUERY, description="降价",
                              type=openapi.TYPE_INTEGER),
        ],
        security=[]
    )
    def get(self, request, format=None):
        
        isHot = request.GET.get('isHot')
        isNew = request.GET.get('isNew')
        isDis = request.GET.get('isDis')
        # page = request.GET.get('page')
        # size = request.GET.get('size')
        # order = request.GET.get('order')
        # sort = request.GET.get('sort')
        # categoryId = request.GET.get('categoryId')

        # 热门
        if isHot == '1' and isNew == '0' and isDis == '0':
            
            
            hotProducts = PTag.objects.get(name='热门商品').product.all()
            hotgoods = ProductSerializer2(hotProducts, many=True)
            return Response().successMessage({"goodsList": hotgoods.data}, status=status.HTTP_200_OK)


        


