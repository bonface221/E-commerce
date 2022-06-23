from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=100)
    price=models.FloatField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.name 


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered =models.DateTimeField(auto_now_add=True)
    complete =models.BooleanField(default=False,null=True,black=False)
    transaction_id= models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity= models.IntegerField(default=0,null=True,black=True)
    date_added=models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,black=True,null=True)
    address= models.CharField(max_length=100,null=True)
    city= models.CharField(max_length=100,null=True)
    state= models.CharField(max_length=100,null=True)
    zipcode= models.CharField(max_length=100,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address