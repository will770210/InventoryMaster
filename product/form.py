# -*- coding: utf-8 -*-
from django import forms
from product.models import *
from user.models import *
from inventory.models import *


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

    safetyDays = forms.IntegerField(
        label='安全庫存天數',
        required=True,
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                'size': '20',
                'class': 'form-control'
            }
    ))

    class Meta:
        model = Product
        fields = ('name', 'category') #Note that we didn't mention user field here.

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '請輸入商品名稱'
                })
        }

        labels = {
            'name': '商品名稱',
        }

        max_length = {
            'name': 255,
        }

        required = {
            'name': True,
        }

    def __init__(self, *args, **kwargs):
        storeId = kwargs.pop('storeId')
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["category"] = forms.ModelChoiceField(
            label='商品類別',
            required=True,
            queryset=Product_Category.objects.filter(store_id=storeId,enable=True),
            widget=forms.Select(attrs={
                'class': 'form-control',
                'title': '請選擇商品類別'
            }),
            empty_label='請選擇商品類別',
            to_field_name='id'

        )

        if self.instance:
            inventory = Inventory.objects.filter(product=self.instance).first()
            rule = Safety_Inventory_Rule.objects.filter(inventory=inventory).first()
            if rule:
                self.fields['safetyDays'].initial = rule.safety_days
            else:
                self.fields['safetyDays'].initial = 1



class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = Product_Category

        fields = ('name', 'parent_category')  # Note that we didn't mention user field here.

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '請輸入類別名稱'
                })
        }

        labels = {
            'name': '商品類別名稱',
        }

        max_length = {
            'name': 255,
        }

        required = {
            'name': True,
        }

    def __init__(self,*args,**kwargs):
        storeId = kwargs.pop('storeId')
        super(ProductCategoryForm, self).__init__(*args, **kwargs)

        self.fields["parent_category"] = forms.ModelChoiceField(
            label='商品父類別',
            required=False,
            queryset=Product_Category.objects.filter(store_id=storeId,enable=True),
            widget=forms.Select(attrs={
                'class': 'form-control',
                'title': '請選擇父類別'
            }),
            empty_label='請選擇父類別',
            to_field_name='id'

        )