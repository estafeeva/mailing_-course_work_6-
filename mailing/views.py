from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from mailing.models import MailingSettings, MailingMessage


def test_view(request):
    context = {"object": "mailing"}
    return render(request, "mailing/test.html", context=context)


"""class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    login_url = "/users/login/"


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    login_url = "/users/login/"


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