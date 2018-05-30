# -*- coding: utf-8 -*-
from django import forms


class CreateProductForm(forms.Form):
    name = forms.CharField(
        label='產品名稱',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入商品名稱'
            }
        ))
    categoryName = forms.CharField(
        label='產品類別',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入產品類別'
            }
        ))

    safetyDays = forms.IntegerField(
        label='安全庫存天數',
        required=True,
        min_value=1,
        initial=1,

        widget=forms.NumberInput(
            attrs={
                'size': '20',
                'class': 'form-control'
            }
    ))





