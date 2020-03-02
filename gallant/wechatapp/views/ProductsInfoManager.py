from wechatapp.views import *
# 模型
from wechatapp.models.ProductModel import (ProductBaseInfo,ProductUrl,ProductType,ProductTag)
# 序列器
from wechatapp.serializers.ProductBaseInfoSerializer import (ProductSerializer,ProductUrlSerializer,ProductTypeSerializer,ProductTagSerializer,ProductAllSerializer,ItemsAllSerializer)

from wechatapp.serializers.AdvSeralizer import AdvPicSerializer
from wechatapp.models.AdvModel import AdvPicModel

class itemtype(APIView):
    """
    商品类别管理接口
    """
    @swagger_auto_schema(
    operation_description="添加商品分类借口",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['typeName'],
        properties={
            'typeName': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    responses={201:"创建成功",
               406:"重复不接受创建"},
    security=[]
    )
    def post(self,request,format=None):

        serializer = ProductTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response().successMessage(status=status.HTTP_201_CREATED)
        return Response().errorMessage(error="error",status=status.HTTP_406_NOT_ACCEPTABLE)

    
    
    
    
    @swagger_auto_schema(
    operation_description="获取商品类别列表",
    manual_parameters=[
        openapi.Parameter("list", openapi.IN_QUERY, description="test manual param",
                                   type=openapi.TYPE_STRING),
        openapi.Parameter("level", openapi.IN_QUERY, description="test manual param",
                                   type=openapi.TYPE_STRING),
        
    ],
    responses={200:"success"
    },
    security=[]
    )
    def get(self,request,format=None):

        productType = ProductType.objects.all()
        typeName_list = []
        typeChildName_list = []

        for i in productType:
            typeName_list.append(i.typeName)
    
           
        typeName_list = list(set(typeName_list))
       
        
        typeName_list = [{"name":i} for i in typeName_list ]
        
        
        flag = request.GET['list']
        level = request.GET['level']
        
            
        
        if flag == "all" and level == "null":
            return Response().successMessage({"typeName":typeName_list},status=status.HTTP_200_OK)
        
        elif flag != "all" and flag !=None and level == "null":  #and level1 != None and level2 != None:
            
            productType = ProductType.objects.filter(typeName=flag)
            for i in productType:
                typeChildName_list.append(i.typeChildName)
            typeChildName_list = list(set(typeChildName_list))
            typeChildName_list = [{"name":i} for i in typeChildName_list ]
            
            return Response().successMessage({"typeName":typeChildName_list},status=status.HTTP_200_OK)

        elif flag != "all" and flag !=None and level != "null": 
            productType = ProductType.objects.filter(typeName=flag).filter(typeChildName=level)
            ser = ProductTypeSerializer(productType,many=True)
            return Response().successMessage(ser.data,status=status.HTTP_200_OK)
        
        else:
            return Response().errorMessage(error="错误的参数请求",status=status.HTTP_200_OK)

    
    
    
    
    @swagger_auto_schema(
    operation_description="获取商品类别列表",
    manual_parameters=[
        openapi.Parameter("id", openapi.IN_QUERY, description="test manual param",
                                   type=openapi.TYPE_INTEGER),
    ],
    responses={404:"找不到数据",
               200:"删除成功",
    },
    security=[]
    )
    def delete(self,request,format=None):

        mid = request.GET['id']
        try:
            pt = ProductType.objects.get(id=mid)
        except:
            return Response().errorMessage(error="id={},数据不存在".format(mid),status=status.HTTP_404_NOT_FOUND)

        serializer = ProductTypeSerializer(instance=pt)
        pt.delete()
        return Response().successMessage(serializer.data,status=status.HTTP_200_OK)



class items(APIView):
    """
    商品信息相关的接口
    """

    @swagger_auto_schema(
    operation_description="添加商品分类借口",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['productId','productName','productType','price'],
        properties={
            'productId': openapi.Schema(type=openapi.TYPE_STRING),
            'productName': openapi.Schema(type=openapi.TYPE_STRING),
            'productType':openapi.Schema(type=openapi.TYPE_STRING),
            'systemCode': openapi.Schema(type=openapi.TYPE_INTEGER),
            'barCode': openapi.Schema(type=openapi.TYPE_INTEGER),
            'color': openapi.Schema(type=openapi.TYPE_STRING),
            'norms': openapi.Schema(type=openapi.TYPE_STRING),
            'weight': openapi.Schema(type=openapi.TYPE_INTEGER),
            'price': openapi.Schema(type=openapi.TYPE_INTEGER),
            'descripation': openapi.Schema(type=openapi.TYPE_STRING),
            'quantity': openapi.Schema(type=openapi.TYPE_INTEGER),  
            'shell': openapi.Schema(type=openapi.TYPE_STRING),  
        },
    ),
    responses={201:"创建成功",
               },
    security=[]
    )
    def post(self, request, format=None):
        
        productId = request.data.get('productId')
        productName = request.data.get('productName')
        productType = request.data.get('productType')
        systemCode = request.data.get('systemCode')
        barCode = request.data.get('barCode')
        color = request.data.get('color')
        norms = request.data.get('norms')
        weight = request.data.get('weight')
        price = request.data.get('price')
        descripation = request.data.get('descripation')

        
        try:
            ptype = ProductType.objects.get(typeName=productType)
            product = ProductBaseInfo(productType=ptype,
            productId=productId,
            productName=productName,
            systemCode=systemCode,
            barCode=barCode,
            color=color,
            norms=norms,
            weight=weight,
            price=price,
            descripation=descripation
            )
            product.save()
            return Response().successMessage(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response().errorMessage(error="无法保存",status=status.HTTP_400_BAD_REQUEST)

    
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

        tag_hot = ProductBaseInfo.objects.filter(producttag__tag__contains='h')
        tag_new = ProductBaseInfo.objects.filter(producttag__tag__contains='n')
        tag_discount = ProductBaseInfo.objects.filter(producttag__tag__contains='d')
        
        hotgoods = ProductAllSerializer(tag_hot,many=True)
        newgoods = ProductAllSerializer(tag_new,many=True)
        discountgoods = ProductAllSerializer(tag_discount,many=True)
        
        advpic = AdvPicModel.objects.all()
        rollAdvPic = AdvPicSerializer(advpic,many=True)

        return Response().successMessage({"hotgoods":hotgoods.data,
                                          "newgoods":newgoods.data,
                                          "discountgoods":discountgoods.data,
                                          "rollAdvPic":rollAdvPic.data
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

