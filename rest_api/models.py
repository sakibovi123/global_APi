from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Campaigns(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    camp = models.ForeignKey(Campaigns, null=True, blank=True, on_delete=models.CASCADE)
    related_product = models.BooleanField(default=False)
    regular_price = models.IntegerField()
    sale_price = models.IntegerField()

    def __str__(self):
        return self.title



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    totla = models.FloatField()
    isComplete = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"User={self.user.username}|isComplete={self.isComplete}"


class Cartproduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    price = models.FloatField()
    quantity = models.IntegerField()
    subtotal = models.FloatField()


    def __str__(self):
        return f"Cart=={self.cart.id}<==>CartProduct:{self.id}==Qualtity=={self.quantity}"

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)