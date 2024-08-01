from django.db import models
from django.db.models import ForeignKey


class Category(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Categorie'


class Product(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    description = models.TextField(max_length=512)
    price = models.DecimalField(max_digits=12, decimal_places=1, blank=False, null=False)
    upc = models.IntegerField(blank=False, null=False, unique=True)
    stock = models.IntegerField(blank=True, null=True)
    category_id = models.ForeignKey(Category, models.CASCADE)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} : Price = ({self.price}) , UPC = ({self.upc}) , Stock = ({self.stock}) , Category = ({self.category_id})'


class ProductImage(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.product} - {self.image}'
