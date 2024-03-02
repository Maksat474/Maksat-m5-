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


class ReviewCreateSerializer(serializers.Serializer):
    stars = serializers.IntegerField(min_value=1, max_value=5)
    text = serializers.CharField(max_length=60)


class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=10)
    description = serializers.CharField()
    price = serializers.FloatField()
    category_id = serializers.IntegerField()
    reviews = serializers.ListField(child=ReviewCreateSerializer())

    # list_ = serializers.ListField()
    # object_ = ObjectCreateSerializer()

    def validate(self, category_id):
        if models.Category.objects.filter(id=category_id).count() == 0:
            raise ValidationError(f"Category with id {id} does not exist")


class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=5, max_length=40)


class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.CharField()
    stars = serializers.IntegerField(default=1)


