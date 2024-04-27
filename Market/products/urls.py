from django.urls import path, include
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'cart', views.CartViewSet)

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>', views.product_instance, name='product_instance'),
    path('product_filter/<int:type_pk>', views.filter_type, name='product_filter'),

    path('api/v1/', include(router.urls)),
]
