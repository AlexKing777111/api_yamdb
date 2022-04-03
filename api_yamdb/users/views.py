from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework import filters, viewsets
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from .models import User
from django.core.mail import send_mail
from .serializers import (
    EmailSerializer,
    ConfirmationCodeSerializer,
    UserSerializer,
)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_confirmation_code(request):
    if request.method == "POST":
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        username = serializer.validated_data.get("username")
        user, _ = User.objects.get_or_create(email=email, username=username)
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
@permission_classes([permissions.AllowAny])
def send_token(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    confirmation_code = serializer.validated_data.get("confirmation_code")
    username = serializer.validated_data.get("username")
    user = get_object_or_404(User, username=username)
    if confirmation_code is None:
        return Response("Введите confirmation_code")
    if username is None:
        return Response("Введите email")
    token_check = default_token_generator.check_token(user, confirmation_code)
    if token_check is True:
        refresh = RefreshToken.for_user(user)
        return Response(f"Ваш токен:{refresh.access_token}")
    return Response("Неправильный confirmation_code или email.")


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    permission_classes = (permissions.IsAdminUser,)
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
        permission_classes=[permissions.IsAuthenticated],
        url_path="me",
        url_name="me",
    )
    def get_me(self, request):
        user = self.request.user
        self.check_object_permissions(self.request, user)
        serializer = self.get_serializer(user)
        if request.method == "PATCH":
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.data)
