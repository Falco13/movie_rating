from django.urls import path
from accounts.views import register, user_logout, user_login, profile, delete_user

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('profile/delete_user/<int:pk>', delete_user, name='delete_user'),
]
