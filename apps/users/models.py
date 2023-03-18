from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import TimeStampedModel
from apps.products.models import Product

class Usuario(AbstractUser):
    is_active = models.BooleanField(default=False)

class UserSelection(TimeStampedModel):
    user = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
