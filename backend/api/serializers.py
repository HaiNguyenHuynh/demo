from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
