from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet, send_confirmation_code, send_token

v1_router = DefaultRouter()

v1_router.register(r"users", UsersViewSet, basename="users")

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/auth/signup/", send_confirmation_code),
    path("v1/auth/token/", send_token),
]
