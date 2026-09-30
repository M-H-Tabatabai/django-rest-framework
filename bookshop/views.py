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

class UserInfoApiVeiew(APIView):
    def get(self, request):
        user = request.user
        return Response(
            {
            'username': user.username,
            'email': user.email,
            'id': user.id,
            'first_name': user.first_name,
            'last_name' : user.last_name
            }
     )