from typing import Any
from rest_framework.serializers import ModelSerializer

from api.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'city']

    def create(self, validated_data: dict[str, Any]):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
    
    
