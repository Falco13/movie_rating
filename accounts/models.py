from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='date of birth')
