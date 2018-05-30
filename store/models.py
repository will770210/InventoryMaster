from django.db import models
from user.models import User
# Create your models here.

class Store(models.Model):
    store_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    enable = models.BooleanField(default=True)


class Store_User_Relation(models.Model):
    user = models.ForeignKey(User)
    store = models.ForeignKey(Store)
    is_manager = models.BooleanField(default=False)
