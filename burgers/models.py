from django.db import models

# Create your models here.
class Burger(models.Model):
    nameOfBurger=models.CharField(max_length=200)
    ingredientOne=models.CharField(max_length=200)
    ingredientTwo=models.CharField(max_length=200)
    ingredientThree=models.CharField(max_length=200)
    ingredientFour=models.CharField(max_length=200)
    ingredientFive=models.CharField(max_length=200)
    ingredientSix=models.CharField(max_length=200)
    ingredientSeven=models.CharField(max_length=200)
    haveEaten=models.BooleanField(default=False)