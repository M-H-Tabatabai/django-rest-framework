from django.urls import path

from .views import MyBookApiView, UserInfoApiVeiew

urlpatterns = [
    path("bookshop/", MyBookApiView.as_view(), name="bookstore"),
    path("user/", UserInfoApiVeiew.as_view(), name="user"),
]