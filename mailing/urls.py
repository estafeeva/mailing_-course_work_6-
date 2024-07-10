from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from mailing.apps import MailingConfig
from mailing.views import (
    TestPageView, MailingMessageListView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView,
)

app_name = MailingConfig.name

urlpatterns = [
    path("", views.home_view, name="home"),
#    path("", MailingMessageListView.as_view(), name="home"),

    path("client/", ClientListView.as_view(), name="list_client"),
    path("client/create", ClientCreateView.as_view(), name="create_client"),
    path("client/<int:pk>", ClientDetailView.as_view(), name="detail_client"),
    path("client/update/<int:pk>", ClientUpdateView.as_view(), name="update_client"),
#    path("client/delete/<int:pk>", ClientDeleteView.as_view(), name="delete_client"),
]
