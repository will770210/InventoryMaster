# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from user.models import *
from store.models import *
from django.utils.functional import wraps

# 验证用户
def check_login(view_func):
    # 此方法为包裹view_func的方法
    # 我们可以在这里定义自己需要的功能
    def _wrapped_view_func(request, *args, **kwargs):
        user = request.session.get('user')
        # 如果用户名为bendan，则重定向到登陆页面
        if user is None:
            return redirect('login')
        # 返回包裹的方法
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func


# def check_permission(view_func):
#     def _wrapped_view_func(request, *args, **kwargs):
#         user = request.session.get('user')
#         # 如果用户名为bendan，则重定向到登陆页面
#         if user is not None:
#             print(storeId)
#             releation = Store_User_Relation.objects.filter(store_id=request.GET.get('storeId'),user=user).first()
#             if releation and releation.is_manager == False:
#                 return render(request,'no_permission.html')
#         # 返回包裹的方法
#         return view_func(request, *args, **kwargs)
#
#     return _wrapped_view_func


def check_permission(view):
    @wraps(view)
    def inner(request, storeId, *args, **kwargs):
        user = request.session.get('user')
        # 如果用户名为bendan，则重定向到登陆页面
        if user is not None:
            print(storeId)
            releation = Store_User_Relation.objects.filter(store_id=storeId, user=user).first()
            if releation and releation.is_manager == False:
                return render(request, 'no_permission.html')

        # Return the actual company object to the view
        return view(request, storeId, *args, **kwargs)

    return inner