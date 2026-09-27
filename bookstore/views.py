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
        title = request.data.get("title")
        author = request.data.get("author")
        published_date = request.data.get("published_date")
        isbn = request.data.get("isbn")
        pages = request.data.get("pages")
        language = request.data.get("language")

        if not all([title, author, published_date, isbn, pages, language]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        
        book = Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            isbn=isbn,
            pages=pages,
            language=language,
        )
        return Response({
            "message": "Book created successfully",
            "book": {
                "title": book.title,
                "author": book.author,
                "published_date": book.published_date,
                "isbn": book.isbn,
                "pages": book.pages,
                "language": book.language,
            }
        }, status=status.HTTP_201_CREATED)