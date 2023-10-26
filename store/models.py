import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser
from .utils import product_image_upload_path

from core.models import BaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=80)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="category_created")
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="category_updated")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _('Categories')


class Product(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    short_dscription = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="product_created")
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="product_updated")
    
    class Meta:
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title
    


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productImage")
    image = models.ImageField(upload_to=product_image_upload_path, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="productImage_created")
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="productImage_updated")

    class Meta:
        verbose_name_plural = _('ProductImages')
