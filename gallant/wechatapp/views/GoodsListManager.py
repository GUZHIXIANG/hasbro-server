from wechatapp.views import *
# 模型
from wechatapp.models.ProductModel import (ProductBaseInfo,ProductUrl,PTag)
# 序列器
from wechatapp.serializers.ProductBaseInfoSerializer import *
from wechatapp.serializers.TypeSerializer import *

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
        order = request.GET.get('order')
        sortType = request.GET.get('sort')
        categoryId = request.GET.get('categoryId')

        #（这里要返回所有3级分类的标签）
        
        filterCategory = PTag.objects.filter(desc=3)
        channel = PTypeSerializer(filterCategory, many=True)


        # 热门
        if isHot == '1' and isNew == '0' and isDis == '0':
            
            # 判断是否sortType 有 category 这个关键字在，说明要根据 类别过滤返回的商品
            if sortType=='category':
                
                #TODO：（跟具 3级分类的ID 过滤返回商品相关的数据）
                pass
                
            
            
            if sortType=='price':

                pass


            if sortType=='default':

                pass

            hotProducts = PTag.objects.get(name='热门商品').product.all()
            hotgoods = ProductSerializer2(hotProducts, many=True)
            return Response().successMessage({"goodsList": hotgoods.data}, status=status.HTTP_200_OK)


        


