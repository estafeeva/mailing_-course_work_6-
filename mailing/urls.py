from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from mailing.apps import MailingConfig
from mailing.views import (
    TestPageView, MailingMessageListView,
)

app_name = MailingConfig.name

urlpatterns = [
    path("", MailingMessageListView.as_view(), name="home"),
    path("test/", views.test_view, name="test"),
]
