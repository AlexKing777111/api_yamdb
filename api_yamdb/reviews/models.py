from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField()
    year = models.IntegerField(verbose_name="Год")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="Категория",
    )
    genre = models.ManyToManyField(Genre, related_name="Жанр")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-pk",)


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name="Произведение",
    )
    text = models.TextField(
        verbose_name="Текст",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор"
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Оценка",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "title"], name="unique_review"
            )
        ]
        ordering = ["-pub_date"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        default_related_name = "reviews"

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Отзыв",
    )
    text = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
