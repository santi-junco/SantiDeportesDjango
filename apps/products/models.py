from django.db import models

from apps.core.models import TimeStampedModel
from apps.categories.models import Category

class Product(TimeStampedModel):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    talle = models.CharField(max_length=10, null=False)
    active = models.BooleanField(default=True)

class ProductPhoto(TimeStampedModel):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products/', null=False)

class ProductCategory(TimeStampedModel):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
