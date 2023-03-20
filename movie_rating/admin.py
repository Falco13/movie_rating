from django.contrib import admin
from movie_rating.models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description_short', 'year', 'country', 'is_active', 'rating_short']
    prepopulated_fields = {'slug': ('title',)}

    @staticmethod
    def description_short(obj: Movie):
        if len(obj.description) < 50:
            return obj.description
        return obj.description[:50] + '...'

    @staticmethod
    def rating_short(obj: Movie):
        if len(str(obj.average_rating)) < 3:
            return str(obj.average_rating)
        return str(obj.average_rating)[:3]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'created_date', 'rating', 'is_active']
    list_editable = ['is_active']

    def get_queryset(self, request):
        return Rating.objects.select_related('movie', 'user').all()
