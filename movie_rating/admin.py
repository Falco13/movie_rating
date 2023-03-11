from django.contrib import admin
from movie_rating.models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'year', 'country', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size': '20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    # }


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'created_date', 'rating', 'is_active']
    # readonly_fields = ['movie', 'user', 'created_date', 'rating']
    list_editable = ['is_active']
