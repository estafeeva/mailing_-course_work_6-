from random import shuffle

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from pytils.translit import slugify

from mailing.forms import ClientForm, MailingSettingsForm, MailingMessageForm
from mailing.models import MailingSettings, MailingMessage, Client, Blog, MailingAttempt
from mailing.services import get_current_datetime

@cache_page(60)
def home_view(request):
    """количество рассылок всего,
    количество активных рассылок,
    количество уникальных клиентов для рассылок,
    три случайные статьи из блога.
    """
    mailing_total = len(MailingSettings.objects.all())
    mailing_active = len(MailingSettings.objects.filter(status__in=[MailingSettings.STARTED]))
    clients_total = len(Client.objects.all())
    blog_list = [item for item in Blog.objects.all()]
    shuffle(blog_list)

    context = {"mailing_total": mailing_total,
               "mailing_active": mailing_active,
               "clients_total": clients_total,
               "blog_list": blog_list[:3],
               }
    return render(request, "mailing/home.html", context=context)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    login_url = "/users/login/"


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    login_url = "/users/login/"


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:list_client")
    login_url = "/users/login/"

    def form_valid(self, form):

        if form.is_valid():
            self.object = form.save()
            user = self.request.user
            self.object.owner = user
            self.object.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form))


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:list_client")
    login_url = "/users/login/"

    def form_valid(self, form):

        if form.is_valid():
            self.object = form.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form))


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client  # Модель
    success_url = reverse_lazy(
        "mailing:list_client"
    )  # Адрес для перенаправления после успешного удаления
    login_url = "/users/login/"

    def test_func(self):
        pk = self.kwargs.get("pk")
        client = get_object_or_404(Client, pk=pk)
        return (self.request.user == client.owner) or self.request.user.is_superuser


##########################


class MailingMessageListView(LoginRequiredMixin, ListView):
    model = MailingMessage
    login_url = "/users/login/"


class MailingMessageDetailView(LoginRequiredMixin, DetailView):
    model = MailingMessage
    login_url = "/users/login/"


class MailingMessageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy("mailing:list_mailingmessage")
    login_url = "/users/login/"

    def form_valid(self, form):

        if form.is_valid():
            self.object = form.save()
            user = self.request.user
            self.object.owner = user
            self.object.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form))


class MailingMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy("mailing:list_mailingmessage")
    login_url = "/users/login/"

    def form_valid(self, form):

        if form.is_valid():
            self.object = form.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form))


class MailingMessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MailingMessage  # Модель
    success_url = reverse_lazy(
        "mailing:list_mailingmessage"
    )  # Адрес для перенаправления после успешного удаления
    login_url = "/users/login/"

    def test_func(self):
        pk = self.kwargs.get("pk")
        mailingmessage = get_object_or_404(MailingMessage, pk=pk)
        return (
            self.request.user == mailingmessage.owner
        ) or self.request.user.is_superuser



class MailingMessageListView(ListView):
    model = MailingMessage
    login_url = "/users/login/"

    """def get_queryset(self):
        return get_mailing_from_cache()"""

##########################


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings
    login_url = "/users/login/"


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings
    login_url = "/users/login/"


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailing:list_mailingsettings")
    login_url = "/users/login/"

    def form_valid(self, form):

        if form.is_valid():
            self.object = form.save()
            user = self.request.user
            self.object.owner = user
            self.object.save()
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form))


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailing:list_mailingsettings")
    login_url = "/users/login/"

    def form_valid(self, form):

        if form.is_valid():
            self.object = form.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class MailingSettingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MailingSettings  # Модель
    success_url = reverse_lazy(
        "mailing:list_mailingsettings"
    )  # Адрес для перенаправления после успешного удаления
    login_url = "/users/login/"

    def test_func(self):
        pk = self.kwargs.get("pk")
        mailingsettings = get_object_or_404(MailingSettings, pk=pk)
        return (
            self.request.user == mailingsettings.owner
        ) or self.request.user.is_superuser


class TestPageView(TemplateView):
    template_name = "mailing/test.html"


class BlogListView(ListView):
    model = Blog

    """get_queryset выводит в список статей только те, которые имеют положительный признак публикации"""

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    """При открытии отдельной статьи get_object увеличивает счетчик просмотров"""

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog  # Модель
    fields = (
        "title",
        "content",
        "preview",
    )  # Поля для заполнения при создании
    success_url = reverse_lazy(
        "mailing:blog_list"
    )  # Адрес для перенаправления после успешного создания

    """form_valid при создании динамически формирует slug name для заголовка"""

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog  # Модель
    fields = (
        "title",
        "content",
        "preview",
    )  # Поля для редактирования
    #    success_url = reverse_lazy('catalog:blog_list') # Адрес для перенаправления после успешного редактирования

    """form_valid при создании динамически формирует slug name для заголовка"""

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    """После успешного редактирования записи get_success_url перенаправляет пользователя на просмотр этой статьи"""

    def get_success_url(self):
        return reverse("mailing:blog", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog  # Модель
    success_url = reverse_lazy(
        "mailing:blog_list"
    )  # Адрес для перенаправления после успешного удаления


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    login_url = "/users/login/"


def change_status(request, pk):
    """
    Активирует/деактивирует статус настройки рассылки.
    """

    mailing = get_object_or_404(MailingSettings, pk=pk)

    if mailing is None:
        return render(request, 'mailing/home.html')
    else:
        if not (request.user == mailing.owner or
                request.user.has_perm('mailing.deactivate_mailingsettings')):
            return render(request, 'mailing/home.html')
        else:

            if mailing.status == mailing.COMPLETED:

                if mailing.first_sent_datetime < get_current_datetime():
                    mailing.status = mailing.STARTED
                else:
                    mailing.status = mailing.CREATED
            else:
                mailing.status = mailing.COMPLETED

            mailing.save()

            return redirect('mailing:list_mailingsettings')
