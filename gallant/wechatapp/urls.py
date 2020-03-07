from django.urls import path
from wechatapp.views.UserManager import user_register
from wechatapp.views.SignUpManager import *
from wechatapp.views.ActivityManager import *
from wechatapp.views.StoreManager import *
from wechatapp.views.AddressManager import *
from wechatapp.views.ProductsInfoManager import items,itemurl,itemtag,homepage,hotgoods,disgoods,newgoods,itemsdetail
from wechatapp.views.TrollyManager import trolly,trollynum,trollycheckbox
from wechatapp.views.SearchManager import itemSearch,typeForItem
from wechatapp.views.TypeManager import itemtype
from wechatapp.views.CheckOutManager import checkOut

urlpatterns = [

    path('user/register', user_register.as_view(), name='user_register'),
    # path('test/helloworld', donothing.as_view(), name='donothing'),
    path('signup/signup_create', signup_create.as_view(), name='signup_create'),
    path('signup/signup_update',
         signup_update.as_view(), name='signup_update'),
    path('signup/signup_cancel',
         signup_cancel.as_view(), name='signup_cancel'),
    path('signup/signup_view',
         signup_view.as_view(), name='signup_view'),

    path('store/store_create',
         store_create.as_view(), name='store_create'),
    path('store/store_delete',
         store_delete.as_view(), name='store_delete'),
    path('store/store_update',
         store_update.as_view(), name='store_update'),
    path('store/store_view',
         store_view.as_view(), name='store_view'),

    path('activity/activity_create',
         activity_create.as_view(), name='activity_create'),
    path('activity/activity_delete',
         activity_delete.as_view(), name='activity_delete'),
    path('activity/activity_update',
         activity_update.as_view(), name='activity_update'),
    path('activity/activity_view',
         activity_view.as_view(), name='activity_view'),
    path('activity/activitydetail_view',
         activitydetail_view.as_view(), name='activitydetail_view'),
#     path('activity/activitystore_view',
#          activitystore_view.as_view(), name='activitystore_view'),

     path('activitytype/activitytype_create',
         activitytype_create.as_view(), name='activitytype_create'),
     path('activitytype/activitytype_delete',
             activitytype_delete.as_view(), name='activitytype_delete'),
     path('activitytype/activitytype_update',
         activitytype_update.as_view(), name='activitytype_update'),
     path('activitytype/activitytype_view',
         activitytype_view.as_view(), name='activitytype_view'),


       # 商品种类
     path('product/itemtype', itemtype.as_view(), name='itemtype'),
     path('product/items', items.as_view(), name='items'),
     path('product/itemspic', itemurl.as_view(), name='itemsurl'),
     path('product/itemtag', itemtag.as_view(), name='itemtag'),

     # 首页
     path('home/all', homepage.as_view(), name='homepage'),
     path('home/hotgoods', hotgoods.as_view(), name='hot'),
     path('home/newgoods', newgoods.as_view(), name='new'),
     path('home/disgoods', disgoods.as_view(), name='dis'),

     # 商品详情
     path('items/detail', itemsdetail.as_view(), name='itemsdetail'),

     # 购物车
     path('trolly/item', trolly.as_view(), name='trolly'),
     path('trolly/num', trollynum.as_view(), name='trolly'),
     path('trolly/checkbox', trollycheckbox.as_view(), name='trolly'),

     # 订单相关信息
     path('checkout/checked', checkOut.as_view(), name='checked'),
     

     # 搜索查询
     path('search/items', itemSearch.as_view(), name='search'),
     path('search/typeForItem', typeForItem.as_view(), name='typeForItem'),

     # 省市区查询
     path('areas', area_view.as_view(), name='areas'),
     path('areas2', area_view2.as_view(), name='areas2'),

     # 地址管理
     path('address', address.as_view(), name='address'),
     path('address/detail', address_detail.as_view(), name='address_detail'),

]  
