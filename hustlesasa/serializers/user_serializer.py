from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for Users"""

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']