from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'
        # exclude = ['created_at', 'updated_at', 'created_by', 'updated_by']

        
class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_images(self, obj):
        # Assuming you have a related name 'productImage_created' for the images
        images = obj.productImage.all()
        
        request = self.context.get('request')
        image_urls = [request.build_absolute_uri(image.image.url) for image in images]
        return image_urls






