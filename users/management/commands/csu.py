from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Создание тестовых пользователей с разными возможностями:
    is_active, is_staff, is_superuser.
    """
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin2@example.com")
        user.set_password("12345678")

        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.save()
