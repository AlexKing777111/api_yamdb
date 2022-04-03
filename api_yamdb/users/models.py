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

    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELDS = "email"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
