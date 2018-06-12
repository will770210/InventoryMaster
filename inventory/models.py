from django.db import models
from store.models import *
from product.models import *
# Create your models here.


class Inventory(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=0)


class Inventory_History(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(Product)
    inventory = models.ForeignKey(Inventory)
    previous_amount = models.IntegerField(default=0)
    current_amount = models.IntegerField(default=0)
    action_type = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User)
    updated_by = models.ForeignKey(User)


class Safety_Inventory_Rule(models.Model):
    inventory = models.ForeignKey(Inventory)
    safety_days = models.IntegerField(default=3)
    enable = models.BooleanField(default=True)

