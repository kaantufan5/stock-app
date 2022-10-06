from django.forms import ValidationError
from rest_framework import serializers
from .models import (
    Category,
    Brand,
    Firm,
    Product,
    Stock
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )

class BrandSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Brand
        fields = (
            'id',
            'name'
        )

class ProductSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(write_only=True)
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'category_id',
            'brand',
            'brand_id',
            'stock'
        )

class FirmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'adress'
        )

class StockSerializers(serializers.ModelSerializer):
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField(write_only=True, required=False)
    user = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Stock
        fields = (
            'id',
            'user',
            'firm',
            'firm_id',
            'transaction',
            'product',
            'product_id',
            'quantity',
            'price',
            'price_total'
        )

    read_only_fields = ('price_total',)

    def validate(self, data):
        if data.get('transaction') == "O":
            product = Product.object.get(id=data.get('product_id'))
            if data.get('quantity') > product.stock:
                raise serializers.ValidationError(
                    f'Sorry, we are out of stock. Stock: {product.stock}'
                )
        return data
