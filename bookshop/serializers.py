from rest_framework import serializers
from bookshop.models import MyBook


class MyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBook
        fields = "__all__"