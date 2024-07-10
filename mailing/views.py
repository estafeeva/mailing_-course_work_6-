from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from mailing.forms import ClientForm
from mailing.models import MailingSettings, MailingMessage, Client


def home_view(request):
    context = {"object": "mailing"}
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

            return self.render_to_response(
                self.get_context_data(form=form)
            )


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

            return self.render_to_response(
                self.get_context_data(form=form)
            )

"""    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.set_published") and user.has_perm("catalog.change_description") and user.has_perm("catalog.change_category"):
            return ProductModeratorForm
        raise PermissionDenied"""

"""class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client  # Модель
    success_url = reverse_lazy(
        "mailing:home"
    )  # Адрес для перенаправления после успешного удаления
    login_url = "/users/login/"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ClientForm
        if user.has_perm("mailing.set_published") and user.has_perm("catalog.change_description") and user.has_perm("catalog.change_category"):
            return ClientModeratorForm
        raise PermissionDenied
"""


"""

class ClientCreateUpdate(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form, object_is_new=True):
        if form.is_valid():
            set_owner(self, form, object_is_new)
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ClientCreateView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form, object_is_new=True):
        if form.is_valid():
#            set_owner(self, form, object_is_new)
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))




class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, ClientCreateUpdate, UpdateView):
    login_url = "/users/login/"

    def form_valid(self, form, *args):
        return super().form_valid(form, False)

    def test_func(self):
        return check_user_is_owner_or_su(self, Client)


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')
    login_url = "/users/login/"

    def test_func(self):
        return check_user_is_owner_or_su(self, Client)


###


"""


class TestPageView(TemplateView):
    template_name = "mailing/test.html"


class MailingMessageListView(ListView):
    model = MailingMessage
    login_url = "/users/login/"


    """def get_queryset(self):
        return get_mailing_from_cache()"""