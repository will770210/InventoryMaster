"""InventoryMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from user.views import *

from store.views import createStore, joinStore, listStore, deleteStore, updateStore

from product.views import createProduct,createProductFirst, updateProduct, listProduct, deleteProduct, createProductCategory, updateProductCategory, listProductCategory, deleteProductCategory

from inventory.views import *

urlpatterns = [
    url(r'^/',login),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^user/$', user.views.login_view, name='user'),
    url(r'^user/login/$', login, name='login'),
    url(r'^user/logout/$', logout, name='logout'),
    url(r'^user/register/', register, name='register'),
    url(r'^user/forgotPassword/', forgotPassword, name='forgotPassword'),
    url(r'^user/userActivate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', userActivate, name='userActivate'),
    url(r'^user/resetPassword/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', userResetPassword, name='userResetPassword'),
    url(r'^user/reSendActiveMail/', reSendUserActiveMail, name='reSendUserActiveMail'),
    url(r'^user/home/', home, name='home'),
    url(r'^user/testMail/', testMail),
    url(r'^user/setNewPassword/', userSetNewPassword, name='userSetNewPassword'),
    url(r'^user/detail/', userDetail,name='userDetail'),
    url(r'^user/updatePassword/', updatePassword, name='updatePassword'),
    url(r'^user/update/', updateUser,name='updateUser'),
    url(r'^store/create/', createStore , name='createStore'),
    url(r'^store/join/', joinStore, name='joinStore'),
    url(r'^store/list/', listStore, name='listStore'),
    url(r'^store/delete/(?P<storeId>\d+)/$', deleteStore, name='deleteStore'),
    url(r'^store/update/(?P<storeId>\d+)/$', updateStore, name='updateStore'),

    url(r'^product/create/(?P<storeId>\d+)/$', createProduct, name='createProduct'),
    url(r'^product/createFirest/(?P<storeId>\d+)/$', createProductFirst, name='createProductFirst'),
    url(r'^product/update/(?P<productId>\d+)/$', updateProduct, name='updateProduct'),
    url(r'^product/list/(?P<storeId>\d+)/$', listProduct, name='listProduct'),
    url(r'^product/delete/(?P<productId>\d+)/$', deleteProduct, name='deleteProduct'),

    url(r'^category/create/(?P<storeId>\d+)/$', createProductCategory, name='createProductCategory'),
    url(r'^category/update/(?P<categoryId>\d+)/$', updateProductCategory, name='updateProductCategory'),
    url(r'^category/list/(?P<storeId>\d+)/$', listProductCategory, name='listProductCategory'),
    url(r'^category/delete/(?P<categoryId>\d+)/$', deleteProductCategory, name='deleteProductCategory'),
    url(r'^$', login),

    url(r'^inventory/detail/(?P<productId>\d+)/$', inventoryDetail, name='inventoryDetail'),
    url(r'^inventory/update/(?P<inventory_id>\d+)/$', updateInventory, name='updateInventory'),

    url(r'^todo/',TemplateView.as_view(template_name='todo.html'), name='todo')
]