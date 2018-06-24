from django.shortcuts import render, redirect
from store.models import *
from product.models import *
from inventory.models import *
from inventory.form import *

# Create your views here.

def inventoryDetail(request, productId):
    user = request.session.get('user')
    product = Product.objects.filter(id=productId).first()
    relations = Store_User_Relation.objects.filter(user=user, is_manager=True, store__enable=True)

    stores = list([relation.store for relation in relations])

    if product.store in stores:

        inventory = Inventory.objects.filter(product=product).first()
        inventory_histories = Inventory_History.objects.filter(inventory=inventory).order_by('-created_at')
        return render(request, 'inventory_detail.html', {'product': product, 'inventory': inventory, 'inventory_histories': inventory_histories})

    return redirect('listStore')


def updateInventory(request, inventory_id):

    user = request.session.get('user')
    inventory = Inventory.objects.filter(id=inventory_id).first()
    form = UpdateInventoryForm(request.POST, inventroy_id=inventory_id)

    if form.is_valid():
        action_type = form.cleaned_data['action_type']
        current_amount = 0
        if action_type == 'IN':
            current_amount = inventory.amount + form.cleaned_data['quantity']
        elif action_type == 'OUT':
            current_amount = inventory.amount - form.cleaned_data['quantity']

        inventory_History = Inventory_History.objects.create(
            store=inventory.store,
            product = inventory.product,
            inventory = inventory,
            previous_amount = inventory.amount,
            current_amount = current_amount,
            action_type = action_type,
            created_by = user,
            updated_by = user
        )
        inventory_History.save()

        inventory.amount = current_amount

        if action_type == 'IN' and current_amount >= inventory.safety_inventory_amount: # 進貨若總庫存大於安全庫存，則將低於安全庫存的flag改為False
            inventory.is_less_safety_inventory = False

        inventory.save()

        return redirect('inventoryDetail', productId=inventory.product.id)

    else:
        form = UpdateInventoryForm(inventroy_id=inventory_id)

    print(inventory.store.id)

    return render(request, 'inventory_update_form.html', {'inventory':inventory , 'form': form})
