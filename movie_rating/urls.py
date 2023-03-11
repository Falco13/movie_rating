from django.urls import path
from movie_rating.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
]
