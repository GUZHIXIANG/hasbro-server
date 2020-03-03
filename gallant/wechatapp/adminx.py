import xadmin
from xadmin import views

from .models.UserModel import UserProfile
from .models.ProductTypeModel import ProductMainCategory,ProductSecondCategory,ProductType
from .models.ProductModel import ProductBaseInfo,ProductUrl,ProductTag
from .models.TrollyModel import MyTrolly
from .models.AdvModel import AdvPicModel

from .models.ActivityModel import Activity,ActivityStore,ActivityType,ActivityImage
from .models.SignUpModel import SignUp
from .models.StoreModel import Store


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
    list_display = ('id', 'typeName','typeChildName','image_img')
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
xadmin.site.register(Activity)
xadmin.site.register(ActivityStore)
xadmin.site.register(ActivityType)
xadmin.site.register(ActivityImage)
xadmin.site.register(SignUp)
xadmin.site.register(Store)