from django.db import transaction
import xlrd
from wechatapp.views import *

# 模型
from wechatapp.models.ProductModel import (ProductBaseInfo,ProductUrl,ProductTag)
from wechatapp.models.ProductTypeModel import ProductType,ProductSecondCategory,ProductMainCategory
from wechatapp.models.AdvModel import AdvPicModel
# 序列器
from wechatapp.serializers.ProductBaseInfoSerializer import (ProductSerializer,ProductUrlSerializer,ProductTagSerializer,ProductAllSerializer,ItemsAllSerializer)
from wechatapp.serializers.AdvSeralizer import AdvPicSerializer
from wechatapp.serializers.TypeSerializer import ProductSecondCategorySerializer

class items(APIView):
    """
    商品信息相关的接口
    """

    # @swagger_auto_schema(
    # operation_description="添加商品分类借口",
    # request_body=openapi.Schema(
    #     type=openapi.TYPE_OBJECT,
    #     required=['productId','productName','productType','price'],
        # properties={
        #     'productId': openapi.Schema(type=openapi.TYPE_STRING),
        #     'productName': openapi.Schema(type=openapi.TYPE_STRING),
        #     'productType':openapi.Schema(type=openapi.TYPE_STRING),
        #     'systemCode': openapi.Schema(type=openapi.TYPE_INTEGER),
        #     'barCode': openapi.Schema(type=openapi.TYPE_INTEGER),
        #     'color': openapi.Schema(type=openapi.TYPE_STRING),
        #     'norms': openapi.Schema(type=openapi.TYPE_STRING),
        #     'weight': openapi.Schema(type=openapi.TYPE_INTEGER),
        #     'price': openapi.Schema(type=openapi.TYPE_INTEGER),
        #     'descripation': openapi.Schema(type=openapi.TYPE_STRING),
        #     'quantity': openapi.Schema(type=openapi.TYPE_INTEGER),  
        #     'shell': openapi.Schema(type=openapi.TYPE_STRING),  
        # },
    # ),
    # responses={201:"创建成功",
    #            },
    # security=[]
    # )
    # def post(self, request, format=None):
        
    #     productId = request.data.get('productId')
    #     productName = request.data.get('productName')
    #     productType = request.data.get('productType')
    #     systemCode = request.data.get('systemCode')
    #     barCode = request.data.get('barCode')
    #     color = request.data.get('color')
    #     norms = request.data.get('norms')
    #     weight = request.data.get('weight')
    #     price = request.data.get('price')
    #     descripation = request.data.get('descripation')

        
    #     try:
    #         ptype = ProductType.objects.get(typeName=productType)
    #         product = ProductBaseInfo(productType=ptype,
    #         productId=productId,
    #         productName=productName,
    #         systemCode=systemCode,
    #         barCode=barCode,
    #         color=color,
    #         norms=norms,
    #         weight=weight,
    #         price=price,
    #         descripation=descripation
    #         )
    #         product.save()
    #         return Response().successMessage(status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print(e)
    #         return Response().errorMessage(error="无法保存",status=status.HTTP_400_BAD_REQUEST)

    
    @swagger_auto_schema(
    operation_description="get product items from",
    manual_parameters=[
        openapi.Parameter("productId", openapi.IN_QUERY, description="获取商品详情信息",
                                   type=openapi.TYPE_STRING),
    ],
    responses={200:"success"
    },
    security=[]
    )
    def get(self, request, format=None):
        product_id = request.GET['productId']
        product = ProductBaseInfo.objects.get(productId=product_id)
        serializer = ProductSerializer(product)
        return Response().successMessage(serializer.data,status=status.HTTP_200_OK)


class itemurl(APIView):
    """
    商品图片相关接口
    """
    @swagger_auto_schema(
    operation_description="添加商品图片",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['productId','url'],
        properties={
            'productId': openapi.Schema(type=openapi.TYPE_STRING),
            'url': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    responses={201:"创建成功",
               },
    security=[]
    )
    def post(self, request, format=None):
        
        productId = request.data.get('productId')
        url = request.data.get('url')
        try:
            pid = ProductBaseInfo.objects.get(productId=productId)
            product = ProductUrl(
            productbaseinfo=pid,
            url=url
            )
            product.save()
            return Response().successMessage(status=status.HTTP_200_OK)
        except Exception as e:
            return Response().errorMessage(error="无法保存",status=status.HTTP_400_BAD_REQUEST)

    
    @swagger_auto_schema(
    operation_description="get product items from",
    manual_parameters=[
        openapi.Parameter("productId", openapi.IN_QUERY, description="获取商品图片信息",
                                   type=openapi.TYPE_STRING),
    ],
    responses={200:"success"
    },
    security=[]
    )
    def get(self, request, format=None):
        product_id = request.GET['productId']
        product = ProductUrl.objects.filter(productbaseinfo=product_id)
        serializer = ProductUrlSerializer(product,many=True)
        return Response().successMessage(serializer.data,status=status.HTTP_200_OK)


class itemtag(APIView):
    """
    商品标签相关
    """
    @swagger_auto_schema(
    operation_description="添加商品标签,tag类型限定，h=热门，d=打折，n=新款",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['productId','tag'],
        properties={
            'productId': openapi.Schema(type=openapi.TYPE_STRING),
            'tag': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    responses={201:"创建成功",
               },
    security=[]
    )
    def post(self, request, format=None):
        
        productId = request.data.get('productId')
        tag = request.data.get('tag')
        try:
            pid = ProductBaseInfo.objects.get(productId=productId)
            product = ProductTag(
            productbaseinfo=pid,
            tag=tag
            )
            product.save()
            return Response().successMessage(status=status.HTTP_200_OK)
        except Exception as e:
            return Response().errorMessage(error="无法保存",status=status.HTTP_400_BAD_REQUEST)

    
    @swagger_auto_schema(
    operation_description="获取商品相关标签",
    manual_parameters=[
        openapi.Parameter("productId", openapi.IN_QUERY, description="获取商品标签信息",
                                   type=openapi.TYPE_STRING),
    ],
    responses={200:"success"
    },
    security=[]
    )
    def get(self, request, format=None):
        product_id = request.GET['productId']
        tag = ProductTag.objects.get(productbaseinfo=product_id)
        serializer = ProductTagSerializer(tag)
        return Response().successMessage(serializer.data,status=status.HTTP_200_OK)


# 
class hotgoods(APIView):
    @swagger_auto_schema(
    operation_description="获取热门商品信息",
    responses={200:"success"
    },
    security=[]
    )
    def get(self, request, format=None):
        tag = ProductTag.objects.filter(tag='h')
        for hot in tag:
            h = ProductBaseInfo.objects.filter(productId=hot.productbaseinfo)
            serializer = ProductAllSerializer(h,many=True)
        return Response().successMessage({"hotgoods":serializer.data},status=status.HTTP_200_OK)

class newgoods(APIView):
    @swagger_auto_schema(
    operation_description="获取新品商品信息",
    responses={200:"success"
    },
    security=[]
    )
    def get(self, request, format=None):
        tag = ProductTag.objects.filter(tag='n')
        for n in tag:
            h = ProductBaseInfo.objects.filter(productId=n.productbaseinfo)
            serializer = ProductAllSerializer(h,many=True)
           
        return Response().successMessage({"newgoods":serializer.data},status=status.HTTP_200_OK)


class disgoods(APIView):
    @swagger_auto_schema(
    operation_description="获取折扣商品信息",
    responses={200:"success"
    },
    security=[]
    )
    def get(self, request, format=None):
        tag = ProductTag.objects.filter(tag='d')
        for d in tag:
            h = ProductBaseInfo.objects.filter(productId=d.productbaseinfo)
            serializer = ProductAllSerializer(h,many=True)
        return Response().successMessage({"disgoods":serializer.data},status=status.HTTP_200_OK)



class homepage(APIView):
    @swagger_auto_schema(
    operation_description="获取商品首页所有信息",
    responses={200:"success"
    },
    security=[]
    )
    def get(self, request, format=None):

        # 首页信息
        type_list = ProductSecondCategory.objects.all() 
        advpic = AdvPicModel.objects.all()
        tag_hot = ProductBaseInfo.objects.filter(producttag__tag__contains='h')
        tag_new = ProductBaseInfo.objects.filter(producttag__tag__contains='n')
        tag_discount = ProductBaseInfo.objects.filter(producttag__tag__contains='d')
        goodsCount = ProductBaseInfo.objects.all()
        
        rollAdvPic = AdvPicSerializer(advpic,many=True)
        channel = ProductSecondCategorySerializer(type_list,many=True)
        hotgoods = ProductAllSerializer(tag_hot,many=True)
        newgoods = ProductAllSerializer(tag_new,many=True)
        discountgoods = ProductAllSerializer(tag_discount,many=True)
        goodsCount = len(goodsCount)
        
        
        return Response().successMessage({"hotgoods":hotgoods.data,
                                          "newgoods":newgoods.data,
                                          "discountgoods":discountgoods.data,
                                          "rollAdvPic":rollAdvPic.data,
                                          "channel":channel.data,
                                          "goodsCount":goodsCount
                                        },status=status.HTTP_200_OK)
   
class itemsdetail(APIView):
    @swagger_auto_schema(
    operation_description="获取商品详情页面",
    manual_parameters=[
        openapi.Parameter("productId", openapi.IN_QUERY, description="获取商品详情信息",
                                   type=openapi.TYPE_STRING),
    ],
    responses={200:"success"
    },
    security=[]
    )
    def get(self,request,format=None):
        
        product_id = request.GET['productId']
        product = ProductBaseInfo.objects.get(productId=product_id)
        url     = ProductUrl.objects.filter(productbaseinfo=product)

        url_seri = ProductUrlSerializer(url,many=True)
        kiop = {"gallary":url_seri.data,
                "goodsinfo":{
                    "name":product.productName,
                    "price":product.price,
                    "brief":product.brief,
                    "brand":product.brand
                    },
                "attribute":{
                        "norms":product.norms,
                        "weight":product.weight
                },
                "number":product.quantity,
                "productId":product.productId
                }
        
        return Response().successMessage(kiop,status=status.HTTP_200_OK)


'''################## Excel批量导入 ##################'''

class import_products_excel(APIView):

    def post(self, request, format=None):
        if request.method == "POST":  # 验证请求方式
            excel_file = request.FILES.get('excel_file', '')
            file_type = excel_file.name.split('.')[1]
            if file_type in ['xlsx', 'xls']:   # 支持这两种文件格式
                # 打开工作文件
                data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
                table = data.sheets()[0]
                rows = table.nrows
                try:
                    with transaction.atomic():
                        for row in range(1, rows):
                            vals = table.row_values(row)
                            ProductBaseInfo.objects.create(
                                productId=vals[0],
                                productName=vals[1],
                                productType=vals[2],  # 关联
                                systemCode=vals[3],
                                barCode=vals[4],
                                color=vals[5],
                                norms=vals[6],
                                weight=vals[7],
                                price=vals[8],
                                descripation=vals[9],
                                brief=vals[10],
                                brand=vals[11],
                                shell=vals[12],
                                quantity=vals[13],
                            )
                except:
                    message = '解析excel文件或者数据插入错误'
                    return Response().successMessage(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=message)
        else:  # 请求方式异常
            message = "请求方式错误"
            return Response().successMessage(status=status.HTTP_405_METHOD_NOT_ALLOWED, message=message)
