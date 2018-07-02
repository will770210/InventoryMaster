from django import forms
from inventory.models import *

class UpdateInventoryForm(forms.Form):
    # ACTION_TYPE_CHOICES = (('IN','進貨'), ('OUT','扣庫存'))

    # action_type = forms.ChoiceField(
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     ),
    #     choices=ACTION_TYPE_CHOICES,
    #     label='執行',
    #     required=True
    # )

    inventory_id = forms.CharField(widget=forms.HiddenInput())

    quantity = forms.IntegerField(
        label='庫存變更為',
        required=True,
        min_value=0,
        initial=1,
        widget=forms.NumberInput(
            attrs={
                'size': '20',
                'class': 'form-control'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        inventory_id = kwargs.pop('inventroy_id')
        super(UpdateInventoryForm, self).__init__(*args, **kwargs)
        self.fields['inventory_id'].initial = inventory_id

        if inventory_id:
            inventory = Inventory.objects.get(id = inventory_id)
            self.fields['quantity'].initial = inventory.amount


    def clean_quantity(self):
        inventory_id = self.cleaned_data['inventory_id']
        inventory = Inventory.objects.get(id=inventory_id)
        quantity = self.cleaned_data['quantity']
        if inventory.amount == quantity:
            raise forms.ValidationError("不可與目前庫存數量一樣")

        return quantity