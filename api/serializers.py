# import serializer from rest_framework
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
 
# import model from models.py
from .models import Cart, CartImage
 
# Create a model serializer


class CartImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartImage
        fields = ['img_name', 'image', 'products']

class CartSerializer(serializers.ModelSerializer):
    # specify model and fields
    results = CartImageSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
  #      fields = ('product_name', 'product_price')
        fields = ['product_name', 'product_price', 'product_quantity', 'results']