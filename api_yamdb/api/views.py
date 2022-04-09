from django_filters.rest_framework import DjangoFilterBackend
<<<<<<< HEAD
from django.db.models import Avg
=======
>>>>>>> 12c2d9b024c3ebcf1eba83e6c917a1dd5ddcd8ea
from rest_framework import filters, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Category, Genre, Review, Title

from api.filters import TitleFilter
from api.permissions import IsAdmin, ReadOnly, ReviewCommentPermission
<<<<<<< HEAD
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitlePOSTSerializer, TitleSerializer)
=======
from api.serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitlePOSTSerializer,
    TitleSerializer,
)
>>>>>>> 12c2d9b024c3ebcf1eba83e6c917a1dd5ddcd8ea


class GetPostDelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    permission_classes = (ReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
<<<<<<< HEAD
        if self.action not in ('list', 'retrieve'):
=======
        if self.action not in ("list", "retrieve"):
>>>>>>> 12c2d9b024c3ebcf1eba83e6c917a1dd5ddcd8ea
            return (IsAdmin(),)
        return super().get_permissions()


class TitleViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('-id')
=======
    queryset = Title.objects.all()
>>>>>>> 12c2d9b024c3ebcf1eba83e6c917a1dd5ddcd8ea
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    permission_classes = (ReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
<<<<<<< HEAD
        if self.action in ('list', 'retrieve'):
=======
        if self.action in ("list", "retrieve"):
>>>>>>> 12c2d9b024c3ebcf1eba83e6c917a1dd5ddcd8ea
            return TitleSerializer
        return TitlePOSTSerializer

    def get_permissions(self):
<<<<<<< HEAD
        if self.action not in ('list', 'retrieve'):
=======
        if self.action not in ("list", "retrieve"):
>>>>>>> 12c2d9b024c3ebcf1eba83e6c917a1dd5ddcd8ea
            return (IsAdmin(),)
        return super().get_permissions()


class CategoryViewSet(GetPostDelViewSet):
    lookup_field = "slug"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(GetPostDelViewSet):
    lookup_field = "slug"
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (ReviewCommentPermission,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, id=title_id)
        serializer.save(
            author=self.request.user,
            title=title,
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (ReviewCommentPermission,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        title_id = self.kwargs.get("title_id")
        review = get_object_or_404(Review, id=review_id, title_id=title_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get("review_id")
        title_id = self.kwargs.get("title_id")
        review = get_object_or_404(Review, id=review_id, title_id=title_id)
        serializer.save(
            author=self.request.user,
            review=review,
        )
