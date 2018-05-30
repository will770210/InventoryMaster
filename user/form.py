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

