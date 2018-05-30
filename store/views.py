from django.shortcuts import render, redirect
# Create your views here.
from store.form import *
from store.models import *
from product.form import *
import uuid

def listStore(request):
    user = request.session.get('user')
    relations = Store_User_Relation.objects.filter(user=user, is_manager=True).select_related('store')

    stores = list([relation.store for relation in relations])

    print(stores)
    return render(request, 'store_list.html', {'stores': stores})


def deleteStore(request, storeId):
    user = request.session.get('user')
    store = Store.objects.filter(pk=storeId).first()
    store.delete()
    return redirect('listStore')

def updateStore(request, storeId):
    pass

def createStore(request):
    if request.method == 'POST':
        form = CreateStoreForm(request.POST)
        if form.is_valid():
            store = Store.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                enable=True,
                store_code=str(uuid.uuid4())
                )
            store.save()

            store_user_releation = Store_User_Relation.objects.create(
                user=request.session.get('user'),
                store=store,
                is_manager=True

            )
            store_user_releation.save()

            form = CreateProductForm()
            return render(request, 'product_create_product.html', {'form': form,'store':store})

    else:
        form = CreateStoreForm()

    return render(request, 'store_create_store.html', {'form': form})


def joinStore(request):
    pass