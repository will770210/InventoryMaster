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
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get('password')
        user = User.objects.filter(email=email, password=password).first()

        if user is not None and user.is_active==False:
            return render(request, 'user_active_send.html', {})
        elif user is not None:
            request.session['user'] = user
            storeCount = Store_User_Relation.objects.filter(user=user, is_manager=True).values_list("store").count()

            if storeCount == 0:
                return render(request, 'user_home.html', {})
            else:
                return redirect('listStore')

    return render(request, 'user_login.html', {})



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
            #todo render view
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


def forgot_password_view(request):
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
        # login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


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

