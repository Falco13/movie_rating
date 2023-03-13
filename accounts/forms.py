from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username or email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='repeat password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(label='date of birthday', widget=forms.DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'date_of_birth')
