from django.urls import path
from .views import HelloWorldView, hello_world

urlpatterns = [
    path("hello/", hello_world, name="hello_world"),
    path("hello-class/", HelloWorldView.as_view(), name="hello_world_class"),
]