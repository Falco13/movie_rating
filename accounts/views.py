from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import UserRegisterForm, UserLoginForm, EditUserForm
from accounts.models import User


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
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You are logged out of your account')
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


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
            return redirect('home')
        else:
            messages.error(request, form.errors)
    else:
        form = EditUserForm(instance=user)
    return render(request, 'accounts/edit_user.html', {'user': user, 'form': form})
