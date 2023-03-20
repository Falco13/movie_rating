from django.urls import path
from movie_rating.views import HomePage, AboutView, detail_movie

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('detail/<slug:slug>/', detail_movie, name="detail"),
    path('about/', AboutView.as_view(), name="about"),
]
