from django.urls import path
from movie_rating.views import HomePage, AboutView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
]
