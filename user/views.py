from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render(request, 'user_login.html', {
        'data': "hello",
    })


def register_view(request):
    return render(request, 'user_register.html', {})

def forgot_password_view(request):
    return render(request, 'user_forgot_password.html', {})