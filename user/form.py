# -*- coding: utf-8 -*-
from django import forms
from user.models import User


class RegisterForm(forms.Form):
    name = forms.CharField(
        label='名字',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入名字'
            }
        ))
    email = forms.EmailField(
        label='Email',
        max_length=254,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入Email'
            }
        ))
    password = forms.CharField(
        label='密碼',
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入密碼'
            }
        )
    )
    checkPassword = forms.CharField(
        label='確認密碼',
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入密碼'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("此Email已註冊過")

        return email

    def clean_checkPassword(self):
        password = self.cleaned_data['password']
        checkPassword = self.cleaned_data['checkPassword']

        if password != checkPassword:
            raise forms.ValidationError("確認密碼錯誤，請重新輸入")

        return password

class UpdateUserForm(forms.Form):
    name = forms.CharField(
        label='名字',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入名字'
            }
        ))

    # def __init__(self, *args, **kwargs):
    #     name = kwargs.pop('name')
    #     super(UpdatePasswordForm, self).__init__(*args, **kwargs)
    #
    #     self.fields["name"].initial = name


class UpdatePasswordForm(forms.Form):

    # user = None


    old_password = forms.CharField(
        label='舊密碼',
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入舊密碼'
            }
        )
    )

    new_password = forms.CharField(
        label='新密碼',
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入新密碼'
            }
        )
    )

    check_new_password = forms.CharField(
        label='確認新密碼',
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入新密碼'
            }
        )
    )

    # def __init__(self, request, *args, **kwargs):
    #     super(UpdatePasswordForm, self).__init__(*args, **kwargs)
    #     self.user = request.session.get('user')

    def clean_check_new_password(self):
        password = self.cleaned_data['new_password']
        checkPassword = self.cleaned_data['check_new_password']

        if password != checkPassword:
            raise forms.ValidationError("確認密碼錯誤，請重新輸入")

        return password

    # def clean_old_password(self):
    #
    #     old_password = self.cleaned_data['old_password']
    #     user = self.user
    #     if old_password != user.password:
    #         raise forms.ValidationError("舊密碼錯誤，請重新輸入")
    #
    #     return old_password


