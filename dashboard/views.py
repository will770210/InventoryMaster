from django.shortcuts import render
from store.models import *
from inventory.models import *
# Create your views here.
from user.decorators import *


@check_login
def dashboard_index(request):
    user = request.session.get('user')

    relations = Store_User_Relation.objects.filter(user=user)
    stores = list([relation.store for relation in relations])

    print(stores)

    less_safety_inventories = []
    for store in stores:
        print(store.name)
        inventories = Inventory.objects.filter(store=store, is_less_safety_inventory=True)

        storeInventory = StoreInventory()
        storeInventory.store = store
        storeInventory.inventories = inventories

        less_safety_inventories.append(storeInventory)

    return render(request, 'dashboard_index.html', {'less_safety_inventories':less_safety_inventories})


class StoreInventory():
    store = None
    inventories = []
