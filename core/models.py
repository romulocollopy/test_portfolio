from django.db import models
from django.db.models import F, Sum
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=11, decimal_places=2)


class Portfolio (models.Model):
    user = models.ForeignKey(User)
    inclusion = models.ManyToManyField(Item, through='Inclusion',
                                  through_fields=('portfolio', 'item'))

    def total(self):
        return self.inclusion_set.all().aggregate(
            total=Sum(F('original_price')*F('quantity')))['total']

class Inclusion(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    item = models.ForeignKey(Item)
    original_price = models.DecimalField(max_digits=11, decimal_places=2)
    quantity = models.PositiveIntegerField(max_length=64)
