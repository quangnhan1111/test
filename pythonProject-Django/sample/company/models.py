from django.db import models

# Create your models here.
# from sample.base.models import Base
# from sample.base.models import Base


class Company(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

    def delete(self):
        self.deleted_at = True
        self.save()

    def restore(self):
        self.deleted_at = False
        self.save()
