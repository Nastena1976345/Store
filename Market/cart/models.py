from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

user = get_user_model()


class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_price(self):
        return self.quantity * self.product.price


class Cart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def add_to_cart(self, product, quantity=1):
        product = Product.objects.get(pk=product)
        item, created = CartItem.objects.get_or_create(product=product, cart=self)
        if not created:
            item.quantity += 1
            item.save()

    def remove_from_cart(self, product):
        item = CartItem.objects.get(product=product, cart=self)
        item.delete()

    def decrease_quantity(self, product):
        item = CartItem.objects.get(product=product, cart=self)
        if item.quantity == 1:
            item.delete()
        else:
            item.quantity -= 1
            item.save()

    def get_cart_items(self):
        return CartItem.objects.filter(cart=self)

    def get_total(self):
        cart_items = self.get_cart_items()
        return sum(item.get_price for item in cart_items)
