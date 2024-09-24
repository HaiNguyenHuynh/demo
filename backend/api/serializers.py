from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["bio", "avatar", "date_of_birth", "location"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "profile",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
