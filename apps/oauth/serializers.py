from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = 'avatar', 'username', 'country', 'city', 'bio',  