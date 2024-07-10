from django.db import models
from django.core.exceptions import ValidationError


class Catalog(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Category(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    total_products = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Shop(models.Model):
    name = models.CharField(max_length=255)
    credit = models.BooleanField(default=True)
    delivery = models.CharField(max_length=255, default='not_available', choices=(
        ('mavjud', 'Mavjud'),
        ('mavjud_emas', 'Mavjud emas')
    ))

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/')
    series = models.ManyToManyField('Series')

    def __str__(self):
        return self.name


class Quantity(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='quantity')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name}"


class Product(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    series = models.ForeignKey('Series', on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=255)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    price = models.CharField(max_length=16)
    rating = models.DecimalField(max_digits=5, default=5, decimal_places=2)
    description = models.TextField()
    ordered = models.IntegerField()
    popular = models.IntegerField()
    available = models.CharField(max_length=255, default='available', choices=(
        ('mavjud', 'Mavjud'),
        ('mavjud_emas', 'Mavjud emas')
    ))

    def __str__(self):
        return f"{self.brand} {self.name}"


class Series(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Color(models.Model):
    icon = models.ImageField(upload_to='icons/')
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name