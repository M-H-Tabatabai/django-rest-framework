from rest_framework import serializers
from bookshop.models import MyBook, Author, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
    

class MyBookSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    # category = serializers.StringRelatedField(many = True)

    author = AuthorSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = MyBook
        fields = "__all__"