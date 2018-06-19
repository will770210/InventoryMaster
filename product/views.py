from django.shortcuts import render,redirect
from product.form import *
from product.models import *
from store.models import *
from inventory.models import *
# Create your views here.


def updateProduct(request, productId):
    product = Product.objects.filter(pk=productId).first()

    if request.method == 'POST':

        form = ProductForm(request.POST or None, instance=product, storeId=product.store.id)
        if form.is_valid():

            product.name = form.cleaned_data['name']
            product.category = form.cleaned_data['category']
            product.save()

            inventory = Inventory.objects.filter(product=product).filter()


            Safety_Inventory_Rule.objects.filter(inventory=inventory).update(safety_days=form.cleaned_data['safetyDays'])


            return redirect('listProduct', storeId=product.store.id)

    else:

        form = ProductForm(request.POST or None, instance=product, storeId=product.store.id)

    return render(request, 'product_update_form.html', {'form': form, 'product': product})


def deleteProduct(request, productId):
    user = request.session.get('user')

    product = Product.objects.filter(pk=productId).first()
    storeId = product.store.pk

    store = Store.objects.filter(pk=storeId).first()
    relations = Store_User_Relation.objects.filter(store=store, user=user, is_manager=True)
    if relations.count():
        product.enable = False
        product.save()

    return redirect('listProduct', storeId=storeId)


def listProduct(request, storeId):
    user = request.session.get('user')
    if storeId is not None:
        store = Store.objects.filter(pk=storeId).first()
        relations = Store_User_Relation.objects.filter(store=store, user=user, is_manager=True)
        if relations.count():
            products = Product.objects.filter(store=store, enable=True)
            categories = Product_Category.objects.filter(store=store,enable=True)
            return render(request, 'product_list.html', {'store': store, 'products': products, 'categories':categories})
        else:
            return redirect('listStore')


def createProductFirst(request, storeId):
    store = Store.objects.filter(pk=storeId).first()

    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            category = None
            if form.cleaned_data['categoryName'] is not None:
               category = Product_Category.objects.create(
                    store=store,
                    parent_category=None,
                    level_of_product=0,
                    name=form.cleaned_data['categoryName'],
                    enable=True,
               )
               category.save()

            elif form.cleaned_data['categoryId'] is not None:
                category = Product_Category.objects.filter(pk=form.cleaned_data['categoryId'],store=store).first()

            product = Product.objects.create(
                name=form.cleaned_data['name'],
                category=category,
                store=store,
                status=0,
                enable=True

            )
            product.save()

            inventory = Inventory.objects.create(
                store=store,
                product=product,
                amount=0
            )
            inventory.save()

            inventory_rule = Safety_Inventory_Rule.objects.create(
                inventory=inventory,
                safety_days=form.cleaned_data['safetyDays'],
                enable=True
            )

            inventory_rule.save()

            return redirect('listProduct', storeId=store.pk)

    else:
        form = CreateProductForm()

    return render(request, 'product_create_form.html', {'form': form, 'store':store})


def createProduct(request, storeId):
    store = Store.objects.filter(pk=storeId).first()

    if request.method == 'POST':
        form = ProductForm(request.POST or None, storeId = storeId)
        if form.is_valid():
            # category = Product_Category.objects.filter(pk=form.cleaned_data['category'], store=store).first()

            product = Product.objects.create(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                store=store,
                status=0,
                enable=True

            )
            product.save()

            inventory = Inventory.objects.create(
                store=store,
                product=product,
                amount=0
            )
            inventory.save()

            inventory_rule = Safety_Inventory_Rule.objects.create(
                inventory=inventory,
                safety_days=form.cleaned_data['safetyDays'],
                enable=True
            )

            inventory_rule.save()

            return redirect('listProduct', storeId=store.id)

    else:
        form = ProductForm(request.POST or None, storeId=storeId)

    return render(request, 'product_create_form.html', {'form': form, 'store':store})


def createProductCategory(request, storeId):
    store = Store.objects.filter(id=storeId).first()
    form = ProductCategoryForm(request.POST or None, storeId=store.id)

    if request.method == 'POST':

        if form.is_valid():
            parent_category = form.cleaned_data['parent_category']
            level_of_product = 0
            if parent_category is not None:
                level_of_product = parent_category.level_of_product + 1

            category = Product_Category.objects.create(
                store=store,
                parent_category=parent_category,
                level_of_product=level_of_product,
                name=form.cleaned_data['name'],
                enable=True
            )
            category.save()
            return redirect('listProduct', storeId=storeId)

    return render(request, 'category_create_form.html', {'form':form , 'store':store})

def updateProductCategory(request,categoryId):

    category = Product_Category.objects.filter(id=categoryId).first()

    form = ProductCategoryForm(request.POST or None, instance=category, storeId=category.store.id)

    if request.method == 'POST':

        if form.is_valid():
            parent_category = form.cleaned_data['parent_category']
            level_of_product = 0
            if parent_category is not None:
                level_of_product = parent_category.parent_category + 1
            category.parent_category = parent_category
            category.level_of_product = level_of_product
            category.name = form.cleaned_data['name']
            category.save()

            return redirect('listProduct', storeId=category.store.id)

    return render(request, 'category_update_form.html', {'form': form, 'store': category.store})


def listProductCategory(request,storeId):
    pass


def deleteProductCategory(request,categoryId):
    user = request.session.get('user')

    category = Product_Category.objects.filter(id=categoryId).first()

    store = category.store
    relations = Store_User_Relation.objects.filter(store=store, user=user, is_manager=True)
    if relations.count() > 0:
        products = Product.objects.filter(category=category,enable=True)
        parent_categories = Product_Category.objects.filter(parent_category=category, enable=True)
        if products.count() == 0 and parent_categories.count() == 0:
            category.enable = False
            category.save()

    return redirect('listProduct', storeId=store.id)
