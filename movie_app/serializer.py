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