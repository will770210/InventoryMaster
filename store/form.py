# -*- coding: utf-8 -*-
from django import forms
from store.models import Store


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


class StoreForm(forms.ModelForm):


    class Meta:
        model = Store
        fields = ('name', 'phone', 'address') #Note that we didn't mention user field here.

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '請輸入商店名稱'
                }),
            'phone':  forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '請輸入商店電話'
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '請輸入商店地址'
                }),
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
