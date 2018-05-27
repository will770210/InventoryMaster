from django.shortcuts import render
from django import forms
from user.models import User
from user.form import *
from django.http import HttpResponse
# import logging
# Create your views here.

# logger = logging.getLogger('django')


def login_view(request):
    return render(request, 'user_login.html', {
        'data': "hello",
    })


def register(request):
    if request.method == 'POST':
        # logger.info('request.method')
        form = RegisterForm(request.POST)
        if form.is_valid():
            # logger.info('is_valid pass')
            User.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                is_active=False)
            #todo render view
            return HttpResponse("Register Success!")
    else:
        form = RegisterForm()
    return render(request, 'user_register.html', {'form': form})


def forgot_password_view(request):
    return render(request, 'user_forgot_password.html', {})


