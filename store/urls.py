from django.urls import path
from .views import *

urlpatterns = [
    path('category', CategoryList.as_view(), name="category"),
    path('product', ProductList.as_view(), name="product"),
    path('product-image', ProductImageList.as_view(), name="productImage"),
]
