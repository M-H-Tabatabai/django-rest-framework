from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100, write_only=True)
    is_vip = serializers.BooleanField(default=False)

    def to_internal_value(self, data):
        internal_data = super().to_internal_value(data)
        return internal_data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['username'] = instance.username.upper()
        representation['is_vip'] = instance.is_vip

        return representation

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_vip"]
