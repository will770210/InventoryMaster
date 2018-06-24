from django.shortcuts import render,render_to_response,redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from user.tokens import account_activation_token

def sendUserActiveMail(request, user):
    # send user activate mail
    current_site = get_current_site(request)
    message = render_to_string('user_active_mail.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    # Sending activation link in terminal

    mail_subject = '[庫存大師] 啟用帳號'
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype = 'html'
    email.send()