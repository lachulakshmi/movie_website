
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name



class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('U', 'Universal'),
        ('U/A', 'Parental Guidance'),
        ('A', 'Adult'),
        ('S', 'Special'),
    ]
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    youtube_trailer_link = models.URLField()
    added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'



