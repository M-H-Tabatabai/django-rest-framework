from django.shortcuts import render

from vip_users.models import User
from vip_users.serializer import UserSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.filter(is_vip=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()

        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_200_OK
        )