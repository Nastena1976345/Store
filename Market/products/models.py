from django.db import models
from django.urls import reverse


class Type(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"title: {self.title}, id: {self.pk}"


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    product_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"title: {self.title}, id: {self.pk}"

    def get_absolute_url(self):
        return reverse("product_instance", kwargs={"pk": self.pk})


class ProductIMG(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')


###########################################
class Image(models.Model):
    path = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    gallery_id = models.PositiveIntegerField()

    def __str__(self):
        return f"path: {self.path}, id: {self.pk}"
