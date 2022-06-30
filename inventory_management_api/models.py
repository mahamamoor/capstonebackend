from django.db import models

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=32)
    product = models.CharField(max_length=32)
    warehouse = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    quantity = models.IntegerField()
