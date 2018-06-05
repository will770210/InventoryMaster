from django.shortcuts import render,render_to_response,redirect
from django import forms
from user.models import *
from store.models import *
from user.form import *
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.template import RequestContext
from user.tokens import *

# import logging
# Create your views here.

# logger = logging.getLogger('django')


def login(request):

    user = None

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get('password')
        user = User.objects.filter(email=email, password=password).first()

    if user is not None and user.is_active == False:
        return render(request, 'user_active_send.html', {})
    elif user is not None:
        request.session['user'] = user
        storeCount = Store_User_Relation.objects.filter(user=user, is_manager=True).values_list("store").count()

        if storeCount == 0:
            return render(request, 'user_home.html', {})
        else:
            return redirect('listStore')

    return render(request, 'user_login.html')


def register(request):
    if request.method == 'POST':
        # logger.info('request.method')
        form = RegisterForm(request.POST)
        if form.is_valid():
            # logger.info('is_valid pass')
            user = User.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                is_active=False)

            #send user activate mail
            current_site = get_current_site(request)
            message = render_to_string('user_active_mail.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = '[庫存大師] 啟用帳號'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return render(request, 'user_active_send.html', {})
    else:
        form = RegisterForm()
    return render(request, 'user_register.html', {'form': form})


def forgotPassword(request):
    print(request.method)
    if request.method == 'POST':
        current_site = get_current_site(request)
        user = User.objects.filter(email=request.POST.get('email')).first()
        print(request.POST.get('email'))
        if user is None:
            print('Can not find user!')
            render(request, 'user_forgot_password.html', {})
        else:
            # Sending activation link in terminal
            mail_subject = '[庫存大師] 密碼重置'
            to_email = user.email
            message = render_to_string('user_reset_password_mail.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_reset_password_token.make_token(user),
            })

            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'message.html',{'title':'重置密碼','content':'已傳送重置密碼連結，至您的註冊Email，請至您的個人Email進行重密碼'})

    return render(request, 'user_forgot_password.html', {})


def userActivate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

    else:
        title = '帳號驗證失敗'
        content = '啟用帳號的連結有誤!'
        return render(request, 'message.html', {'title': title, 'content': content})


def userResetPassword(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_reset_password_token.check_token(user, token):
        return render(request, 'user_reset_password.html', {'user': user})
    else:
        title = '重置密碼失敗'
        content = '重置密碼連結有誤!'
        return render(request, 'message.html', {'title': title, 'content': content})


def userSetNewPassword(request):
    if request.method == 'POST':
        if request.POST.get('id') is not None:
            users = User.objects.filter(pk=request.POST.get('id'))
            user = None
            if users.count() > 0:
                user = users.first()

            if user is not None:
                if request.POST.get('password') is not None and request.POST.get('checkPassword') is not None and request.POST.get('password') == request.POST.get('checkPassword'):
                    user.password = request.POST.get('password')
                    user.save()
                    return redirect('login')
                else:
                    return render(request, 'user_reset_password.html', {'user': user})

    title = '重置密碼失敗'
    content = '重置密碼失敗'
    return render(request, 'message.html', {'title': title, 'content': content})


def home(request):
    return render(request, 'user_home.html', {})


def testMail(request):
    message = render_to_string('test_mail.html', {

    })
    # Sending activation link in terminal
    # user.email_user(subject, message)
    mail_subject = '[庫存大師] 測試信件'
    to_email = 'will770210@gmail.com'
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
    return HttpResponse('Send Success')

