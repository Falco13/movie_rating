from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username',
                    'first_name',
                    'last_name',
                    'email',
                    'date_of_birth',
                    'is_staff',
                    'is_superuser',
                    'date_joined',
                    'last_login',
                    ]
