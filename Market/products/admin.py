from django.contrib import admin
from .models import Product, ProductIMG, Type

admin.site.register(Type)


class AdminInLineAndProductIMG(admin.TabularInline):
    model = ProductIMG


class AdminProduct(admin.ModelAdmin):
    fields = ["title", "price", "count", "product_type"]
    inlines = [AdminInLineAndProductIMG]


admin.site.register(Product, AdminProduct)
# Register your models here.
# a = {
#    'Ширина (см)': 100,
#    'Высота (см)': 200.6,
#    'Глубина (см)': 37.2,
#    'Цвет': "Белый",
# }
