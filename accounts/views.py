from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from accounts.forms import UserRegisterForm, UserLoginForm, EditUserForm, PasswordChangingForm
from accounts.models import User
from movie_rating.models import Rating


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
        else:
            messages.error(request, 'Registration error!')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong password or user name!')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You are logged out of your account')
    return redirect('home')


@login_required
def profile(request):
    user_ratings = Rating.objects.filter(user=request.user).order_by('-created_date')
    ratings_data = []
    for rating in user_ratings:
        movie = rating.movie
        average_rating = Rating.objects.filter(movie=movie, is_active=True).aggregate(Avg('rating'))['rating__avg']
        total_votes = Rating.objects.filter(movie=movie, is_active=True).aggregate(Count('rating'))['rating__count']

        ratings_data.append({
            'movie': movie,
            'rating': rating.rating,
            'average_rating': average_rating or 0,
            'total_votes': total_votes or 0,
        })
    return render(request, 'accounts/profile.html', {'ratings_data': ratings_data})


@login_required
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User profile has been deleted')
        return redirect('home')
    return render(request, 'accounts/delete_user.html', {'user': user})


@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditUserForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User data has been changed')
            return redirect('accounts:profile')
        else:
            messages.error(request, form.errors)
    else:
        form = EditUserForm(instance=user)
    return render(request, 'accounts/edit_user.html', {'user': user, 'form': form})


class UserPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = PasswordChangingForm
    success_url = reverse_lazy('accounts:profile')
    success_message = 'Your password has been changed successfully'
