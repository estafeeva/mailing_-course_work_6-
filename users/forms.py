from users.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации пользователя.
    """
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
