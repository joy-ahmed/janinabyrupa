from django.urls import path
from .views import *

urlpatterns = [
    path('categories', CategoryList.as_view(), name="category"),
    path('products', ProductList.as_view(), name="product"),
    path('product-image', ProductImageList.as_view(), name="productImage"),
]
