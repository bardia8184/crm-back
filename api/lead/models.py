from django.db import models


class Lead(models.Model):
    status = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=300, unique=False, null=False)
    phone = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=100, null=False)
    interest = models.CharField(max_length=300, null=False)
    source = models.CharField(max_length=50, null=False)
    remark = models.CharField(max_length=300, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
