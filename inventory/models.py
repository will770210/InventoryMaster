from django.db import models
from store.models import *
from product.models import *
# Create your models here.


class Inventory(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=0)


class Safety_Inventory_Rule(models.Model):
    inventory = models.ForeignKey(Inventory)
    safety_days = models.IntegerField(default=3)
    enable = models.BooleanField(default=True)

