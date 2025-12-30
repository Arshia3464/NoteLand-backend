from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    class Meta:
        model = Profile
        fields = ["user_id","name", "last_name", "address", "contact_number", "zip_code", "image", "birth_date"]
        read_only_fields = ["user", "role", "subscription_type"]

class ProfileAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user"]

