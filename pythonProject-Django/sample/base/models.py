from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.BooleanField(null=False, default=False)

    class Meta:
        abstract = True
