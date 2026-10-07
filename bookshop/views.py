from django.shortcuts import render
from rest_framework.views import APIView
from bookshop.models import MyBook
from bookshop.serializers import MyBookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import BlocklistPermission
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

# Create your views here.
class MyBookApiView(APIView):
    def get(self, request):
        books = MyBook.objects.all()
        ser = MyBookSerializer(books, many=True)
        return Response(ser.data)


class UserInfoApiView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [BlocklistPermission]

    def get(self, request):
        user = request.user
        return Response(
            {
                "username": user.username,
                "email": user.email,
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        )


class BookManageApiView(APIView):
    def get_object(self, pk):
        book = get_object_or_404(MyBook, id=pk)
        self.check_object_permissions(self.request, book)
        return book

    def get(self, request, pk):
        book = self.get_object(pk)
        ser = MyBookSerializer(book)
        return Response(ser.data)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response({"message":"Book deleted"}, status=status.HTTP_204_NO_CONTENT)
         
class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        token = OutstandingToken.objects.filter(user=user)

        for t in token:
            try:
                BlacklistedToken.objects.get_or_create(token=t)
            except Exception:
                pass

        return Response({"message":"Logout success"}, status=status.HTTP_205_RESET_CONTENT)
