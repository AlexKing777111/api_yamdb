from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Category, Genre, Title, Review, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class TitlePOSTSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(many=False,
                                queryset=Category.objects.all(),
                                slug_field='slug')
    genre = SlugRelatedField(many=True,
                             queryset=Genre.objects.all(),
                             slug_field='slug')

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = SlugRelatedField(many=True,
                             queryset=Genre.objects.all(),
                             slug_field='slug')

    class Meta:
        fields = '__all__'
        model = Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    # title = serializers.SlugRelatedField(
    #     slug_field='id',
    #     read_only=True,
    # )

    class Meta:
        fields = '__all__'
        model = Review
        read_only_fields = ('title',)
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('author', 'title')
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment
