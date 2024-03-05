from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = models.Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, object):
        return object.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    avarage_rating = serializers.SerializerMethodField()
    class Meta:
        model = models.Movie
        fields = 'id title description duration director reviews avarage_rating'.split()

    def get_avarage_rating(self, object):
        total_stars = sum(review.stars for review in object.reviews.all())
        num_reviews = object.reviews.count()

        if total_stars >0:
            return total_stars / num_reviews
        else:
            return 0.0


class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=5, max_length=40)

    def validate_name_min_length(value, min_length):
        if len(value) < min_length:
            raise serializers.ValidationError(f'Минимальная длина для поля {value} равна {min_length}')
        return value


class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.CharField()
    director_id = serializers.IntegerField()
    # reviews = serializers.ListField(child=ReviewCreateSerializer())

    def validate_director_id(self, director_id):
        if models.Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f"Director with id {director_id} does not exist")

    # def validate(self, attrs):
    #     id = attrs['director_id']
    #     try:
    #         models.Director.objects.get(id=id)
    #     except:
    #         raise ValidationError(f"Director with id {id} does not exist")
    #     return attrs


class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.CharField()
    stars = serializers.IntegerField()

    def validate_movie(self, movie):
        if models.Movie.objects.filter(id=movie).count() == 0:
            raise ValidationError(f"Movie with id {movie} does not exist")