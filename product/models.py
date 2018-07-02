from django.db import models
from store.models import *


class Product_Category(models.Model):
    store = models.ForeignKey(Store)
    parent_category = models.ForeignKey('self', null=True)
    level_of_product = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    store = models.ForeignKey(Store)
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    category = models.ForeignKey(Product_Category)
    enable = models.BooleanField(default=True)
    unit = models.CharField(max_length=50, default="個")
    description = models.CharField(max_length=1024, null=True)


