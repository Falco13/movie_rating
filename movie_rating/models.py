from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse

from accounts.models import User
from django.utils.text import slugify


class Movie(models.Model):
    title = models.CharField(max_length=55, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    year = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    @property
    def average_rating(self):
        return self.rating.filter(is_active=True).aggregate(Avg('rating'))['rating__avg']

    @property
    def count_votes(self):
        return self.rating.filter(is_active=True).aggregate(Count('rating'))['rating__count']

    class Meta:
        ordering = ['title']


class Rating(models.Model):
    RATE_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Rating creation date')
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Movie: {self.movie} is rated {self.rating}'

    class Meta:
        unique_together = ('movie', 'user',)

    @property
    def percentage_vote(self):
        total_votes = Rating.objects.filter(movie=self.movie).count()
        rating_count = Rating.objects.filter(movie=self.movie, rating=self.rating).count()
        if total_votes == 0:
            return 0
        else:
            vote_in_percentage = (rating_count / total_votes) * 100
        return vote_in_percentage
