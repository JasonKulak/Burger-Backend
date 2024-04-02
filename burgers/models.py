from django.db import models

# Create your models here.
class Burger(models.Model):
    nameOfBurger=models.CharField(max_length=200)
    ingredients=models.CharField(max_length=200)
    haveEaten=models.BooleanField(default=False)