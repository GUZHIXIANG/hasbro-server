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


# 商品详情况管理
class ProductBaseInfoAdmin(object):
    list_display = ('productId', 'productName',"image_img",'productType','color','norms','price','quantity','shell')
xadmin.site.register(ProductBaseInfo,ProductBaseInfoAdmin)

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


# 临时后台用
xadmin.site.register(ActivityType)
xadmin.site.register(SignUp)
xadmin.site.register(Store)

'''############################################################'''

class AImageStackInline(object):
    model = ActivityImage
    extra = 1

class ATextStackInline(object):
    model = ActivityText
    extra = 1


class ActivityAdmin(object):
    list_display = ('activity_name',
                    'activity_type', 'activity_descripation', 'activity_store', 'activity_start_datetime', 'activity_end_datetime', 'super_activity')
    filter_horizontal = ('activity_store',)
    style_fields = {'activity_store': 'm2m_transfer'}

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'activity_store':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs['queryset'] = qs.select_related('content_type')
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)
    
    inlines = [AImageStackInline, ATextStackInline]  # 关联子表

    # def fromfield_for_dbfield(self,db_field,**kwargs):
    #     if db_field.name = 

xadmin.site.register(Activity, ActivityAdmin)

'''############################################################'''
# 外键导入测试
class TypeAdmin(object):
    list_display = ('name','desc')
xadmin.site.register(Type,TypeAdmin)
    
class Test2StackInline(object):
    model = Test2
    extra = 1

class Test3Admin(object):
    list_display = ('name','user')
    filter_horizontal = ('user',)
    style_fields = {'user': 'm2m_transfer'}
xadmin.site.register(Test3, Test3Admin)

class Test41Inline(object):
    model = Test41
    filter_horizontal = ('user',)
    style_fields = {'user': 'm2m_transfer'}
    extra = 1

class Test4Admin(object):
    list_display = ('name', 'user')
    inlines = [Test41Inline]
    # filter_horizontal = ('user',)
    # style_fields = {'user': 'm2m_transfer'}

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'user':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs['queryset'] = qs.select_related('content_type')
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)

xadmin.site.register(Test4, Test4Admin)

# excel导入测试
class TestAdmin(object):
    list_display = ('name', 'age', 'sex','type')

    def type(self, obj):
        '''关联类型名称获取'''
        return obj.type.name
    type.short_description = '类别' # 后台显示名称
    
    inlines = [Test2StackInline] #关联子表

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
                            CHOICE_dict = {'未知':0,'男':1,'女':2}
                            Test.objects.create(
                                name=vals[0],
                                age=vals[1],
                                sex=CHOICE_dict.get(vals[2])
                            )
                except Exception as e:
                    return e
        return super(TestAdmin, self).post(request, args, kwargs)
xadmin.site.register(Test, TestAdmin)





