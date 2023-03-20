from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView, DetailView
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


def detail_movie(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'movie_rating/detail.html', context={'movie': movie})


class AboutView(TemplateView):
    template_name = 'movie_rating/about.html'
