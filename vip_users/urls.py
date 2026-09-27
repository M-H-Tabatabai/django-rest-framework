from django.urls import path
from vip_users.views import UserAPIView

urlpatterns = [
    path('vip-users/', UserAPIView.as_view(), name='vip-users'),
]