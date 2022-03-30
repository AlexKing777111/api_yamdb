import email
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
    email = models.EmailField("e-mail", unique=True, blank=False)
    role = models.CharField(
        choices=USER_ROLES,
        max_length=10,
        verbose_name="Роль пользователя",
        default="user",
    )
