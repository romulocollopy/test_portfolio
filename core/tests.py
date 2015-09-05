from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Item, Portfolio, Inclusion


class TestPortFolio(TestCase):
    def setUp(self):
        self.me = User.objects.create(username="Romulo", password="test")

        Item.objects.create(name="item1", price="2")
        Item.objects.create(name="item2", price="5")
        Item.objects.create(name="item3", price="15")

        port = Portfolio.objects.create(user=self.me)

        for item, qtd in zip(Item.objects.all(), [3, 2, 3]):
            inc = Inclusion()
            inc.portfolio = port
            inc.item = item
            inc.quantity = qtd
            inc.original_price = item.price
            inc.save()

        item1 = Item.objects.get(id=1)
        item1.price = 185
        item1.save()

    def test_total(self):
        port = Portfolio.objects.get(user=self.me)
        total = port.total()
        print("O total deu o valor esperado: %d" % total)
        self.assertEqual(2*3 + 5*2 + 15*3, total)

