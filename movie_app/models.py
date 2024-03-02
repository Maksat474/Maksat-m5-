from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def count_reviews(self):
        return self.reviews.all().count()

    @property
    def get_avarage_rating(self, object):
        total_stars = sum(review.stars for review in object.reviews.all())
        num_reviews = object.reviews.count()


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.IntegerField(default=1, choices=[(i, i * '*') for i in range(6)])

    def __str__(self):
        return self.text