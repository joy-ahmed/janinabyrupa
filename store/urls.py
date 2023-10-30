from django.urls import path,  include

from rest_framework import routers
from .views import *
from accounts import views as accountsView

route = routers.DefaultRouter()
route.register('products', ProductViewsets)
route.register('categories', CategoryViewsets)
route.register('product-images', ProductImageViewsets)

# users api
route.register('users', accountsView.CustomUserViewsets)

urlpatterns = [
    path('', include(route.urls))
]
