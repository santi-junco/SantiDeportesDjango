from django.db import models

from apps.core.models import TimeStampedModel

class Category(TimeStampedModel):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
