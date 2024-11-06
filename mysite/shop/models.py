from django.db import models


class Category(models.Model):
    category_name=models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name=models.CharField(max_length=64)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    have = models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    video=models.FileField(upload_to='vid/', null=True,blank=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)


    def __str__(self):
        return self.product_name

