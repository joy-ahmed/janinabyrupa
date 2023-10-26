import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from .utils import product_image_upload_path

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    short_dscription = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_upload_path, blank=True)

    class Meta:
        verbose_name_plural = _('ProductImages')
