from django import forms

class UpdateInventoryForm(forms.Form):
    ACTION_TYPE_CHOICES = (('IN','進貨'), ('OUT','扣庫存'))

    action_type = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        choices=ACTION_TYPE_CHOICES,
        label='執行',
        required=True
    )

    inventory_id = forms.CharField(widget=forms.HiddenInput())

    quantity = forms.IntegerField(
        label='數量',
        required=True,
        min_value=1,
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
