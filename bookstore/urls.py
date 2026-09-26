from django.urls import path

from .views import bookstoreView

urlpatterns = [
    path("books/", bookstoreView.as_view(), name="bookstore"),
]