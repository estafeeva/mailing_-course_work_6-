from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from mailing.apps import MailingConfig
from mailing.views import (
    TestPageView, MailingMessageListView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView,
    ClientDeleteView, MailingSettingsListView, MailingSettingsCreateView, MailingSettingsDeleteView,
    MailingMessageDetailView, MailingMessageCreateView, MailingMessageUpdateView, MailingMessageDeleteView,
    MailingSettingsDetailView, MailingSettingsUpdateView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView,
    BlogDeleteView,
)

app_name = MailingConfig.name


urlpatterns = [
    path("", views.home_view, name="home"),
#    path("", MailingMessageListView.as_view(), name="home"),

    path("client/", ClientListView.as_view(), name="list_client"),
    path("client/create", ClientCreateView.as_view(), name="create_client"),
    path("client/<int:pk>", ClientDetailView.as_view(), name="detail_client"),
    path("client/update/<int:pk>", ClientUpdateView.as_view(), name="update_client"),
    path("client/delete/<int:pk>", ClientDeleteView.as_view(), name="delete_client"),

    path("mailingsettings/", MailingSettingsListView.as_view(), name="list_mailingsettings"),
    path("mailingsettings/create", MailingSettingsCreateView.as_view(), name="create_mailingsettings"),
    path("mailingsettings/<int:pk>", MailingSettingsDetailView.as_view(), name="detail_mailingsettings"),
    path("mailingsettings/update/<int:pk>", MailingSettingsUpdateView.as_view(), name="update_mailingsettings"),
    path("mailingsettings/delete/<int:pk>", MailingSettingsDeleteView.as_view(), name="delete_mailingsettings"),

    path("mailingmessage/", MailingMessageListView.as_view(), name="list_mailingmessage"),
    path("mailingmessage/create", MailingMessageCreateView.as_view(), name="create_mailingmessage"),
    path("mailingmessage/<int:pk>", MailingMessageDetailView.as_view(), name="detail_mailingmessage"),
    path("mailingmessage/update/<int:pk>", MailingMessageUpdateView.as_view(), name="update_mailingmessage"),
    path("mailingmessage/delete/<int:pk>", MailingMessageDeleteView.as_view(), name="delete_mailingmessage"),

    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_list/blog/<int:pk>", BlogDetailView.as_view(), name="blog"),
    path("blog_list/blog/create", BlogCreateView.as_view(), name="create"),
    path("blog_list/blog/update/<int:pk>", BlogUpdateView.as_view(), name="update"),
    path("blog_list/blog/delete/<int:pk>", BlogDeleteView.as_view(), name="delete"),
]
