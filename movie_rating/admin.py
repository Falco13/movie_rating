from django.contrib import admin
from movie_rating.models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description_short', 'year', 'country', 'is_active']
    prepopulated_fields = {'slug': ('title',)}

    @staticmethod
    def description_short(obj: Movie):
        if len(obj.description) < 50:
            return obj.description
        return obj.description[:50] + '...'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'created_date', 'rating', 'is_active']
    list_editable = ['is_active']
