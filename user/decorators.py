# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from user.models import *

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