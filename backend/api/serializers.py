from django.contrib.auth.models import User, Group
from dj_rest_auth.registration.serializers import RegisterSerializer
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


class CustomRegisterSerializer(RegisterSerializer):
    date_of_birth = serializers.DateField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["date_of_birth"] = self.validated_data.get("date_of_birth", "")
        return data

    def save(self, request):
        user = super().save(request)
        viewer_group = Group.objects.get(name="Viewer")  # Default group
        user.groups.add(viewer_group)  # Assign user to Viewer role
        user.save()
        return user
