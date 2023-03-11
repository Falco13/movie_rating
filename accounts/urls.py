from django.urls import path
from accounts.views import register, user_logout, user_login

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
]
