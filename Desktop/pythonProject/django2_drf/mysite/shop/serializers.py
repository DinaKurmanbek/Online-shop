from django import forms
from rest_framework import serializers

from shop.models import Product, Category, SavedItems


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'type' , 'category', 'price', 'demo_content']


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = SavedItems
        fields = ['products']
