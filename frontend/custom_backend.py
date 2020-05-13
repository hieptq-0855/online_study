from django.contrib.auth.hashers import check_password
from frontend.models import User


def authenticate(email=None, password=None):
    try:
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None
