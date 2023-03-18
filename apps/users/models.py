from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import TimeStampedModel
from apps.products.models import Product

class User(AbstractUser):
    is_active = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='auth_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='auth_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class UserSelection(TimeStampedModel):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
