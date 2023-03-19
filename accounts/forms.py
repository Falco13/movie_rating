from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username or email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your username'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'repeat password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'}))
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'your date of birth'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'date_of_birth')


class DateInput(forms.DateInput):
    input_type = 'date'


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(),
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your old password'}))
    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your new password'}))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'repeat your new password'}))
