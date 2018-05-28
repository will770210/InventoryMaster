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

from django.contrib import admin
admin.autodiscover()

from user.views import login, register, userActivate, forgot_password_view, testMail,home

from store.views import createStore,joinStore

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^user/$', user.views.login_view, name='user'),
    url(r'^user/login/', login, name='login'),
    url(r'^user/register/', register, name='register'),
    url(r'^user/forgotPassword/', forgot_password_view, name='forgot_password'),
    url(r'^userActivate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', userActivate, name='userActivate'),
    url(r'^user/home/', home, name='home'),
    url(r'^user/testMail', testMail),

    url(r'^store/create/', createStore , name='createStore'),
    url(r'^store/join/', joinStore, name='joinStore'),
]