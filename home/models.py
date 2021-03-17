from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Description = models.TextField()
    def __str__(self):
        return self.Name
class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Description = models.TextField()
    def __str__(self):
        return self.Name
class Shoes(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Price = models.IntegerField(blank=True, null = True)
    SexID = models.ForeignKey(Sex, default=None, on_delete=models.CASCADE, blank=True, null = True)
    CategoryID = models.ForeignKey(Category, default=None, on_delete=models.CASCADE, blank=True, null = True)
    NumberBuy = models.IntegerField(blank=True, null = True)
    Color = models.CharField(max_length=20)
    Style = models.CharField(max_length=40)
    Made_in = models.CharField(max_length=40)
    Sales = models.BooleanField(null= True, blank=True)
    New_Price = models.IntegerField(blank=True, null = True)
    Image = models.ImageField()
    Description = models.TextField(blank=True, null = True)
    def __str__(self):
        return self.Name
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    ShoesID = models.ForeignKey(Shoes, default=None, on_delete=models.CASCADE, blank=True, null = True)
    Quantity = models.IntegerField(blank=True, null = True)
    UserID = models.ForeignKey(User, default=None, on_delete=models.CASCADE, blank=True, null = True)
    def __str__(self):
        return self.Name
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    ShoesID = models.ForeignKey(Shoes, default=None, on_delete=models.CASCADE, blank=True, null = True)
    Quantity = models.IntegerField(blank=True, null = True)
class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Date = models.DateTimeField(auto_now_add = True)
    ProductID = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, blank=True, null = True)
    Total_price = models.IntegerField(blank=True, null = True)
    def __str__(self):
        return self.Name

