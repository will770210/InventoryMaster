from django.shortcuts import render,redirect
from product.form import *
from product.models import *
from store.models import *
from inventory.models import *
# Create your views here.


def updateProduct(request, productId):
    user = request.session.get('user')
    product = Product.objects.filter(pk=productId, user=user)
    storeId = product.store.pk
    return redirect('listProduct', storeId=storeId)


def deleteProduct(request, productId):
    user = request.session.get('user')

    product = Product.objects.filter(pk=productId, user=user)
    storeId = product.store.pk

    product.delete()
    return redirect('listProduct', storeId=storeId)


def listProduct(request, storeId):
    user = request.session.get('user')
    if storeId is not None:
        store = Store.objects.filter(pk=storeId).first()
        relations = Store_User_Relation.objects.filter(store=store, user=user, is_manager=True)
        if relations.count():
            products = Product.objects.filter(store=store)
            print(products.count())
            return render(request, 'product_list.html', {'store': store, 'products': products})
        else:
            return redirect('listStore')

def createProduct(request,storeId):
    store = Store.objects.filter(pk=storeId).first()

    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():


            category = None
            if form.cleaned_data['categoryName'] is not None:
               category = Product_Category.objects.create(
                    store= store,
                    parent_category = None,
                    level_of_product = 0,
                    name = form.cleaned_data['categoryName'],
                    enable = True,
               )
               category.save()
            elif form.cleaned_data['categoryId'] is not None:
                category = Product_Category.objects.filter(pk=form.cleaned_data['categoryId'],store=store).first()

            product = Product.objects.create(
                name= form.cleaned_data['name'],
                category=category,
                store=store,
                status=0,
                enable=True

            )
            product.save()

            inventory = Inventory.objects.create(
                store=store,
                product = product,
                amount= 0
            )
            inventory.save()

            inventory_rule = Safety_Inventory_Rule.objects.create(
                inventory=inventory,
                safety_days= form.cleaned_data['safetyDays'],
                enable=True
            )

            inventory_rule.save()

            return redirect('listProduct', storeId=store.pk)

    else:
        form = CreateProductForm()

    return render(request, 'product_create_product.html', {'form': form,'store':store})


