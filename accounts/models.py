import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='date of birth')

    def age(self):
        if self.date_of_birth:
            return int((datetime.date.today() - self.date_of_birth).days / 365.25)
        else:
            return None
