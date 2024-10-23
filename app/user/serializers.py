"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model  # type: ignore

from rest_framework import serializers  # type: ignore


class UserSerializer(serializers.ModelSerializer):
    """Serializers for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwarg = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
