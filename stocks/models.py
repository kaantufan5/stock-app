from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.shortcuts import get_object_or_404

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    @property
    def product_count(self):
        return self.product_set.count() 


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @property
    def products_count(self):
        return self.product_set.count() 


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="product_brand")
    stock = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Firm(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    adress = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Stock(models.Model):

    SCALE = (
        ('I', 'In'),
        ('O', 'Out'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, related_name="stock_firm")
    transaction = models.CharField(max_length=1, choices=SCALE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock_product")
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    price_total = models.DecimalField(max_digits=9, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.firm} - {self.product} - {self.price}'


@receiver(pre_save, sender=Stock)
def price_update(instance, *args, **kwargs):
        if not instance.price_total:
            instance.price_total = instance.quantity * instance.price


@receiver(post_save, sender=Stock)
def stock_update(instance, created=False, *args, **kwargs):
    if created:
        if instance.transaction == "O":
            if instance.quantity > instance.product.stock:
                print("Sorry, we are out of stock.")
            else:
                product_stock = get_object_or_404(Product, pk=instance.product.id)
                product_stock.stock -= instance.quantity
                product_stock.save(update_fields=["stock"]) 
                print("Successfully taken out of stock!") 
        elif instance.transaction == "I":
                product_stock = get_object_or_404(Product, pk=instance.product.id)
                product_stock.stock += instance.quantity
                product_stock.save(update_fields=["stock"]) 
                print("Successfully added to stock!")




