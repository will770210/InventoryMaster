# -*- coding: utf-8 -*-
from django import forms


class CreateStoreForm(forms.Form):
    name = forms.CharField(
        label='商店名稱',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入商店名稱'
            }
        ))
    phone = forms.CharField(
        label='商店電話',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入商店電話'
            }
        ))
    address = forms.CharField(
        label='商店地址',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入商店地址'
            }
        )
    )

