from django.shortcuts import render
# from rest_framework import generics, viewsets

from cart.models import CartItem
from .models import Product, Type, Image

from rest_framework import viewsets, status
from rest_framework.response import Response

from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend

from users.service import ProductFilter
from .serializers import ProductSerializers, CartSerializers, ImageSerializers

type_list = Type.objects.all()


def product_list(requests):
    products = Product.objects.all()
    return render(requests, "products/product_list.html", context={"products": products, "product_type": type_list})


def product_instance(requests, pk):
    product = Product.objects.get(pk=pk)
    return render(requests, "products/product_instance.html", context={"product": product})


def filter_type(requests, type_pk):
    products = Product.objects.filter(product_type=type_pk)
    return render(requests, "products/product_list.html", context={"products": products, "product_type": type_list})


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProductFilter

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            instance.delete()
            return Response(serializer.data)
        except Http404:
            return Response(status=status.HTTP_204_NO_CONTENT)


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializers
    # filter_backends = (DjangoFilterBackend, )
    # filterset_class = CartFilter

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            instance.delete()
            return Response(serializer.data)
        except Http404:
            return Response(status=status.HTTP_204_NO_CONTENT)


#############################################################
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            instance.delete()
            return Response(serializer.data)
        except Http404:
            return Response(status=status.HTTP_204_NO_CONTENT)