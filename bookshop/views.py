from django.shortcuts import render
from rest_framework.views import APIView
from bookshop.models import MyBook
from bookshop.serializers import MyBookSerializer
from rest_framework.response import Response

# Create your views here.
class MyBookApiView(APIView):
    def get(self, request):
        books = MyBook.objects.all()
        ser = MyBookSerializer(books, many=True)
        return Response(ser.data)