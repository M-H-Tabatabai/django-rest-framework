from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    isbn = serializers.CharField(max_length=13)
    pages = serializers.IntegerField()
    language = serializers.CharField(max_length=50)
    