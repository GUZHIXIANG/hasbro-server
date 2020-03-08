
from wechatapp.views import *
from wechatapp.models.ProductTypeModel import ProductType,ProductSecondCategory,ProductMainCategory
from wechatapp.serializers.TypeSerializer import ProductTypeSerializer,ProductMainCategorySerializer,ProductSecondCategorySerializer


class itemtype(APIView):
    """
    商品类别管理接口
    """
    @swagger_auto_schema(
    operation_description="获取商品分类接口设定",
    manual_parameters=[
        openapi.Parameter("currentTypeId", openapi.IN_QUERY, description="test manual param",
                                   type=openapi.TYPE_STRING),
    ],
    responses={200:"success"
    },
    security=[]
    )
    def get(self,request,format=None):

        currentTypeId = request.GET.get('currentTypeId')
       
        # productType = ProductType.objects.all() 总类目前这一级别不做
        productSecondCategory = ProductSecondCategory.objects.all()

        try:
            currentCategory = ProductSecondCategory.objects.get(id=currentTypeId)
        except:
            return Response().errorMessage(error="没有该类别",status=status.HTTP_400_BAD_REQUEST)
        
        productCurrentCategory = ProductType.objects.filter(typeChildName=currentCategory)

        p_second = ProductSecondCategorySerializer(productSecondCategory,many=True)
        currentCategoryList = ProductTypeSerializer(productCurrentCategory,many=True)
        banner = ProductSecondCategorySerializer(currentCategory)
        
        return Response().successMessage({"typeList":p_second.data,"currentCategory":currentCategoryList.data,"banner":banner.data},status=status.HTTP_200_OK)
       


