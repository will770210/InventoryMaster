from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from store.form import *
from store.models import *
from product.form import *
import uuid
from django.views.generic import UpdateView
from user.decorators import *

@check_login
def listStore(request):
    user = request.session.get('user')
    relations = Store_User_Relation.objects.filter(user=user, store__enable=True)

    stores = list([relation.store for relation in relations])

    print(stores)
    return render(request, 'store_list.html', {'stores': stores})


@check_login
@check_permission
def deleteStore(request, storeId):
    user = request.session.get('user')
    store = Store.objects.filter(pk=storeId).first()
    relations = Store_User_Relation.objects.filter(store=store, user=user, is_manager=True, store__enable=True)
    if relations.count() > 0:
        store.enable = False
        store.save()
    return redirect('listStore')


@check_login
@check_permission
def updateStore(request, storeId):
    store = get_object_or_404(Store, pk=storeId)
    form = StoreForm(request.POST or None, instance=store)
    if form.is_valid():
        form.save()
        return redirect('listStore')
    return render(request, 'store_update_from.html', {'form': form})


@check_login
def createStore(request):
    if request.method == 'POST':
        form = StoreForm(request.POST or None)
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
            return render(request, 'product_create_first_form.html', {'form': form, 'store': store})

    else:
        form = CreateStoreForm()

    return render(request, 'store_create_form.html', {'form': form})

@check_login
def join_store(request):
    form = JoinStoreForm(request)

    user = request.session.get('user')
    if request.method == 'POST':
        form = JoinStoreForm(request,request.POST)
        if form.is_valid():

            store = Store.objects.get(store_code=form.cleaned_data['store_code'])

            store = Store_User_Relation.objects.create(
                user=user,
                store=store,
                is_manager=False
            )

            store.save()

            return redirect('listStore')

            # store_code = request.POST.get('store_code')
            # store = Store.objects.get(store_code=store_code)
            # if store is not None:
            #
            #     releation = Store_User_Relation.objects.get(user=user, store__store_code=store_code)
            #
            #     if releation is None:






    return render(request, 'store_join_from.html',{'form':form})