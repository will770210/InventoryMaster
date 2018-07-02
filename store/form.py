# -*- coding: utf-8 -*-
from django import forms
from store.models import *


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

class JoinStoreForm(forms.Form):
    store_code = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '請輸入商店代號'
            }
        ))

    def clean_store_code(self):
        store_code = self.cleaned_data['store_code']
        store = Store.objects.filter(store_code=store_code).first()

        if store is None:
            raise forms.ValidationError("請輸入正確商店代碼")


        user = self.request.session.get('user')
        releation = Store_User_Relation.objects.filter(store=store,user=user).first()

        if releation is not None:
            raise forms.ValidationError("您已加入此商店，請輸入其他商店代碼")
            return

        return store_code

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(JoinStoreForm, self).__init__(*args, **kwargs)
