from rest_framework import serializers
from bookshop.models import MyBook, Author, Category


class MyBookSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    # category = serializers.StringRelatedField(many = True)

    author = serializers.SlugRelatedField(slug_field = 'name', queryset = Author.objects.all())
    category = serializers.SlugRelatedField(slug_field = 'title', queryset = Category.objects.all(), many = True)

    class Meta:
        model = MyBook
        fields = "__all__"