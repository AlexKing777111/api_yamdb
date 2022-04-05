from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_ROLES = (
        ("user", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Администратор"),
    )

    bio = models.TextField(
        "Биография",
        blank=True,
    )
    email = models.EmailField("email", unique=True, null=False)
    role = models.CharField(
        choices=USER_ROLES,
        max_length=10,
        verbose_name="Роль пользователя",
        default="user",
    )
    password = models.CharField("password", max_length=128, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_superuser = models.BooleanField(default=False, null=True)

    USERNAME_FIELDS = "email"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def is_moderator(self):
        return self.role == "moderator"

    @property
    def is_user(self):
        return self.role == "user"
