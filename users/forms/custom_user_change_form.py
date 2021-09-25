from django.contrib.auth.forms import UserChangeForm
from users.models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ['email', 'password']
