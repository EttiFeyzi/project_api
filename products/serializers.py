from rest_framework import serializers
from .models import Product, ProductsImage
from django.utils import timezone
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth import get_user_model
User = get_user_model()



class DateTimeFieldTZ(serializers.DateTimeField):
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldTZ, self).to_representation(value)

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['phone']


class ProductsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsImage
        fields  = ['image']

class ProductSerializers(serializers.ModelSerializer):

    # user = serializers.SlugRelatedField(read_only=True, slug_field='phone')
    user = UserSerializer(read_only=True, many=False)
    images = ProductsImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(allow_empty_file=False, use_url=False),
    write_only=True)
    
    class Meta:
        model = Product
        fields = ['user','location','category','title','description','publish_time','price','address','images','uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            ProductsImage.objects.create(product=product, image=image)
        return product

