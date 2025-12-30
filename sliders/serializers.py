from rest_framework import serializers
from .models import Slider

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ["id", "publisher", "name", "link","description", "price", "active","image"]
        read_only_fields = ["publisher"]

