from django.shortcuts import render
from store.models import *
from product.models import *
from inventory.models import *
# Create your views here.

def inventoryDetail(request, productId):
    user = request.session.get('user')
    product = Product.objects.filter(id=productId)
    relations = Store_User_Relation.objects.filter(user=user, is_manager=True, store__enable=True)

    stores = list([relation.store for relation in relations])

    if product.store in stores:

        inventory = Inventory.objects.filter(product=product).first()


