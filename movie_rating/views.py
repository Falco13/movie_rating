from django.shortcuts import render
from django.views.generic import ListView
from movie_rating.models import Movie


class HomePage(ListView):
    model = Movie
    template_name = 'movie_rating/home.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        return context

    def get_queryset(self):
        return Movie.objects.filter(is_active=True)
