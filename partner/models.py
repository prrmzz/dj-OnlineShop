'''
from django.db import models
from django.db.models import ForeignKey
from products.models import Product


class Partner(models.Model):
    name = models.CharField(max_length=9, blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name

    @property
    def stock(self):
        return self.partners.all()



class PartnerStock(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.partner} : {self.product} / {self.price}"
'''