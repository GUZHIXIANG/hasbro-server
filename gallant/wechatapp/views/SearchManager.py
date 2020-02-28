from wechatapp.views import *
# 模型
from wechatapp.models.ProductModel import (ProductBaseInfo,ProductUrl,ProductType,ProductTag)
# 序列器
from wechatapp.serializers.ProductBaseInfoSerializer import (ProductSerializer,ProductUrlSerializer,ProductTypeSerializer,ProductTagSerializer,ProductAllSerializer,ItemsAllSerializer)

# 商品搜索栏支持返回搜索商品用的

class itemSearch(APIView):
    

    @swagger_auto_schema(
    operation_description="get product items from",
    manual_parameters=[
        openapi.Parameter("keyword", openapi.IN_QUERY, description="获取商品详情信息",
                                   type=openapi.TYPE_STRING),
        openapi.Parameter("page", openapi.IN_QUERY, description="获取商品详情信息",
                                   type=openapi.TYPE_STRING),
        openapi.Parameter("size", openapi.IN_QUERY, description="获取商品详情信息",
                                   type=openapi.TYPE_STRING),
        openapi.Parameter("sort", openapi.IN_QUERY, description="获取商品详情信息",
                                   type=openapi.TYPE_STRING),
        openapi.Parameter("order", openapi.IN_QUERY, description="获取商品详情信息",
                                   type=openapi.TYPE_STRING),
        openapi.Parameter("categoryId", openapi.IN_QUERY, description="获取商品详情信息",
                                   type=openapi.TYPE_STRING),
    ],
    responses={200:"success"
    },
    security=[]
    )
    def get(self, request, format=None):

        keyword = request.GET['keyword']
        product = ProductBaseInfo.objects.filter(productName__icontains=keyword)
        serializer = ProductSerializer(product,many=True)
        return Response().successMessage(serializer.data,status=status.HTTP_200_OK)