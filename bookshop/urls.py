from django.urls import path

from .views import MyBookApiView

urlpatterns = [
    path("bookshop/", MyBookApiView.as_view(), name="bookstore"),
]