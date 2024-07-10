from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import Product, Quantity


class User(AbstractUser):
    phone = models.CharField(max_length=13)
    icon = models.ImageField(upload_to='icons/')
    bio = models.TextField()

    def __str__(self):
        return f"{self.get_full_name()} {self.id}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=255, default='preparing', choices=(
        ('preparing', 'Preparing'),
        ('delievering', 'Delievering'),
        ('delievered', 'Delievered')
    ))

    def __str__(self):
        return f"{self.user} {self.product}"
    
    def save(self, *args, **kwargs):
        if self.status == 'delievered':
            qua = Quantity.objects.get(product=self.product)
            qua.quantity -= self.quantity
            self.product.ordered += self.quantity
            self.product.save()
            qua.save()
        super(Order, self).save(*args, **kwargs)


class FavouriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.product}"


class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.DecimalField(max_digits=5, default=5, decimal_places=2)
    text = models.TextField()

    def __str__(self):
        return f"{self.user} {self.product} {self.rating}"
    

    def save(self, *args, **kwargs):
        rating = self.rating
        count = 1
        for feedback in self.product.feedbacks.all():
            rating += feedback.rating
            count += 1
        self.product.rating = (rating / count)
        self.product.save()
        super(FeedBack, self).save(*args, **kwargs)