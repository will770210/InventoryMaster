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

