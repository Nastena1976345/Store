from django.shortcuts import render, redirect
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required


@login_required
def cart_view(requests):
    cart_instance = Cart.objects.get(user=requests.user)
    cart_items = cart_instance.get_cart_items()
    return render(requests, "cart.html", {"cart_items": cart_items})


@login_required
def add_to_cart(requests, product_id):
    cart_instance = Cart.objects.get(user=requests.user)
    cart_instance.add_to_cart(product_id)
    return redirect("cart")


@login_required
def delete_item(requests, product_id):
    cart_instance = Cart.objects.get(user=requests.user)
    cart_instance.remove_from_cart(product_id)
    return redirect("cart")


@login_required
def decrease_item(requests, product_id):
    cart_instance = Cart.objects.get(user=requests.user)
    cart_instance.decrease_quantity(product_id)
    return redirect("cart")
