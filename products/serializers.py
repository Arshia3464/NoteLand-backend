from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "owner", "name","name_end", "description_en" "description", "price", "available", "created_at","image"]
        read_only_fields = ["owner", "created_at"]

