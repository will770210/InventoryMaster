from django.shortcuts import render
# Create your views here.
from store.form import *
from store.models import *
import uuid


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
            # store.save()

    else:
        form = CreateStoreForm()

    return render(request, 'store_create_store.html', {'form': form})


def joinStore(request):
    pass