from rest_framework import serializers

from cart.models import CartItem
from products.models import Product
from products.models import Image

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "price", "count")


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("id", "cart", "product", "quantity")

########################################################################
class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "path", "decs", "gallery_id")
