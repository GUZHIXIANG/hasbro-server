import xadmin
from xadmin import views
from django.contrib import admin

from .models.UserModel import UserProfile
from .models.ProductTypeModel import ProductMainCategory,ProductSecondCategory,ProductType
from .models.ProductModel import ProductBaseInfo,ProductUrl,ProductTag
from .models.TrollyModel import MyTrolly
from .models.AdvModel import AdvPicModel

from .models.ActivityModel import *
from .models.SignUpModel import SignUp
from .models.StoreModel import Store
from .models.TestModel import *

from django.db import transaction
import xlrd


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True      # 开启主题切换功能
    use_bootswatch = True 


xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "酷远后台管理系统"  # 设置站点标题
    site_footer = "酷远商贸有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)


# 通过微信注册的用户相关信息
class UserProfileAdmin(object):
    list_display = ('user', 'nickName','image_img','city')
xadmin.site.register(UserProfile,UserProfileAdmin)


# 商品类别管理

class ProductMainCategoryAdmin(object):
    list_display = ('id', 'typeName')
xadmin.site.register(ProductMainCategory,ProductMainCategoryAdmin)

class ProductSecondCategoryAdmin(object):
    list_display = ('id', 'typeName','typeChildName','image_img','image_img1','banner_name')
xadmin.site.register(ProductSecondCategory,ProductSecondCategoryAdmin)

class ProductTypeAdmin(object):
    list_display = ('id', 'typeChildName','typeChildsName','image_img')
xadmin.site.register(ProductType,ProductTypeAdmin)

class ProductUrlAdmin(object):
    list_display = ('productbaseinfo','image_img','url')
xadmin.site.register(ProductUrl,ProductUrlAdmin)

class ProductTagAdmin(object):
    list_display = ('productbaseinfo','tag')
xadmin.site.register(ProductTag,ProductTagAdmin)

class MyTrollyAdmin(object):
    list_display = ('user','productbaseinfo','nums','checkbox')
xadmin.site.register(MyTrolly,MyTrollyAdmin)

class AdvPicAdmin(object):
    list_display = ('order','productbaseinfo','image_img')
xadmin.site.register(AdvPicModel,AdvPicAdmin)

'''##########################################'''
'''############### 商品信息管理 ###############'''
'''##########################################'''


@xadmin.sites.register(ProductBaseInfo)
class ProductBaseInfoAdmin(object):
    list_display = ('productId', 'productName', "image_img",
                    'productType', 'color', 'norms', 'price', 'quantity', 'shell')

    #excel导入导出功能
    list_export = ['xls', 'xml', 'json']
    import_excel = True

    def post(self, request, *args, **kwargs):
        #  导入逻辑
        if 'excel' in request.FILES:
            pass
            excel_file = request.FILES.get('excel')
            file_type = excel_file.name.split('.')[1]
            if file_type in ['xlsx', 'xls']:   # 支持这两种文件格式
                # 打开工作文件
                data = xlrd.open_workbook(
                    filename=None, file_contents=excel_file.read())
                table = data.sheets()[0]
                rows = table.nrows
                try:
                    with transaction.atomic():
                        for row in range(1, rows):
                            vals = table.row_values(row)
                            CHOICE_dict = {'上架': 'on', '下架': 'off'}
                            ProductBaseInfo.objects.create(
                                productName=vals[0],
                                productType=1,
                                systemCode=vals[2],
                                barCode=vals[3],
                                color=vals[4],
                                norms=vals[5],
                                weight=vals[6],
                                price=vals[7],
                                description=vals[8],
                                brief=vals[9],
                                brand=vals[10],
                                smallurl='',
                                shell=CHOICE_dict.get(vals[12]),
                                quantity=vals[13]

                            )
                except Exception as e:
                    return e
        return super(ProductBaseInfoAdmin, self).post(request, args, kwargs)

'''##########################################'''
'''############### 报名信息查看 ###############'''
'''##########################################'''


@xadmin.sites.register(SignUp)
class SignUpAdmin(object):
    list_display = ('user', 'activity', 'store', 'signup_name',
                    'signup_phone', 'signup_create_time', 'signup_operate_time')
    readonly_fields = ('user', 'activity', 'store', 'signup_name',
                       'signup_phone', 'signup_create_time', 'signup_operate_time')
    search_fields = ('activity__activity_name', 'store__store_name')
    list_filter = ('activity', 'store')
    List_display_links = None  #禁用编辑链接

    def has_add_permission(self):
        return False

    def has_delete_permission(self,request=None):
        return False

'''##########################################'''
'''############### 门店信息管理 ###############'''
'''##########################################'''


@xadmin.sites.register(Store)
class StoreAdmin(object):
    list_display = ('store_name', 'store_telephone',
                    'store_address', 'store_area')
    search_fields = ('store_name', 'store_telephone',
                     'store_address')
    list_filter = ('store_area',)

'''##########################################'''
'''############### 活动类型管理 ###############'''
'''##########################################'''


@xadmin.sites.register(ActivityType)
class ATypeAdmin(object):
    list_display = ('activity_type', 'type_description')
    search_fields = ('activity_type',)


'''##########################################'''
'''############### 活动信息管理 ###############'''
'''##########################################'''

class AImageStackInline(object):
    model = ActivityImage
    extra = 1

class ATextStackInline(object):
    model = ActivityText
    extra = 1


@xadmin.sites.register(Activity)
class ActivityAdmin(object):
    list_display = ('activity_name',
                    'activity_type', 'activity_store', 'activity_start_datetime', 'activity_end_datetime', 'super_activity')
    search_fields = ('activity_name',)
    list_filter = ('activity_type', 'activity_store')
    ordering = ('activity_start_datetime', 'activity_end_datetime')

    filter_horizontal = ('activity_store', 'activity_type')
    style_fields = {'activity_store': 'm2m_transfer'}
    inlines = [AImageStackInline, ATextStackInline]  # 关联子表

