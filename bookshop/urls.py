from django.urls import path

from .views import MyBookApiView, UserInfoApiView

urlpatterns = [
    path("bookshop/", MyBookApiView.as_view(), name="bookstore"),
    path("user/", UserInfoApiView.as_view(), name="user"),
]