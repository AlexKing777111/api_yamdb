from rest_framework import viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitlePOSTSerializer, TitleSerializer)
from rest_framework import mixins, viewsets
from reviews.models import Category, Genre, Title


class GetPostDelViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # permission_classes =

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializer
        return TitlePOSTSerializer


class CategoryViewSet(GetPostDelViewSet):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes =


class GenreViewSet(GetPostDelViewSet):
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes =
