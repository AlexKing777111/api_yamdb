from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (ConfirmationCodeSerializer, EmailSerializer,
                          UserSerializer)


@api_view(["POST"])
def send_confirmation_code(request):
    if request.method == "POST":
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        user, _ = User.objects.get_or_create(email=email)
        token = default_token_generator.make_token(user)
        send_mail(
            subject="Confirmation code!",
            message=str(token),
            from_email="admin@yamdb.ru",
            recipient_list=[
                email,
            ],
        )
        return Response("Confirmation code отправлен на ваш Email.")


@api_view(["POST"])
def send_token(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    confirmation_code = serializer.validated_data.get("confirmation_code")
    email = serializer.validated_data.get("email")
    user = get_object_or_404(User, email=email)
    if confirmation_code is None:
        return Response("Введите confirmation_code")
    if email is None:
        return Response("Введите email")
    token_check = default_token_generator.check_token(user, confirmation_code)
    if token_check is True:
        refresh = RefreshToken.for_user(user)
        return Response(f"Ваш токен:{refresh.access_token}")
    return Response("Неправильный confirmation_code или email.")


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    lookup_field = "username"
    queryset = User.objects.all()
    search_fields = ("user__username",)
    ordering = ("username",)

    @action(
        detail=False,
        methods=(
            "get",
            "patch",
        ),
        url_path="me",
        url_name="me",
    )
    def get_me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)
        if request.method == "PATCH":
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.data)
