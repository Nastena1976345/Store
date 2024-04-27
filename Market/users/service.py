from django_filters import rest_framework as filters

from products.models import Product

# class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass


class ProductFilter(filters.FilterSet):
    # price = filters.RangeFilter()
    count = filters.RangeFilter()
    class Meta:
        model = Product
        fields = ['price', 'count']
