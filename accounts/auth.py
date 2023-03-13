from django.contrib.auth import backends, get_user_model
from django.db.models import Q


class EmailOrUsernameModelBackend(backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        try:
            user = user_model.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            user_model.set_password(password)
