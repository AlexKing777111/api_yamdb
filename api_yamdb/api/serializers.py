from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Category, Genre, Title


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
        exclude = 'id'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
