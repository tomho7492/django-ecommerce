from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Order(models.Model):
    items = models.CharField(max_length=300, null=True)
    totalCost = models.FloatField(null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.items}"

class Pizza(models.Model):
    type = models.CharField(max_length=300)
    toppingAmount = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=300)
    cost = models.FloatField()

    def __str__(self):
        if self.toppingAmount == None:
            return f"{self.type}, {self.size}, ${self.cost}"
        return f"{self.type}, {self.toppingAmount} toppings, {self.size}, ${self.cost}"

class CartItem(models.Model):
    pizzas = models.ForeignKey(Pizza, on_delete=models.CASCADE, default=None, null=True)
    Cost = models.FloatField(default=0.00)
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"x{self.Quantity} | {self.pizzas} "

class Sub(models.Model):
    type = models.CharField(max_length=300)
    size = models.CharField(max_length=300)
    extras = models.CharField(max_length=300)
    cost = models.FloatField()
class Pasta(models.Model):
    type = models.CharField(max_length=300)
    cost = models.FloatField()
class Salad(models.Model):
    type = models.CharField(max_length=300)
    cost = models.FloatField()
class DinnerPlatter(models.Model):
    type = models.CharField(max_length=300)
    cost = models.FloatField()
    size = models.CharField(max_length=300)