from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from movie_rating.models import Movie, Rating
from movie_rating.forms import RatingForm


class HomePage(ListView):
    model = Movie
    template_name = 'movie_rating/home.html'
    context_object_name = 'movies'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        return context

    def get_queryset(self):
        return Movie.objects.filter(is_active=True)


def detail_movie(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    ratings_counts = Rating.objects.filter(movie=movie, is_active=True).values('rating').annotate(
        count=Count('rating')).order_by('rating')
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = request.POST.get('rating')
            if Rating.objects.filter(user=request.user, movie=movie).exists():
                Rating.objects.filter(user=request.user, movie=movie).delete()
                Rating.objects.create(user=request.user, rating=rating, movie=movie)
                messages.success(request, 'You have changed your rating!')
            else:
                Rating.objects.create(user=request.user, rating=rating, movie=movie)
                messages.success(request, 'Thank you for your review of the movie!')
            return HttpResponseRedirect(reverse('detail', args=(slug,)))
    else:
        form = RatingForm()
        user_rating = None
        if request.user.is_authenticated:
            user_rating = Rating.objects.filter(user=request.user, movie=movie).first()
        return render(request, 'movie_rating/detail.html', context={'ratings_counts': ratings_counts,
                                                                    'movie': movie,
                                                                    'form': form,
                                                                    'user_rate': user_rating})


class AboutView(TemplateView):
    template_name = 'movie_rating/about.html'
