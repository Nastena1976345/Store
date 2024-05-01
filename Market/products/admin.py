from django.contrib import admin
from .models import Product, ProductIMG, Type

admin.site.register(Type)


class AdminInLineAndProductIMG(admin.TabularInline):
    model = ProductIMG


class AdminProduct(admin.ModelAdmin):
    fields = ["title", "price", "description", "count", "product_type"]
    inlines = [AdminInLineAndProductIMG]


admin.site.register(Product, AdminProduct)
