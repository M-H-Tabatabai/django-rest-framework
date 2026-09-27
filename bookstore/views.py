from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from bookstore.models import Book
from rest_framework import status

from bookstore.serializers import BookSerializer

# Create your views here.
class bookstoreView(APIView):
    def get(self, request):
        books = Book.objects.all()
        ser = BookSerializer(books, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = BookSerializer(data=request.data)
        if  ser.is_valid():
            data = ser.validated_data
            book = Book.objects.create(**data)
            serialized_book = BookSerializer(book)
            return Response({
                "message": "Book created successfully",
                "book": serialized_book.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Book creation failed",
            "errors": ser.errors
        }, status=status.HTTP_400_BAD_REQUEST)