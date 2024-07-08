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


class TestPageView(TemplateView):
    template_name = "mailing/test.html"


class MailingMessageListView(ListView):
    model = MailingMessage
    login_url = "/users/login/"

    """def get_queryset(self):
        return get_mailing_from_cache()"""