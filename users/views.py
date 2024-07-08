import random
import secrets
import string

from django.contrib.auth.views import PasswordResetView
from django.views.generic import CreateView
from users.models import User
from users.forms import UserRegisterForm, PasswordResetForm
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect

from config.settings import EMAIL_HOST_USER

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")


    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}"

        #print(url)
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейдите по ссылке для подтверждения почты: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class UserResetPasswordView(PasswordResetView):
    model = User
    form_class = PasswordResetForm
    template_name = 'users/password_reset.html'

    def form_valid(self, form):
        form_email = form.cleaned_data.get("email")
        user = User.objects.get(email=form_email)
        characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(random.choice(characters) for _ in range(10))

        user.set_password(new_password)
        user.save()

        #print(url)
        send_mail(
            subject="Смена пароля",
            message=f"Привет, используйте новый пароль: {new_password}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return redirect(reverse("users:login"))


class UserResetPasswordDoneView(PasswordResetView):
    model = User
    form_class = PasswordResetForm
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users:login')


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))