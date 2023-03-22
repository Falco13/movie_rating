from django import forms
from movie_rating.models import Rating


class RatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=Rating.RATE_CHOICES,
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Rating
        fields = ['rating']
