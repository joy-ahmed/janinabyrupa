from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
 





# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ['image']
# class ProductSerializer(serializers.ModelSerializer):
#     productImage = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'slug', 'description', 'price', 'category', 'created_by', 'updated_by', 'productImage']

#     def get_productImage(self, obj):
#         request = self.context.get('request')
#         product_images = ProductImage.objects.filter(product=obj)
#         image_urls = [request.build_absolute_uri(image.image.url) for image in product_images]
#         return image_urls
    


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    productImage = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'short_dscription', 'description', 'price', 'category', 'created_by', 'updated_by', 'productImage']


