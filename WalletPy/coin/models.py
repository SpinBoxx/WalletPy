from django.db import models

# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=6)

class Fiat(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=3)
    short_name = models.CharField(max_length=50)