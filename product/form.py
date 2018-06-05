# -*- coding: utf-8 -*-
from django import forms
from product.models import *


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


class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = ('name', 'category', 'safetyDays') #Note that we didn't mention user field here.

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '請輸入商店名稱'
                }),
            'category':  forms.Select(),
            'safetyDays': forms.NumberInput(
                attrs={
                    'size': '20',
                    'class': 'form-control'
                })
        }

        labels = {
            'name': '商店名稱',
            'phone': '商店電話',
            'address': '商店地址'
        }

        max_length = {
            'name': 255,
            'phone': 255,
            'address': 255
        }

        required = {
            'name': True,
            'phone': True,
            'address': True
        }

