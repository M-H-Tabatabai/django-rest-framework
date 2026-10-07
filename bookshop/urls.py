from django.urls import path

from .views import MyBookApiView, UserInfoApiView, BookManageApiView

urlpatterns = [
    path("bookshop/", MyBookApiView.as_view(), name="bookstore"),
    path("user/", UserInfoApiView.as_view(), name="user"),
    path("b/<int:pk>", BookManageApiView.as_view(), name="user"),
]