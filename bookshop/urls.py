from django.urls import path

from . import views
from .views import MyBookApiView, UserInfoApiView, BookManageApiView, BookModelViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("modelview", views.BookModelViewSet)

urlpatterns = [
    path("bookshop/", MyBookApiView.as_view(), name="bookstore"),
    path("user/", UserInfoApiView.as_view(), name="user"),
    path("b/<int:pk>", BookManageApiView.as_view(), name="user"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/logout", views.LogoutApiView.as_view(), name="logout"),
    # path("modelview/", view=BookModelViewSet.as_view(), name="modelviewset"),
]

# urlpatterns = router.urls

