from users.views import change_status
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.views import UserCreateView, email_verification, UserResetPasswordView, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("password_reset/", UserResetPasswordView.as_view(), name="password_reset"),
    path("", UserListView.as_view(), name="list"),
    path(
        "change_status/<int:pk>",
        change_status,
        name="change_status",
    ),
]
