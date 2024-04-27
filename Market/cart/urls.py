from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase_item/<int:product_id>/', views.add_to_cart, name='increase_item'),
    path('decrease_item/<int:product_id>/', views.decrease_item, name='decrease_item'),
    path('remove_from_cart/<int:product_id>/', views.delete_item, name='remove_from_cart'),
]
